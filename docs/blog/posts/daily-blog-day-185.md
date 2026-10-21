---
title: "Day 185: Google Trends Leaves Out the AI's Internal Searches"
date: 2026-10-22
slug: "day-185-google-trends-leaves-out-ai-internal-searches"
description: "Google Trends excludes internal searches made by AI Mode and AI Overviews. A source comparison shows what that means when commissioning GEO question research."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 185: Google Trends Leaves Out the AI's Internal Searches

Google Trends explicitly filters out internal searches made by AI Mode and AI Overviews.[1] If your GEO research brief asks someone to use Trends to count the related searches those features perform, the requested activity is outside the dataset.

That is a commissioning problem, not a reason to abandon Trends. A marketing director can use relative search-interest context while still needing a different investigation into how an AI response addresses a buyer's question.

The useful split is between interest expressed through searches and research performed inside an answer engine. Google's documentation describes both, but it does not make one a counter for the other.

<!-- more -->

## Read the two descriptions together

The Trends FAQ describes an anonymised, categorised and aggregated sample of actual search requests made to Google. Among its exclusions, it names searches made by Google products and services, explicitly including the internal searches of AI Mode and AI Overviews.[1]

Search Central describes what those AI features may do: use “query fan-out”, issuing multiple related searches across subtopics and data sources to develop a response. “May” matters; the documentation does not say every answer uses that technique.[2]

Put those statements together:

- **Trends supplies search-interest context** from its sampled, filtered data.
- **Fan-out describes possible internal research activity** involved in developing an AI response.
- **The Trends series excludes that internal activity**, rather than reporting it under a different label.

This is a specific boundary. It does not establish whether every initial question a person types into AI Mode is included or excluded. Nor does it support a blanket claim that Trends removes every AI-generated query. The documented exclusion concerns the internal searches named above.[1]

## Change the internal research; hold the chart inputs still

Here is a logical counterexample, not an observed Google experiment or a captured Trends chart.

Imagine two cases with identical inputs to the Trends calculation: the same included search sample, filters, time and geography, normalisation inputs and statistical-noise realisation. Now stipulate that the internal AI searches differ between the cases. One case involves internal research into a particular subtopic; the other does not.

The chart cannot distinguish those cases through that excluded activity. We have changed something the series does not count while holding its inputs fixed.

This does not claim those cases have occurred, or that real search behaviour and internal research are unrelated. It shows why the chart alone cannot identify whether that internal research happened. A larger Trends value cannot be converted into more fan-out, and a zero cannot establish that the engine never researches the subtopic.

Even within its own scope, Trends is relative rather than an absolute query count: Google normalises by time and geography, then scales the results. Low-volume terms can appear as zero, and statistical noise can produce apparent spikes, particularly at low or absent interest.[1] Those limitations reinforce the need to name the question before choosing the input.

## Accept one brief; reject the other

For a CMO commissioning question research, I would separate these deliverables before approving the work.

**Accept: relative Google search-interest context.** Ask for the terms or topics compared, selected period, geography and source. Use the result as one input to investigating buyer interest—not as a count of buyers or the engine's internal searches.

**Reject: a fan-out frequency estimate derived from Trends.** Renaming the chart “AI research demand” cannot supply the excluded population. Do not pay for a ranking of supposed internal queries whose only basis is their Trends values.

**Retain: a concrete buyer question that shows zero.** Keep it as a hypothesis, not a proven opportunity or a zero-demand verdict. If the decision is whether Google AI responses address that question, commission a bounded response review separately: specify the questions and surface, retain the actual responses and dates, and report only what was observed.

That proposed review is not a measurement performed here. Visible answers and supporting links would not, by themselves, reconstruct hidden fan-out or establish how frequently the market asks the question.

For ZSA, the commissioning instruction is narrow: use Trends to investigate relative interest within its documented scope; investigate answer behaviour through separately scoped observations. Do not let a chart that excludes internal AI searches decide that those searches never happen.

## Sources

[1] https://support.google.com/trends/answer/4365533?hl=en
[2] https://developers.google.com/search/docs/appearance/ai-features
