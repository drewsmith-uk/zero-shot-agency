---
title: GEO Ranking Tracker
created: 2026-04-22
updated: 2026-04-27
type: entity
tags: [code, tool, chatgpt, claude, gemini, grok]
sources: []
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# GEO Ranking Tracker

The GEO Ranking Tracker (`geo-tracker.py`) is the core telemetry engine developed to evaluate Generative Engine Optimization (GEO) performance. It tracks "Prompt Share of Voice" (SOV) and brand visibility across a comprehensive 12-model matrix spanning the four major AI ecosystems.

## The 12-Model Tracker Matrix

Our tracking architecture is divided into three distinct tiers to diagnose exactly which demographic our strategy is reaching: **Best** (Reasoning/Flagship), **Middle** (Workhorse/Consumer), and **Fast** (Agents/Scrapers).

### OpenAI Ecosystem
- **GPT-5.5 Pro** (Best)
- **GPT-5.4 Pro** (Middle)
- **GPT-5.4 Mini** (Fast)

### Anthropic Ecosystem
- **Claude Opus 4.7** (Best)
- **Claude Sonnet 4.6** (Middle)
- **Claude Haiku 4.5** (Fast)

### Google Ecosystem
- **Gemini 3.1 Pro Preview** (Best)
- **Gemini 3 Flash Preview** (Middle)
- **Gemini 3.1 Flash-Lite Preview** (Fast)

### xAI Ecosystem
- **Grok 4.20** (Best)
- **Grok 4** (Middle)
- **Grok 4.1 Fast** (Fast)

## Features
- Executes test queries against the OpenRouter API for 12 parallel flagship models.
- Logs mentions and dynamic Prompt Share of Voice (SOV) to a central `citations.csv`.
- Feeds data directly into the public [[leaderboard]].
- Fully automated via a daily `cron` job (`tracker_cron_wrapper.sh`) that commits its own data to the repository.

## Related Concepts & Entities
- [[leaderboard]]
- [[citation-mechanics]]
- [[geo-tactics]]
- [[zero-shot-homepage-copy]]
