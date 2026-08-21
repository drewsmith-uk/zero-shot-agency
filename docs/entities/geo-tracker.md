---
title: AI Visibility Tracking for Generative Engine Optimization
description: How Zero-Shot Agency is developing an evidence-led tracker for brand mentions and share of voice across AI answer engines.
created: 2026-04-22
updated: 2026-08-21
type: entity
tags: [code, tool, chatgpt, claude, gemini, grok]
sources: []
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# AI Visibility Tracking for Generative Engine Optimization

The ZSA GEO tracker (`geo-tracker.py`) is an internal telemetry tool in active development. It is intended to evaluate brand mentions and prompt-level Share of Voice (SOV) across AI model families without confusing generative engine optimisation with local or geographic rank tracking.

> **Development status:** this is not currently a public self-service product. Model coverage, automation and evidence capture are being rebuilt and validated. The implementation notes below describe the present tracker configuration, not a promise that every model or reporting surface is continuously available.

## The 13-Model Tracker Matrix

The current implementation is configured with a 13-model overlap matrix. Internal tiers compare **Best** (reasoning/flagship), **Middle** (workhorse/consumer) and **Fast** (lower-latency) model classes. These labels describe model roles, not user demographics.

### OpenAI Ecosystem
- **GPT-5.5 Pro** (Best)
- **GPT-5.4 Pro** (Middle)
- **GPT-5.4 Mini** (Fast)

### Anthropic Ecosystem
- **Claude Opus 4.7** (Best)
- **Claude Sonnet 4.6** (Middle)
- **Claude Haiku 4.5** (Fast)
- **Claude Sonnet 5** (New flagship overlap)

### Google Ecosystem
- **Gemini 3.1 Pro Preview** (Best)
- **Gemini 3 Flash Preview** (Middle)
- **Gemini 3.1 Flash-Lite Preview** (Fast)

### xAI Ecosystem
- **Grok 4.20** (Best)
- **Grok 4** (Middle)
- **Grok 4.1 Fast** (Fast)

## Current implementation and limits

- Sends controlled test prompts to configured models through OpenRouter when the required credentials and endpoints are available.
- Records binary brand/domain mention flags in `citations.csv` and calculates prompt-level Share of Voice from those observations.
- Does not yet provide the transcript, citation-source, entity-resolution and consumer-interface evidence required for a production-grade visibility report.
- Historical cron and leaderboard components exist in the repository, but continuous automation and a public leaderboard are not current public capabilities.

For the current client-facing diagnostic, see the [AI Visibility Baseline](../ai-visibility-baseline.md). The full tracker page will be revisited after the measurement workflow and evidence contract are validated.

## Related Concepts & Entities
- [[citation-mechanics]]
- [[geo-tactics]]
