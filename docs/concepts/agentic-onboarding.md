---
title: Agentic Client Onboarding
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [architecture, strategy]
---

# Agentic Client Onboarding Architecture

The Agentic Client Onboarding system is the primary lead-capture mechanism for Zero-Shot Agency. Instead of a traditional "Contact Us" form, prospects interact with an AI-driven auditing engine that provides immediate, personalized value by analyzing their current Generative Engine Optimization (GEO) readiness.

## 1. URL Ingestion
- **Input Mechanism:** The prospect enters their primary domain or target landing page URL via a simple intake form on the Zero-Shot homepage.
- **Initial Verification:** A lightweight preliminary check verifies the URL is accessible and not blocking scrapers.

## 2. Live GEO Gap Analysis
The core analytical engine runs a real-time, automated audit focusing on bot-readiness and semantic clarity:
- **Crawler Compatibility Check:**
  - Evaluates the presence and richness of `llms.txt` and `llms-full.txt`.
  - Checks if the site has a machine-readable directory structure optimized for RAG (Retrieval-Augmented Generation) parsers.
- **Semantic Structure Evaluation:**
  - Scrapes the target URL for core HTML elements (H1, H2, structural tags).
  - Assesses whether the information hierarchy aligns with [[geo-tactics]] and [[citation-mechanics]].
- **LLM Baseline Test (Mock Queries):**
  - Sends a simulated query to major LLMs (e.g., Perplexity, Claude, ChatGPT) to measure the baseline citation frequency and "Prompt Share of Voice" for the prospect's brand vs. their competitors.

## 3. Custom Strategy Brief Generation
Once the data is synthesized, the system leverages a large language model (via API) to generate a bespoke strategy document:
- **The Output (Agentic Strategy Brief):** A personalized, markdown-formatted report outlining the prospect's current GEO gaps.
- **Actionable Recommendations:** Suggests concrete fixes (like implementing an `llms.txt` or restructuring content for better citation probability).
- **Lead Capture Hand-off:** The generated brief is delivered to the prospect's email (or presented via a secure link), establishing Zero-Shot Agency as the authoritative expert and prompting a strategy call with the human team.

This architecture seamlessly transitions a prospect from a casual visitor into an engaged lead by providing immediate, empirical proof of their GEO vulnerabilities.
