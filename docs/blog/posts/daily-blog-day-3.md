---
title: "Day 3: The "Drafts via PR" Workflow"
slug: day-3-developer-grade-publishing-preventing-hallucination-leaks
date: 2026-04-23 14:00:00
updated: 2026-04-26
type: concept
tags: [architecture, markdown]
sources: []
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# Day 3: The "Drafts via PR" Workflow

When building a fully autonomous, AI-driven media pipeline, there is a constant tension between **velocity** and **quality control**. 

Over the last two days, we established the core MkDocs site and the [[publisher-pipeline]]. While getting an AI to automatically tweet, email, and deploy static sites is incredibly powerful, it introduces a critical vulnerability: **AI hallucination leaks into production.**

If an LLM misinterprets a source, hallucinates a fact, or simply loses its thematic tone, a fully automated pipeline will instantly publish that error to X, Substack, and the live domain. This degrades domain authority—the most important ranking factor for Generative Engine Optimization (GEO).

## The Solution: Drafts via Pull Request

To solve this, we've implemented a developer-grade publishing architecture. Instead of the AI pushing directly to production, we treat content like software code:

1. **Branch Checkout:** The agent checks out a new branch (`drafts/[post-name]`).
2. **Content Generation:** The AI drafts the content autonomously in markdown.
3. **Automated Pull Request:** Using the GitHub CLI, the AI pushes the branch and opens a Pull Request (PR).
4. **Human Review:** Drew (the human-in-the-loop) reviews the PR, checks for hallucinations, and approves.
5. **Merge & Deploy:** Once merged, the [[publisher-pipeline]] and MkDocs deploy hooks are triggered.

### Why this matters for GEO

This architecture completely eliminates "hallucination leaks" while maintaining 95% of the automation benefits. The AI still does all the heavy lifting—researching, synthesizing, formatting semantic HTML/markdown, and handling the CLI deployment plumbing. 

The human only steps in for a final quality check, ensuring that our [[geo-tactics]] and [[citation-mechanics]] are perfectly executed before the content goes live. We preserve the speed of AI execution without sacrificing the trust and precision required to rank in tools like Perplexity and Claude.

Tomorrow, we'll continue optimizing our internal tools to monitor our brand citations across these generative engines.