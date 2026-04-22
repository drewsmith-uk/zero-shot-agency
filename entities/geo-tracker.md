---
title: GEO Ranking Tracker
created: 2026-04-22
updated: 2026-04-22
type: entity
tags: [code, tool, chatgpt, claude, gemini]
sources: []
---

# GEO Ranking Tracker

The GEO Ranking Tracker (`geo-tracker.py`) is a baseline script developed to evaluate Generative Engine Optimization (GEO) performance. It tracks Share of Voice (SoV) and visibility for a target domain across major AI models.

## Supported Targets
- **GPT-4o** (OpenAI)
- **Claude 3.7 Sonnet** (Anthropic)
- **Gemini 1.5 Pro** (Google)

## Features
- Executes test queries against multiple API endpoints.
- Checks if the target domain is explicitly mentioned in the generated output.
- Outputs a formatted ranking and visibility report.

## Related Concepts
- Implements tracking for strategies defined in [[geo-tactics]].
- Evaluates metrics relevant to [[citation-mechanics]].