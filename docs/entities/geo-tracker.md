---
title: GEO Ranking Tracker
created: 2026-04-22
updated: 2026-04-26
type: entity
tags: [code, tool, chatgpt, claude, gemini]
sources: []
---

# GEO Ranking Tracker

The GEO Ranking Tracker (`geo-tracker.py`) is a baseline script developed to evaluate Generative Engine Optimization (GEO) performance. It tracks Share of Voice (SoV) and visibility for a target domain across major AI models.

## Supported Targets
- **GPT-4o** (OpenAI)
- **GPT-5.5 Pro** (OpenRouter)
- **Claude 3.7 Sonnet** (Anthropic)
- **Claude Sonnet 4.6** (OpenRouter)
- **Gemini 1.5 Pro** / **Gemini 2.5 Flash** (Google)
- **Gemini 3.1 Pro Preview** (OpenRouter)

## Features
- Executes test queries against multiple API endpoints.
- Checks if the target domain is explicitly mentioned in the generated output.
- Outputs a formatted ranking and visibility report.

## Related Concepts
- Implements tracking for strategies defined in [[geo-tactics]].
- Evaluates metrics relevant to [[citation-mechanics]].