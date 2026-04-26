---
title: Internal Automation Tools
created: 2026-04-23
updated: 2026-04-26
type: summary
tags: [tool, artifact, architecture]
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# Internal Automation Tools

Zero-Shot Agency relies on custom Python scripts to track Prompt Share of Voice (SOV) and generate bot-native assets. These tools automate the collection and publishing mechanics required for Generative Engine Optimization (GEO).

## 1. GEO Tracker (`geo-tracker.py`)

A script to monitor major LLMs (OpenAI, Anthropic, Gemini) and track how frequently they mention or cite a specific target domain across a set of target queries. This gives us our "Share of Voice" metric.

### Requirements
```bash
pip install openai anthropic google-generativeai
```

Set the required API keys in your environment:
- `OPENAI_API_KEY` (for GPT-4o)
- `ANTHROPIC_API_KEY` (for Claude 3.7 Sonnet)
- `GEMINI_API_KEY` (for Gemini 1.5 Pro)

*Note: If an API key is missing, the script will skip querying that specific model and print a warning.*

### Usage
```bash
python geo-tracker.py --domain example.com --queries "query 1" "query 2" "query 3"
```

### Arguments
- `--domain` (Required): The target domain to track (e.g., 'example.com').
- `--queries` (Required): A space-separated list of queries to test.

### Output
The script performs synchronous queries (with a 1-second delay between queries to respect rate limits) against all configured LLM APIs. It then prints a Share of Voice report detailing the percentage of times the target domain was mentioned in the output for each engine.

---

## 2. LLMs.txt Generator (`llms-txt-generator.py`)

A specialized web crawler that traverses a domain and builds a standardized `/llms.txt` and `llms-full.txt` file. This is crucial for formatting site content correctly for LLM and bot consumption.

### Requirements
```bash
pip install requests beautifulsoup4 markdownify
```

### Usage
```bash
python docs/tools/llms-txt-generator.py https://example.com --max-pages 50 --output ./site
```

### Arguments
- `url` (Required): Starting URL to crawl (e.g., `https://example.com`).
- `--max-pages`: Maximum number of pages to crawl (Default: 50).
- `--output`: Output directory for the generated files (Default: current directory).
- `--delay`: Delay between requests in seconds to respect server loads (Default: 0.5).

### Output
- `llms.txt`: A markdown index file containing links to all crawled pages.
- `llms-full.txt`: A concatenated markdown file containing the parsed and cleaned text of all main content across the crawled domain.

---

## 3. Publisher Pipeline (`publisher_pipeline.py`)

*(Documentation pending - under development)* 
Automates the deployment of semantic content.

*(Source code is maintained in the `tools/` and `docs/tools/` directory of our repository).*