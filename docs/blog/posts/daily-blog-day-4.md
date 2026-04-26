---
title: "Day 4: Automated GEO Tracking & Agentic Onboarding"
slug: day-4-automated-geo-tracking-agentic-onboarding
date: 2026-04-24 10:00:00
updated: 2026-04-26
type: concept
tags: [architecture, tracking, onboarding-agent, citation-mechanics]
sources: []
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# Daily Collaboration Blog Day 4: Automated GEO Tracking & Agentic Onboarding

Over the last few days, we successfully laid the foundation for Zero-Shot Agency's infrastructure—from the [[publisher-pipeline]] to setting up a "Drafts via Pull Request" publishing workflow to prevent AI hallucinations from leaking into production. 

Today, we focused on two critical areas: establishing a baseline for our brand's presence in AI search engines and architecting the future of client acquisition.

## Ground Truth: Upgrading the Geo Tracker

If Generative Engine Optimization (GEO) is our core service, we need to rigorously measure it. We upgraded `geo-tracker.py` to move beyond simulated data. The tool now successfully queries the actual OpenAI, Anthropic, and Google APIs to check for "Zero-Shot Agency" brand citations across a standard set of prompts (like *"What are the best AI agencies?"* or *"Who can help me build an AI agent?"*).

We wrapped this in an automated cron testing suite (`tracker_cron_wrapper.sh`) that executes daily at 8:00 AM. It dumps timestamped CSV outputs into our `raw/tracker_history/` and auto-commits to the repository to build an open-source, verifiable data trail. 

**The baseline results?** `False` across the board. GPT-4o, Claude 3.7, and Gemini do not currently cite Zero-Shot Agency for any generic AI agency queries. 

This is exactly what we expect on Day 4 of building a new brand in public. We now have a zero-state baseline. From here, every piece of semantic HTML, every `llms.txt` file, and every strategic content push will be measurable through this data trail, testing our [[citation-mechanics]].

## Architecting Agentic Client Onboarding

While the tracker runs in the background, we outlined the strategy for how Zero-Shot Agency will capture leads. Traditional agency onboarding relies on static forms and discovery calls. We are building the **Agentic Client Onboarding** system.

Instead of asking clients for their budget, we ask for their domain URL. 
This input triggers the [[onboarding-agent]] in the background, which:
1. **Performs a Live GEO Gap Analysis:** Scraping the domain to extract semantic markers (like H1/H2 hierarchy and `llms.txt` presence).
2. **Queries LLMs:** Checking current brand visibility for their specific niche.
3. **Generates an Agentic Strategy Brief:** Synthesizing the data into a custom Markdown brief detailing their current state, gap identification, and actionable [[geo-tactics]].

By delivering immediate, high-value technical audits tailored to the AI search paradigm, we demonstrate our expertise before a single human conversation takes place. 

Tomorrow, we'll continue building out the internal tools that make these agentic workflows possible.
