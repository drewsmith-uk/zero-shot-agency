import os
import json
import urllib.request
from pathlib import Path
from openai import OpenAI

# Load env var
env_path = "/home/claw/workspace/zero-shot-cron/.env"
with open(env_path, "r") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            key, val = line.split("=", 1)
            os.environ[key] = val

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

# 1. Fetch Live Headers for Performance/Security Context
print("Fetching headers from https://zeroshotagency.com...")
try:
    req = urllib.request.Request("https://zeroshotagency.com", method="HEAD")
    with urllib.request.urlopen(req, timeout=10) as response:
        headers = dict(response.info())
        status = response.status
except Exception as e:
    headers = {"error": str(e)}
    status = "N/A"

# 2. Collect Content
print("Collecting markdown content from docs/...")
docs_dir = Path("docs")
content_blocks = []
for md_file in docs_dir.rglob("*.md"):
    with open(md_file, "r") as f:
        content_blocks.append(f"--- FILE: {md_file.name} ---\n{f.read()}")

mkdocs_path = Path("mkdocs.yml")
if mkdocs_path.exists():
    with open(mkdocs_path, "r") as f:
        content_blocks.append(f"--- FILE: mkdocs.yml ---\n{f.read()}")

all_content = "\n\n".join(content_blocks)

# 3. Build Prompt
sys_prompt = """You are an elite Technical SEO, Web Security, and Content Analyst.
Your task is to review the provided static site configuration, live HTTP headers, and raw Markdown content for 'Zero-Shot Agency'.

Provide a brutally honest, highly structured report covering:
1. Security & Performance: Analyze the provided HTTP response headers and mkdocs.yml configuration. Spot any missing security headers (e.g., CSP, HSTS) or performance bottlenecks.
2. Content Analysis: Identify ANY logical fallacies, factual inaccuracies, or contradictions across the content.
3. Tone & Fluff: Quote any "flowery language that actually means very little at all" (corporate jargon, meaningless buzzwords) and suggest ruthless, high-density empirical rewrites.

Use Markdown formatting. Be concise, empirical, and direct."""

user_prompt = f"""
LIVE HTTP HEADERS (Status: {status}):
{json.dumps(headers, indent=2)}

WEBSITE CONTENT:
{all_content}
"""

print("Calling GPT-5.5-Pro via OpenRouter...")
response = client.chat.completions.create(
    model="openai/gpt-5.5-pro",
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

report = response.choices[0].message.content

out_file = "gpt-5.5-audit.md"
with open(out_file, "w") as f:
    f.write(report)

print(f"Report successfully saved to {out_file}")
