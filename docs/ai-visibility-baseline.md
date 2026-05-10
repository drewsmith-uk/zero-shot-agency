---
title: AI Visibility Baseline
description: Measure whether AI systems can find, cite, and explain your brand before you spend on GEO, content, or technical fixes.
---

# AI Visibility Baseline

## Turn AI visibility from guesswork into evidence

Your buyers are already asking ChatGPT, Perplexity, Gemini, Claude, and search-backed answer surfaces which tools, agencies, products, and sources they should trust.

The AI Visibility Baseline shows what those systems can currently find, cite, and say about your brand.

It is a fixed-scope diagnostic for CMOs, founders, and technical growth teams who need evidence before they rewrite content, buy another tool, or launch a vague AI visibility programme.

You get a baseline report, retained evidence appendix, technical GEO hygiene review, competitor/source map, and ranked action plan.

No guaranteed rankings. No promised citations. No black-box theatre. Just the evidence you need to decide what to fix next.

[Book an AI Visibility Baseline call](contact.md)

## The problem: buyers now ask AI before they ask sales

Search is no longer a single list of links.

A buyer can ask an AI system:

- "Who are the best agencies for Generative Engine Optimization?"
- "How do I get my brand cited by ChatGPT and Perplexity?"
- "Which AI search visibility tools should a B2B SaaS team use?"
- "What are the alternatives to our current SEO agency?"

The answer may name your competitors, cite third-party sources, summarise old positioning, or omit you completely.

That creates a measurement problem.

Traditional SEO tools can tell you where pages rank. They cannot, on their own, prove whether an answer engine mentioned your brand, cited your URL, used a competitor as the source of truth, or failed to surface your evidence in a defined run.

The baseline gives you a defensible starting point:

- where your brand appears;
- where it is cited;
- where competitors are recommended instead;
- which sources answer engines surface;
- where answers are wrong, thin, stale, or unhelpful;
- which technical gaps may be limiting retrieval;
- what should be fixed, tested, or parked.

## What the baseline measures

The AI Visibility Baseline measures five practical things.

### 1. Visibility

Do answer engines mention your brand for the prompts your buyers actually ask?

We classify each captured answer as visible, cited, mentioned, absent, no-answer, or proxy-only. The point is not to invent a universal ranking score. The point is to show what happened in a defined measurement window and which prompts matter commercially.

### 2. Citations and source paths

When an answer includes sources, we record the URLs and domains displayed.

That shows whether the answer engine is citing your site, a competitor, a publisher, a marketplace, a review site, documentation, or another source layer entirely.

A mention without a citation is not the same as a cited recommendation. The baseline separates them.

### 3. Competitor presence

We track which competitors, tools, agencies, publishers, or alternatives are named and cited.

That gives you a competitor visibility map: who appears, where they appear, which source assets support them, and which prompts create the most commercial risk.

### 4. Answer quality

A brand can be visible and still be misrepresented.

We record whether answers are accurate, stale, vague, under-evidenced, wrongly positioned, or missing the proof a buyer would need to trust the recommendation.

### 5. Technical GEO hygiene

AI visibility is not just copywriting.

If source material is hard to retrieve, parse, attribute, or trust, strong positioning may never make it into an answer. We inspect the technical layer that supports retrievability and citation eligibility, including machine-readable surfaces, metadata, semantic extraction, canonical signals, schema where present, and answer-ready source pages.

Technical hygiene does not guarantee citations. It improves the odds that the right evidence can be found, parsed, and reused.

## How evidence is captured

We do not infer AI visibility from rankings alone.

Each material claim in the baseline must map to captured evidence: an answer-engine transcript or screenshot, a displayed citation/source, a live URL check, or repo/source inspection for technical claims.

Every official run uses a structured evidence record.

| Field | Purpose |
| --- | --- |
| `run_id` | Groups prompts, platforms, and evidence from one measurement window. |
| `prompt_id` | Gives each prompt a stable identifier. |
| `prompt_category` | Separates buyer-intent, comparison, informational, technical, and measurement prompts. |
| `exact_prompt` | Stores the exact wording used. |
| `platform` | Records the system or surface tested, such as ChatGPT, Perplexity, Gemini, Claude, or a proxy search surface. |
| `model_or_surface` | Captures the displayed model, search mode, API route, or answer surface where available. |
| `account_state` | Notes logged-in/logged-out state, paid/free tier, or unknown account context. |
| `geo_or_locale` | Records geography, locale, or language caveats where known. |
| `device/browser if relevant` | Captures browser, device, or UI context when it may affect the run. |
| `timestamp_utc` | Fixes the observation in time. |
| `raw_transcript_or_screenshot_path` | Points to the retained raw answer, screenshot, or API output. |
| `source_urls_displayed` | Lists the URLs shown by the answer surface. |
| `source_titles_domains` | Records displayed titles and domains for source interpretation. |
| `zsa_mention_status` | Tracks whether Zero-Shot Agency is mentioned. For client work, this field becomes the client brand mention status. |
| `zsa_citation_status` | Tracks whether Zero-Shot Agency is cited. For client work, this field becomes the client brand citation status. |
| `zsa_url_cited` | Records cited ZSA URLs. For client work, this field becomes the cited client URL. |
| `competitors_named` | Lists competitors or alternatives named in the answer. |
| `competitors_cited` | Lists competitors or alternatives supported by displayed citations. |
| `answer_quality_notes` | Captures accuracy, stale claims, positioning gaps, missing proof, and anomalies. |
| `classification` | One of: visible, cited, mentioned, absent, no-answer, proxy-only. |
| `limitation_flags` | Notes access limits, geography, personalization, source opacity, rate limits, no citations, proxy-only status, or model variance. |
| `reviewer_initials` | Identifies the human reviewer responsible for classification QA. |
| `hash_or_checksum_of_saved_evidence` | Verifies that retained evidence has not silently changed. |

Weak, absent, no-answer, and proxy-only results stay in the evidence set. They are not deleted because they make the report look less flattering.

Answer engines vary by model, geography, account state, freshness, interface, and sampling. We label those limitations instead of hiding them.

## Scoring and classification

The baseline uses simple classifications before it uses scores.

### Classification states

- **Cited:** the brand appears and a relevant owned URL is displayed as a source.
- **Mentioned:** the brand appears, but no owned URL is cited.
- **Visible:** the brand appears in the answer or recommendation set, with citation status recorded separately.
- **Absent:** the answer responds to the prompt, but the brand does not appear.
- **No-answer:** the platform gives no usable answer because of refusal, block, timeout, login wall, rate limit, or tool failure.
- **Proxy-only:** the evidence comes from search/citation-surface checks, not a captured answer-engine transcript.

### Metrics we may report

Depending on scope and access, the report may include:

- **Prompt Share of Voice:** share of valid prompt/platform pairs where the brand is visible.
- **Citation rate:** share of citation-capable answers where an owned URL is cited.
- **Mentioned-not-cited rate:** where the brand is present but unsupported by owned-source citations.
- **Competitor recurrence:** which competitors appear most often and in which prompt categories.
- **Source overlap:** which domains recur across answer engines.
- **Model/platform variance:** where different systems answer the same prompt differently.
- **Prompt-category risk:** which buyer questions create the highest commercial exposure.

These metrics are directional and evidence-bounded. They are not universal ranking guarantees.

## What buyers get

The AI Visibility Baseline is designed to produce decisions, not a folder of screenshots nobody reads.

### 1. Executive readout

A clear summary of where the brand is visible, cited, absent, misrepresented, or displaced by competitors.

### 2. Prompt inventory

The agreed prompt set, grouped by category: buyer-intent, problem-aware, comparison, evaluation, technical/source trust, and category education.

### 3. Prompt Share of Voice table

A structured view of status by prompt, platform, category, and competitor presence.

### 4. Citation and source map

The URLs, domains, titles, and source patterns displayed by answer engines, with notes on whether each citation supports the claim being made.

### 5. Competitor visibility map

Who appears, who gets cited, which source assets support them, and where your brand is being displaced.

### 6. Answer-quality notes

Human review of accuracy, positioning, missing proof, stale claims, hallucinated or weak citations, and model/platform variance.

### 7. Technical GEO hygiene review

A practical inspection of the infrastructure that helps answer engines retrieve and interpret source material.

### 8. Evidence appendix

The retained evidence set: prompts, timestamps, transcripts or screenshots, displayed sources, limitation flags, reviewer notes, and hashes/checksums where used.

### 9. Ranked action plan

A concise backlog of what to fix now, what to test next, and what to park. Recommendations are tied to visibility risk, buyer impact, and implementation effort.

## Technical GEO hygiene

The baseline looks beyond copy.

A page can have strong messaging and still be a weak source for answer engines if the surrounding technical signals are thin, inconsistent, or hard to extract.

We inspect the technical layer that may affect retrievability:

- `llms.txt` and `llms-full.txt` availability and usefulness;
- sitemap and robots access;
- canonical signals;
- semantic HTML structure;
- metadata coverage and consistency;
- schema/JSON-LD where available;
- raw or machine-readable content routes;
- internal entity links and source relationships;
- answer-ready summaries and proof sections;
- indexable pages that directly support the claims a buyer asks about.

Technical findings require technical evidence.

Answer-engine transcripts alone do not prove whether a site has clean canonicals, useful schema, accessible machine-readable files, or extractable source structure. For those claims, the baseline uses live URL checks and/or repo/source inspection.

We also avoid deterministic causality unless the evidence supports it.

A report may say:

> Technical gaps may be limiting retrieval for this prompt category.

It should not say:

> Technical gaps are blocking retrieval.

unless the captured run and technical inspection justify that stronger claim.

## The ZSA self-experiment

Zero-Shot Agency is running itself through the same baseline.

Not as a victory lap. As method transparency.

The public ZSA experiment is designed to show the working parts:

- preregistered prompts;
- selected answer engines and surfaces;
- retained transcripts and screenshots;
- competitor and citation capture;
- weak, absent, no-answer, and proxy-only results preserved;
- technical limitations disclosed;
- 30/60/90-day remeasurement after interventions.

That matters because GEO work is easy to overclaim.

A credible baseline should show the uncomfortable parts too: where the brand is absent, where competitors are better supported, where answer engines cite the wrong sources, where search-surface proxies are not enough, and where the site's own infrastructure still needs hardening.

ZSA's own foundation is not presented as fully hardened. The current method treats the site the same way it treats a client site: inspect the evidence, label the gaps, fix what matters, and remeasure.

## Best fit / not fit

### Best fit

The AI Visibility Baseline is a strong fit for:

- B2B SaaS, agencies, consultancies, and technical services with complex buyer journeys;
- category creators whose buyers ask educational and comparison questions before sales calls;
- CMOs and founders who need evidence before funding GEO or AI visibility work;
- teams with competitors already appearing in answer-engine outputs;
- organisations that care about technical implementation, not just content briefs;
- brands willing to share real buyer questions, priority offers, competitor sets, and proof assets.

### Not fit

This is not a fit for:

- teams looking for a generic keyword report;
- brands that want guaranteed ChatGPT, Perplexity, Gemini, or Claude citations;
- organisations unwilling to retain evidence or confront weak results;
- teams that only want content recommendations without technical inspection;
- anyone expecting one audit to "fix" AI visibility;
- companies that need high-volume automated monitoring before they have a trusted baseline method.

## FAQ

### Is this an SEO audit?

No. SEO inputs matter, but the baseline measures answer-engine visibility, citations, source patterns, competitor presence, answer quality, and technical retrievability. Search rankings can support the analysis, but they do not prove answer-engine visibility by themselves.

### Can you guarantee we will be cited by ChatGPT, Perplexity, Gemini, or Claude?

No. Any agency promising guaranteed AI citations is overclaiming. We measure current visibility, identify likely limiting factors, and recommend evidence-led interventions.

### Why not just use a content optimisation tool?

Content tools can help with briefs and on-page optimisation. This baseline is broader: buyer prompts, answer surfaces, citations, competitors, source quality, technical hygiene, evidence retention, and implementation priorities.

### What if our brand is absent?

That is useful evidence. Absence shows which prompts, competitors, sources, and technical/content gaps need attention before money is spent on broad rewrites or tooling.

### How do you handle model variance?

We record platform, model or answer surface, timestamp, prompt, account state, geography/locale where known, and limitation flags. Variance is reported as a finding, not hidden.

### Do search rankings count as AI visibility?

Not by themselves. Search and citation-surface checks can show candidate sources, but they are labelled as proxy evidence unless captured inside the answer-engine output.

### Do technical checks prove why an AI system did or did not cite us?

Usually not on their own. Technical checks show whether source material is accessible, parseable, and well structured. They can identify gaps that may be limiting retrieval, but causality should only be stated when the evidence supports it.

### What do we need to provide?

Typically: primary domain, priority offers, buyer questions, target markets, competitors, approved claims, proof assets, and any useful Search Console, analytics, CRM, sales-call, or support inputs.

### What happens after the baseline?

You get a ranked action plan. Follow-on work may include technical hardening, source-backed content, proof assets, answer-ready pages, remeasurement, monitoring, or agentic workflows to keep the evidence current.

### Is this statistically definitive?

No. A baseline is a practical measurement window, not a universal law of AI visibility. The value is in retained evidence, repeatable prompts, clear limitations, and better decisions.

## Start with the evidence

Before you rewrite the site, buy another platform, or brief a content team, find out what AI systems can already see.

The AI Visibility Baseline gives you the measurement layer first: prompts, platforms, citations, competitors, technical hygiene, retained evidence, and a ranked action plan.

[Book an AI Visibility Baseline call](contact.md)

## Do-not-claim note for implementers and reviewers

Do not claim guaranteed AI rankings, guaranteed ChatGPT citations, guaranteed Perplexity visibility, or deterministic control over answer-engine outputs.

Do not imply that search rankings prove answer-engine visibility.

Do not imply that answer-engine transcripts alone verify technical hygiene. Technical GEO claims require live URL checks and/or repo/source inspection.

Do not imply that ZSA already dominates AI visibility or that ZSA Phase 1 is fully hardened.

Use current "ChatGPT" or "ChatGPT Search" terminology only; avoid deprecated prototype or browsing-era labels.

Use limitation-aware causality. Prefer "technical gaps may be limiting retrieval" unless captured evidence and technical inspection justify a stronger claim.
