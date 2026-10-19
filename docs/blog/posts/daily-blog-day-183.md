---
title: "Day 183: When Paying More to Cache Costs Less"
date: 2026-10-20
slug: "day-183-when-paying-more-to-cache-costs-less"
description: "A worked prompt-caching cost comparison: when five-minute retention, one-hour retention or no cache wins for the same repeated model-input prefix."
categories:
  - Build in Public
tags:
  - architecture
  - strategy
  - claude
geo_tactics:
  - cite-sources
  - fluency
---

# Day 183: When Paying More to Cache Costs Less

A cheaper cache read does not make the first request cheaper. Someone has to pay to write the cache before a later request can reuse it.

For a founder budgeting an agent-assisted commercial workflow, that distinction changes the retention decision. Substantial instructions or reference material might repeat across requests, but the interval between those requests determines whether paying extra to retain them makes economic sense.

Here is a worked cost model for Zero-Shot Agency, using Claude's published prompt-caching rules. It is arithmetic, not an API experiment, customer traffic trace or claim of savings we have delivered.

<!-- more -->

## Price one unchanged prefix

Use Claude Sonnet 4.6 on the Claude API as the reference regime. Its documented five-minute cache write costs 1.25 times normal input, a one-hour write costs twice normal input, and a cache read costs 0.1 times normal input.[1] Other models can have different read multipliers; this is not a universal provider comparison.

Define **one cost unit** as processing our entire unchanged prefix once at normal input price. The prefix is the reusable beginning of the prompt, not the answer. Assume it meets Sonnet 4.6's documented minimum of 1,024 tokens, with an explicit cache breakpoint at its end.[1]

We compare only that fixed prefix. Changing buyer details after it, generated output, tool calls, retrieval and operating costs sit outside the calculation. Prompt caching does not eliminate output generation.[1]

Start each schedule cold. There is no pre-warming, prefix change, configuration change or concurrent cold request. Assume each response finishes before the next request starts, and every eligible within-lifetime reuse hits.

## Put the requests on a clock

Claude measures cache lifetime from the **start** of the request that writes or reads the entry, not the end of its response. A hit refreshes that lifetime without another write charge.[1] The read itself still costs money.

The table gives request-start times in minutes from the first request. For modelling, assume entries beyond their lifetime are unavailable. Actual deletion is not instantaneous; do not budget on an expired entry remaining reusable.[1]

| Request starts | No cache | Five-minute cache | One-hour cache |
|---|---:|---:|---:|
| 0 only | 1.00 | 1.25 | 2.00 |
| 0, 2 | 2.00 | 1.35 | 2.10 |
| 0, 2, 4 | 3.00 | 1.45 | 2.20 |
| 0, 20 | 2.00 | 2.50 | 2.10 |
| 0, 20, 40 | 3.00 | 3.75 | 2.20 |
| 0, 90 | 2.00 | 2.50 | 4.00 |

These are calculated prefix costs, not measured bills.

At minutes 0, 2 and 4, the short cache costs **1.25 + 0.10 + 0.10 = 1.45**. Buying an hour adds nothing useful to this schedule: both caches receive the same reads, but the longer write costs more.

At minutes 0, 20 and 40, the short cache instead pays for three writes: **1.25 × 3 = 3.75**. The hour-long cache pays **2.00 + 0.10 + 0.10 = 2.20**, beating both repeated short writes and the uncached total of 3.00.

Now remove the third request. One hour costs **2.10**, less than two short writes but more than the **2.00** uncached counterfactual. “Better than the other cache” is not the same as “cheaper than no cache”.

## Count the reuses that repay the write

For one cold write followed entirely by successful reads, the prefix cost across **n requests** is:

- Five minutes: **1.25 + 0.10 × (n − 1)**.
- One hour: **2.00 + 0.10 × (n − 1)**.
- No cache: **n**.

On these assumptions, the short cache first beats no caching at two requests; the hour-long cache needs three. Expiry or a changed prefix can introduce another write and restart that repayment calculation. These charges are for writes and reads, not accumulating storage rent.[1]

For an operating budget, use the arrival pattern of requests sharing the eligible prefix—not total application traffic. Ask the implementation team to confirm exact prefix matching and the minimum length, then compare billed cache writes, reads and uncached input with the uncached counterfactual.[1]

Keep stable instructions before fresh buyer facts. Do not freeze outdated terms, pad prompts, mix tenants or delay urgent customer responses to manufacture reuse. If the useful requests arrive too far apart, neither cache may win on prefix cost.

The economic choice is the lifetime that earns back its write premium through genuine reuse. A longer memory is worth paying for only when the work returns soon enough, often enough.

## Sources

[1] https://platform.claude.com/docs/en/build-with-claude/prompt-caching — Claude prompt caching
