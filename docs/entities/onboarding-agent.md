---
title: Onboarding Agent
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [tool, claude, chatgpt, architecture]
sources: []
---

# Onboarding Agent

The `onboarding_agent.py` script is a core utility of the Execution Framework designed to automate client ingestion and GEO gap analysis.

## Core Features
- Takes a target domain URL via CLI.
- Scrapes the site for `H1` and `H2` tags.
- Attempts to extract the `/llms.txt` file to understand the domain's AI indexing footprint.
- Feeds aggregated content to the OpenAI API (`gpt-4o`) using a custom system prompt.
- Outputs an 'Agentic Strategy Brief' tailored to the specific business, identifying Agentic Automation Opportunities and Technical & LLM Integration Strategy.

## Cross-References
- Supports the [[geo-tactics]] and [[agentic-onboarding]] workflows.
