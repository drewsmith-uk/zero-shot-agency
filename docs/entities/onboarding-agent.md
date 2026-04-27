---
title: Onboarding Agent
created: 2026-04-23
updated: 2026-04-26
type: entity
tags: [tool, architecture]
sources: []
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# Onboarding Agent

The `onboarding_agent.py` script serves as the "Agentic Client Onboarding" system. It ingests a client URL, scrapes it for H1/H2 tags and its `llms.txt` file, and uses the OpenAI API to perform a live GEO gap analysis, outputting a custom strategy brief in Markdown.

## Functionality
- Takes target domain via CLI.
- Scrapes metadata and extracts headers.
- Queries `llms.txt`.
- Leverages `gpt-4o` to generate the strategy brief to capture leads.


## Related Concepts & Entities
- [[agentic-onboarding]]
- [[citation-mechanics]]
- [[geo-tactics]]
- [[llms-txt-generator]]
- [[llms-txt-template]]
