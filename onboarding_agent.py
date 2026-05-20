#!/usr/bin/env python3
"""
onboarding_agent.py

Takes a domain URL as input, scrapes the site for H1/H2 tags and the llms.txt file,
and uses the OpenAI API to generate an 'Agentic Strategy Brief' formatted in Markdown.

Also supports structured Agentic Gap Analysis runs for prompt batches. Gap-analysis
artifacts are private-by-default and are written outside public docs unless an
explicit publication flag is supplied.
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import OrderedDict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

PROMPT_FIELDS = [
    "prompt",
    "intent",
    "target_entity_page",
    "priority",
    "source",
    "date_collected",
]

GAP_TAXONOMY = [
    "missing topic",
    "weak definition",
    "missing comparison",
    "missing proof/statistic",
    "missing citation",
    "weak developer implementation detail",
    "missing buyer objection",
    "missing entity relationship",
]

MEASUREMENT_FIELDS = [
    "date",
    "prompt",
    "intent",
    "engine/source",
    "zsa_present",
    "zsa_position",
    "zsa_cited_url",
    "competitor_cited_urls",
    "gap_cluster",
    "recommended_artifact",
    "review_status",
    "published_path",
    "notes",
]

TRACKING_QUERY_PREFIXES = ("utm_",)
TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "msclkid",
    "mc_cid",
    "mc_eid",
    "igshid",
    "sessionid",
    "session_id",
    "sid",
    "ref",
    "ref_src",
}
PRIVATE_REFERENCE_PATTERNS = [
    re.compile(r"\bprivate\s+client\b", re.IGNORECASE),
    re.compile(r"\bclient\s+audit\b", re.IGNORECASE),
    re.compile(r"\bprospect\s+(?:data|notes|diagnostics)\b", re.IGNORECASE),
    re.compile(r"\bAcme\s+Corp\b", re.IGNORECASE),
]
SECRET_PATTERN = re.compile(
    r"\b(?:api[_-]?key|token|secret|password|passwd|pwd|authorization)\s*[:=]\s*[^\s,;]+",
    re.IGNORECASE,
)
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
URL_PATTERN = re.compile(r"https?://[^\s)\]}>\"']+")


def setup_env(require_openai: bool = True):
    """Load environment variables and optionally ensure OpenAI API key is present."""
    load_dotenv()
    if require_openai and not os.getenv("OPENAI_API_KEY"):
        sys.stderr.write("Error: OPENAI_API_KEY environment variable is missing. Please set it in a .env file.\n")
        sys.exit(1)


def scrub_url(url: str) -> str:
    """Remove tracking query params/fragments from a URL while preserving useful path data."""
    if not url:
        return ""
    parsed = urlparse(url.strip())
    if not parsed.scheme or not parsed.netloc:
        return url.strip()
    kept_params = []
    for key, value in parse_qsl(parsed.query, keep_blank_values=True):
        lower_key = key.lower()
        if lower_key in TRACKING_QUERY_KEYS or lower_key.startswith(TRACKING_QUERY_PREFIXES):
            continue
        kept_params.append((key, value))
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, urlencode(kept_params), ""))


def scrub_private_content(text: str) -> str:
    """Scrub publishable text for URLs, emails, secrets, and obvious private references."""
    if text is None:
        return ""
    scrubbed = EMAIL_PATTERN.sub("[redacted-email]", str(text))
    scrubbed = SECRET_PATTERN.sub("[redacted-secret]", scrubbed)
    scrubbed = URL_PATTERN.sub(lambda match: scrub_url(match.group(0)), scrubbed)
    for pattern in PRIVATE_REFERENCE_PATTERNS:
        scrubbed = pattern.sub("[redacted-private-reference]", scrubbed)
    return scrubbed


def scrub_value(value):
    """Recursively scrub strings inside JSON-serialisable structures."""
    if isinstance(value, str):
        return scrub_private_content(value)
    if isinstance(value, list):
        return [scrub_value(item) for item in value]
    if isinstance(value, dict):
        return {key: scrub_value(item) for key, item in value.items()}
    return value


def validate_prompt_row(row: dict, row_number: int) -> dict:
    cleaned = {field: scrub_private_content(str(row.get(field, "")).strip()) for field in PROMPT_FIELDS}
    missing = [field for field in PROMPT_FIELDS if not cleaned[field]]
    if missing:
        raise ValueError(f"Prompt row {row_number} missing required fields: {', '.join(missing)}")
    cleaned["intent"] = classify_intent(cleaned["prompt"], cleaned["intent"])
    return cleaned


def load_prompt_batch(path: Path | str) -> list[dict]:
    """Load prompt metadata from CSV or JSON/JSONL with required review metadata fields."""
    prompt_path = Path(path)
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt batch not found: {prompt_path}")

    suffix = prompt_path.suffix.lower()
    rows: list[dict] = []
    if suffix == ".csv":
        with prompt_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
    elif suffix == ".json":
        data = json.loads(prompt_path.read_text(encoding="utf-8"))
        rows = data if isinstance(data, list) else data.get("prompts", [])
    elif suffix in {".jsonl", ".ndjson"}:
        rows = [json.loads(line) for line in prompt_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    else:
        raise ValueError("Prompt batch must be .csv, .json, .jsonl, or .ndjson")

    return [validate_prompt_row(row, index) for index, row in enumerate(rows, start=1)]


def classify_intent(prompt: str, supplied_intent: str = "") -> str:
    """Normalize or infer prompt intent as buyer, informational, or developer."""
    supplied = supplied_intent.strip().lower()
    if supplied in {"buyer", "informational", "developer"}:
        return supplied

    text = prompt.lower()
    if any(term in text for term in ["agency", "consultant", "vendor", "best", "expert", "hire", "service"]):
        return "buyer"
    if any(term in text for term in ["script", "api", "schema", "generator", "cli", "github", "implementation"]):
        return "developer"
    return "informational"


def scrape_headers(url: str) -> dict:
    """Scrape H1 and H2 tags from the given URL."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        h1s = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]
        h2s = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
        return {"h1": h1s, "h2": h2s}
    except requests.RequestException as e:
        sys.stderr.write(f"Warning: Failed to fetch or parse {url} for headers. Error: {e}\n")
        return {"h1": [], "h2": []}


def fetch_llms_txt(url: str) -> str:
    """Fetch the llms.txt file from the root of the domain."""
    parsed_url = urlparse(url)
    llms_url = f"{parsed_url.scheme}://{parsed_url.netloc}/llms.txt"
    try:
        response = requests.get(llms_url, timeout=10)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        sys.stderr.write(f"Warning: Failed to fetch llms.txt from {llms_url}. Error: {e}\n")
    return ""


def generate_strategy_brief(domain: str, headers: dict, llms_text: str) -> str:
    """Generate the strategy brief using OpenAI API."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"Please generate an Agentic Strategy Brief for the domain: {domain}.\n\n"
    prompt += "### Scraped Headers (H1 and H2)\n"
    if headers["h1"]:
        prompt += "**H1 Tags:**\n" + "\n".join(f"- {h1}" for h1 in headers["h1"]) + "\n"
    if headers["h2"]:
        prompt += "**H2 Tags:**\n" + "\n".join(f"- {h2}" for h2 in headers["h2"]) + "\n"
    if not headers["h1"] and not headers["h2"]:
        prompt += "No H1 or H2 tags were found on the website.\n"
    prompt += "\n### llms.txt Content\n"
    if llms_text:
        prompt += f"```text\n{llms_text}\n```\n"
    else:
        prompt += "No llms.txt file found at the root of the domain.\n"
    prompt += "\nBased on the information above, provide a professional Agentic Strategy Brief formatted in Markdown. Include a summary of the site's apparent purpose, potential areas where AI agents could add value, and recommended next steps for onboarding this domain into an agentic framework."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a strategic AI consultant analyzing website data to build agentic onboarding briefs."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        sys.stderr.write(f"Error: OpenAI API request failed. Details: {e}\n")
        sys.exit(1)


def save_brief(domain: str, content: str):
    """Save the markdown brief to a file."""
    output_dir = Path("concepts")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{domain.replace(':', '_')}_strategy_brief.md"
    filepath = output_dir / filename
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Success: Agentic Strategy Brief saved to {filepath}")
    except IOError as e:
        sys.stderr.write(f"Error: Could not save brief to {filepath}. Details: {e}\n")
        sys.exit(1)


def search_duckduckgo(query: str, max_results: int) -> list[dict]:
    """Collect DuckDuckGo search snippets for a prompt."""
    if max_results <= 0:
        return []
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        sys.stderr.write("Warning: duckduckgo-search library is missing; continuing without SERP results.\n")
        return []

    try:
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=max_results))
    except Exception as e:
        sys.stderr.write(f"Warning: DuckDuckGo search failed for '{query}'. Error: {e}\n")
        return []


def visible_questions(soup: BeautifulSoup) -> list[str]:
    questions: list[str] = []
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "summary", "button", "p", "li"]):
        text = " ".join(tag.get_text(" ", strip=True).split())
        if "?" in text and len(text) <= 220:
            questions.append(scrub_private_content(text))
    return list(dict.fromkeys(questions))[:20]


def cited_sources(soup: BeautifulSoup, base_domain: str) -> list[str]:
    sources: list[str] = []
    for link in soup.find_all("a", href=True):
        href = link["href"].strip()
        if not href.startswith(("http://", "https://")):
            continue
        parsed = urlparse(href)
        if parsed.netloc and parsed.netloc != base_domain:
            sources.append(scrub_url(href))
    return list(dict.fromkeys(sources))[:30]


def collect_competitor_page(result: dict) -> dict:
    """Scrape a result page into structured competitor/SERP evidence fields."""
    raw_url = result.get("href") or result.get("url") or ""
    clean_url = scrub_url(raw_url)
    parsed = urlparse(clean_url)
    evidence = {
        "url": clean_url,
        "domain": parsed.netloc,
        "title": scrub_private_content(result.get("title", "")),
        "snippet": scrub_private_content(result.get("body", result.get("snippet", ""))),
        "h1": [],
        "h2": [],
        "h3": [],
        "visible_faq_questions": [],
        "cited_sources": [],
        "date_fetched": datetime.now(timezone.utc).date().isoformat(),
        "fetch_status": "not_fetched",
    }
    if not clean_url:
        return evidence

    try:
        response = requests.get(clean_url, timeout=10, headers={"User-Agent": "Zero-Shot-Agentic-Gap-Analysis/1.0"})
        evidence["fetch_status"] = str(response.status_code)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        page_title = soup.title.get_text(strip=True) if soup.title else ""
        evidence["title"] = scrub_private_content(page_title or evidence["title"])
        evidence["h1"] = [scrub_private_content(h.get_text(" ", strip=True)) for h in soup.find_all("h1")]
        evidence["h2"] = [scrub_private_content(h.get_text(" ", strip=True)) for h in soup.find_all("h2")]
        evidence["h3"] = [scrub_private_content(h.get_text(" ", strip=True)) for h in soup.find_all("h3")]
        evidence["visible_faq_questions"] = visible_questions(soup)
        evidence["cited_sources"] = cited_sources(soup, parsed.netloc)
    except Exception as e:
        evidence["fetch_status"] = f"error: {e}"
    return evidence


def parse_frontmatter(markdown: str) -> tuple[dict, str]:
    if not markdown.startswith("---\n"):
        return {}, markdown
    end = markdown.find("\n---\n", 4)
    if end == -1:
        return {}, markdown
    frontmatter_text = markdown[4:end]
    body = markdown[end + 5 :]
    frontmatter: dict[str, str] = {}
    for line in frontmatter_text.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter, body


def extract_markdown_headings(body: str, level: int) -> list[str]:
    prefix = "#" * level + " "
    return [line.removeprefix(prefix).strip() for line in body.splitlines() if line.startswith(prefix)]


def extract_key_claims(body: str) -> list[str]:
    claims = []
    for line in body.splitlines():
        stripped = line.strip().lstrip("-0123456789. ")
        if len(stripped) > 45 and any(term in stripped.lower() for term in ["zsa", "zero-shot", "we ", "our ", "geo", "agent", "citation", "llm"]):
            claims.append(scrub_private_content(stripped))
    return claims[:12]


def compare_zsa_page(target_entity_page: str, docs_root: Path = Path("docs")) -> dict:
    """Extract comparable title/H1/H2/claim/link/citation/statistic fields from mapped docs content."""
    page_path = Path(target_entity_page)
    if not page_path.is_absolute():
        page_path = Path.cwd() / page_path
    if not page_path.exists() and target_entity_page.startswith("docs/"):
        page_path = Path.cwd() / target_entity_page
    if not page_path.exists():
        return {
            "path": target_entity_page,
            "exists": False,
            "title": "",
            "h1": [],
            "h2": [],
            "key_claims": [],
            "wikilinks": [],
            "citations_statistics": [],
            "last_updated": "",
        }

    content = page_path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(content)
    wikilinks = sorted(set(re.findall(r"\[\[([^\]]+)\]\]", body)))
    citations = sorted(set(URL_PATTERN.findall(body)))
    statistics = sorted(set(re.findall(r"\b\d+(?:\.\d+)?%|\b\d+(?:\.\d+)?x\b|\b\d+(?:,\d{3})+\b", body, flags=re.IGNORECASE)))
    return {
        "path": str(page_path.relative_to(Path.cwd())) if page_path.is_relative_to(Path.cwd()) else str(page_path),
        "exists": True,
        "title": scrub_private_content(frontmatter.get("title", "")),
        "h1": [scrub_private_content(item) for item in extract_markdown_headings(body, 1)],
        "h2": [scrub_private_content(item) for item in extract_markdown_headings(body, 2)],
        "key_claims": extract_key_claims(body),
        "wikilinks": wikilinks,
        "citations_statistics": [scrub_url(item) for item in citations] + statistics,
        "last_updated": frontmatter.get("updated", frontmatter.get("date", frontmatter.get("created", ""))),
    }


def tokenize(items: Iterable[str]) -> set[str]:
    tokens: set[str] = set()
    for item in items:
        tokens.update(re.findall(r"[a-z][a-z0-9-]{2,}", item.lower()))
    return tokens


def classify_gap(prompt: dict, competitor_terms: Iterable[str], zsa_terms: Iterable[str]) -> str:
    """Classify a candidate gap into the approved taxonomy."""
    intent = classify_intent(prompt.get("prompt", ""), prompt.get("intent", ""))
    competitor = tokenize(competitor_terms)
    zsa = tokenize(zsa_terms)
    missing = competitor - zsa

    if {"citation", "citations", "source", "sources", "reference", "references"} & missing:
        return "missing citation"
    if {"statistic", "statistics", "data", "study", "benchmark", "evidence", "proof"} & missing:
        return "missing proof/statistic"
    if {"compare", "comparison", "versus", "vs", "alternative", "alternatives"} & missing:
        return "missing comparison"
    if {"relationship", "entity", "entities", "graph", "wikilink", "internal"} & missing:
        return "missing entity relationship"
    if intent == "developer" and {"api", "script", "schema", "cli", "github", "implementation", "code"} & missing:
        return "weak developer implementation detail"
    if intent == "buyer" and {"pricing", "risk", "objection", "trust", "case", "proof", "vendor"} & missing:
        return "missing buyer objection"
    if {"definition", "define", "meaning", "what"} & missing:
        return "weak definition"
    return "missing topic"


def recommended_artifact_for_gap(gap_cluster: str, prompt: dict) -> str:
    mapping = {
        "missing topic": "Draft a dedicated section or concept page for the missing topic",
        "weak definition": "Strengthen the mapped page with a precise definition and examples",
        "missing comparison": "Add a comparison brief covering alternatives and differentiation",
        "missing proof/statistic": "Add citation-backed proof points or statistics after review",
        "missing citation": "Attach authoritative citations before any public claim is published",
        "weak developer implementation detail": "Add code-facing implementation detail, CLI examples, or schema notes",
        "missing buyer objection": "Add buyer-risk, trust, and objection-handling copy for review",
        "missing entity relationship": "Add wikilinks and entity relationship context in the knowledge graph",
    }
    target = prompt.get("target_entity_page", "mapped ZSA page")
    return f"{mapping[gap_cluster]} in {target}"


def build_measurement_row(
    prompt: dict,
    evidence: dict,
    gap_cluster: str,
    recommended_artifact: str,
    notes: str = "",
    date: str | None = None,
) -> OrderedDict:
    """Generate a review-pending measurement row with stable column order."""
    competitor_urls = evidence.get("competitor_cited_urls", [])
    if isinstance(competitor_urls, str):
        competitor_urls = [competitor_urls]
    row = OrderedDict()
    row["date"] = date or datetime.now(timezone.utc).date().isoformat()
    row["prompt"] = scrub_private_content(prompt.get("prompt", ""))
    row["intent"] = classify_intent(prompt.get("prompt", ""), prompt.get("intent", ""))
    row["engine/source"] = scrub_private_content(prompt.get("source", evidence.get("engine/source", "duckduckgo")))
    row["zsa_present"] = bool(evidence.get("zsa_present", False))
    row["zsa_position"] = evidence.get("zsa_position", "")
    row["zsa_cited_url"] = scrub_url(evidence.get("zsa_cited_url", ""))
    row["competitor_cited_urls"] = ";".join(scrub_url(url) for url in competitor_urls if url)
    row["gap_cluster"] = gap_cluster
    row["recommended_artifact"] = scrub_private_content(recommended_artifact)
    row["review_status"] = "pending"
    row["published_path"] = ""
    row["notes"] = scrub_private_content(notes)
    return row


def build_content_brief(prompt: dict, zsa_page: dict, gap_cluster: str, competitor_pages: list[dict], measurement_row: dict) -> str:
    """Build an internal review-pending content brief; not suitable for docs publication without approval."""
    lines = [
        "# Agentic Gap Analysis Brief",
        "",
        "review_status: pending",
        f"target_page: {prompt.get('target_entity_page', '')}",
        f"prompt: {prompt.get('prompt', '')}",
        f"intent: {measurement_row['intent']}",
        f"gap_cluster: {gap_cluster}",
        "",
        "## Evidence summary",
        f"- Competitor/SERP results captured: {len(competitor_pages)}",
        f"- ZSA page exists: {zsa_page.get('exists', False)}",
        f"- ZSA present in captured results: {measurement_row['zsa_present']}",
        "",
        "## Proposed patch direction",
        f"- {measurement_row['recommended_artifact']}",
        "- Keep this as an internal brief until Drew approves exact public copy.",
        "",
        "## Required citation/statistic",
        "- Add an authoritative citation or statistic if the recommendation makes a factual performance claim.",
        "",
        "## Affected wikilinks",
    ]
    wikilinks = zsa_page.get("wikilinks", [])
    lines.extend([f"- [[{link}]]" for link in wikilinks] or ["- None detected"])
    lines.extend([
        "",
        "## Risk notes",
        "- Raw SERP/answer-engine observations are volatile and should not be treated as public proof.",
        "- Privacy scrubber has removed obvious tracking, emails, secrets, and private/client references.",
        "- Public docs publication requires explicit approval; this run did not auto-publish to docs/.",
    ])
    return scrub_private_content("\n".join(lines) + "\n")


def safe_slug(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return slug[:80] or "gap-analysis"


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(scrub_value(data), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_measurement_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MEASUREMENT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def run_structured_gap_analysis(prompts: list[dict], output_dir: Path, max_results: int = 5) -> dict:
    """Run structured private gap analysis for prompt metadata rows."""
    output_dir.mkdir(parents=True, exist_ok=True)
    analyses = []
    measurement_rows = []

    for prompt in prompts:
        print(f"Analyzing prompt: {prompt['prompt']}")
        results = search_duckduckgo(prompt["prompt"], max_results=max_results)
        competitor_pages = [collect_competitor_page(result) for result in results]
        zsa_page = compare_zsa_page(prompt["target_entity_page"])

        competitor_terms: list[str] = []
        for page in competitor_pages:
            competitor_terms.extend([page.get("title", ""), page.get("snippet", "")])
            competitor_terms.extend(page.get("h1", []))
            competitor_terms.extend(page.get("h2", []))
            competitor_terms.extend(page.get("h3", []))
            competitor_terms.extend(page.get("visible_faq_questions", []))
            if page.get("cited_sources"):
                competitor_terms.append("citation sources")
        zsa_terms = [zsa_page.get("title", "")] + zsa_page.get("h1", []) + zsa_page.get("h2", []) + zsa_page.get("key_claims", []) + zsa_page.get("wikilinks", [])
        if zsa_page.get("citations_statistics"):
            zsa_terms.append("citation statistic")

        gap_cluster = classify_gap(prompt, competitor_terms, zsa_terms)
        zsa_result = next((index for index, page in enumerate(competitor_pages, start=1) if "zero-shot.agency" in page.get("domain", "")), None)
        competitor_urls = [page["url"] for page in competitor_pages if page.get("url") and "zero-shot.agency" not in page.get("domain", "")]
        evidence_for_row = {
            "zsa_present": zsa_result is not None,
            "zsa_position": zsa_result or "",
            "zsa_cited_url": next((page["url"] for page in competitor_pages if "zero-shot.agency" in page.get("domain", "")), ""),
            "competitor_cited_urls": competitor_urls,
        }
        recommended_artifact = recommended_artifact_for_gap(gap_cluster, prompt)
        row = build_measurement_row(
            prompt=prompt,
            evidence=evidence_for_row,
            gap_cluster=gap_cluster,
            recommended_artifact=recommended_artifact,
            notes="Structured gap-analysis run; review required before publication.",
            date=prompt.get("date_collected") or date.today().isoformat(),
        )
        brief = build_content_brief(prompt, zsa_page, gap_cluster, competitor_pages, row)
        slug = safe_slug(prompt["prompt"])
        brief_path = output_dir / "briefs" / f"{slug}.md"
        brief_path.parent.mkdir(parents=True, exist_ok=True)
        brief_path.write_text(brief, encoding="utf-8")

        analysis = {
            "prompt": prompt,
            "review_status": "pending",
            "competitor_serp_capture": competitor_pages,
            "zsa_page_comparison": zsa_page,
            "gap_cluster": gap_cluster,
            "recommended_artifact": recommended_artifact,
            "measurement_row": dict(row),
            "brief_path": str(brief_path),
        }
        write_json(output_dir / "evidence" / f"{slug}.json", analysis)
        analyses.append(analysis)
        measurement_rows.append(row)

    write_json(output_dir / "gap-analysis-results.json", {"review_status": "pending", "analyses": analyses})
    write_measurement_csv(output_dir / "measurement-rows.csv", measurement_rows)
    return {"analyses": analyses, "measurement_rows": measurement_rows, "output_dir": str(output_dir)}


def perform_gap_analysis(query: str, output_dir: Path = Path(".agentic_gap_analysis"), max_results: int = 5, intent: str = "", target_entity_page: str = "docs/strategy.md"):
    """Run single-query structured gap analysis. Private-by-default replacement for the older public Markdown writer."""
    prompt = {
        "prompt": query,
        "intent": classify_intent(query, intent),
        "target_entity_page": target_entity_page,
        "priority": "1",
        "source": "duckduckgo",
        "date_collected": datetime.now(timezone.utc).date().isoformat(),
    }
    result = run_structured_gap_analysis([prompt], output_dir=output_dir, max_results=max_results)
    print(f"Success: structured gap analysis saved under {output_dir}")
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Scrape a domain and generate an Agentic Strategy Brief, or run private-by-default structured Agentic Gap Analysis."
    )
    parser.add_argument("url", nargs="?", help="The target domain URL (e.g., https://example.com) for strategy brief")
    parser.add_argument("--analyze-gaps", type=str, help="Run a single prompt through structured private gap analysis.")
    parser.add_argument("--gap-batch", type=Path, help="CSV/JSON/JSONL prompt batch with prompt,intent,target_entity_page,priority,source,date_collected.")
    parser.add_argument("--gap-output-dir", type=Path, default=Path(".agentic_gap_analysis"), help="Private output directory for evidence, briefs, and measurement rows.")
    parser.add_argument("--gap-max-results", type=int, default=5, help="Maximum DuckDuckGo results to collect per prompt; use 0 for offline/local shape tests.")
    parser.add_argument("--gap-intent", choices=["buyer", "informational", "developer"], default="", help="Optional intent override for --analyze-gaps.")
    parser.add_argument("--gap-target-page", default="docs/strategy.md", help="Mapped ZSA docs page for --analyze-gaps.")
    parser.add_argument("--approve-publication", action="store_true", help="Reserved explicit approval flag for future public docs publication; current structured runner still writes private review artifacts only.")
    args = parser.parse_args()

    if not args.url and not args.analyze_gaps and not args.gap_batch:
        parser.print_help()
        sys.exit(1)

    needs_openai = bool(args.url) and not (args.analyze_gaps or args.gap_batch)
    setup_env(require_openai=needs_openai)

    if args.gap_batch:
        prompts = load_prompt_batch(args.gap_batch)
        run_structured_gap_analysis(prompts, output_dir=args.gap_output_dir, max_results=args.gap_max_results)
        print(f"Success: structured gap analysis saved under {args.gap_output_dir}")
        return

    if args.analyze_gaps:
        perform_gap_analysis(
            args.analyze_gaps,
            output_dir=args.gap_output_dir,
            max_results=args.gap_max_results,
            intent=args.gap_intent,
            target_entity_page=args.gap_target_page,
        )
        return

    if args.url:
        url = args.url
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        domain = urlparse(url).netloc
        if not domain:
            sys.stderr.write("Error: Invalid URL provided.\n")
            sys.exit(1)

        print(f"Scraping headers from {url}...")
        headers = scrape_headers(url)
        print(f"Checking for llms.txt at {domain}...")
        llms_text = fetch_llms_txt(url)
        print("Generating Agentic Strategy Brief...")
        brief_content = generate_strategy_brief(domain, headers, llms_text)
        save_brief(domain, brief_content)


if __name__ == "__main__":
    main()
