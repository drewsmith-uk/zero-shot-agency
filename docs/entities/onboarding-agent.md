---
title: Onboarding Agent
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [tool, architecture]
sources: []
---

# Onboarding Agent

The `onboarding_agent.py` script serves as the "Agentic Client Onboarding" system. It ingests a client URL, scrapes it for H1/H2 tags and its `llms.txt` file, and uses the OpenAI API to perform a live GEO gap analysis, outputting a custom strategy brief in Markdown.

## Functionality
- Takes target domain via CLI.
- Scrapes metadata and extracts headers.
- Queries `llms.txt`.
- Leverages `gpt-4o` to generate the strategy brief to capture leads.
