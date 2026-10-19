---
title: "Day 182: An AI Overview Position Is Not a Citation Rank"
date: 2026-10-19
slug: "day-182-ai-overview-position-not-citation-rank"
description: "A source-based accounting schematic explains shared AI Overview positions, page-versus-property impressions and why overall Web metrics cannot establish first-cited performance."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 182: An AI Overview Position Is Not a Citation Rank

A source listed later inside an AI Overview can receive exactly the same Search Console position as a source listed before it.

Google assigns the position of the containing AI Overview to all its links.[1] The number therefore cannot tell a marketing director that their page was the first citation, the first brand mentioned or the preferred recommendation.

For Day 182, I am working through what that rule does to a performance report. This is an analysis of Google's documentation, not a Search Console account export or a captured search result. The distinction changes which claims a GEO report can make without changing any underlying performance.

<!-- more -->

## One result position, several links

Consider this accounting schematic. Stipulate one AI Overview at result position 2, containing links to two distinct canonical pages, A and B, in the same Search Console property. A appears twice. Assume all the illustrated links meet the applicable impression conditions, and that this property has no other result in this search.

Those are illustration conditions, not observations about Google's typical layouts.

```text
AI Overview: result position 2
    link to page A
    link to page B
    another link to page A

Page grouping:      A = 1 impression; position 2
                    B = 1 impression; position 2
Property grouping:      1 impression; position 2
```

The shared position follows Google's explicit AI Overview rule. The impression counts apply its documented aggregation rules: several links to the same page combine into one impression when grouping by page; grouping the containing element by property counts one impression for that property.[1]

The second placement of A does not create another page impression. B has its own page impression, but adding A and B does not reproduce the property total. These are different reporting scopes, not conflicting accounts of the search.

This is also why a table of page positions cannot reconstruct citation order. A and B both receive 2, even though the schematic lists A first. Neither has been assigned its ordinal place inside the answer.

## Establish the impression before using the position

The schematic's visibility assumption matters. Google says standard impression rules apply to AI Overviews. Those rules vary with the presentation: links inside independently scrolling or expanding elements typically need to be scrolled or expanded into view. A link's mere presence somewhere in the result's HTML is not sufficient grounds to count it.[1]

Google also requires an impression before recording a position. Do not assign every concealed supporting link a recorded position simply because the Overview has one.

Page identity matters too. Search Console generally assigns performance to Google's selected canonical URL, with some exceptions.[1] Two differently written URLs should not automatically become two separate page rows in your reconstruction. The schematic explicitly assumes A and B are distinct canonical pages to avoid that ambiguity.

## The report averages the topmost position

Even a correctly understood container position is not necessarily the position shown for your property across a reporting period.

Google describes the reported average as the topmost position occupied by a link to the property or page, averaged across the queries in which it appeared.[1] Other qualifying results and other searches can therefore affect it. An overall average position is neither a standalone blue-link rank nor an isolated measurement of the Overview's links.

For a performance review, I would use page grouping to examine which URLs received impressions, and property grouping to examine the site's aggregated appearance. Neither view, on its own, identifies those impressions as AI Overview impressions. I would remove a “first-cited” label derived from either position column rather than try to correct it with a different average.

## AI Mode introduces another query boundary

Do not carry the single-Overview-position rule across an entire AI Mode conversation.

Google says AI Mode follows Search's position methodology, including the rules for its carousel and image blocks. A follow-up question is treated as a new query; the new response's impressions, positions and clicks belong to that query. Clicking an external page counts as a click in both AI Mode and AI Overviews.[1]

A conversation is therefore not one fixed result container whose position persists through every answer.

Google includes these AI features in overall Search Console traffic under the Web search type.[2] Those aggregate figures alone cannot establish AI-only click-through rate, traffic contribution or a competitor citation league table.

The correction I would make to a GEO report is precise: retain the documented position metric, name its page or property scope, and withdraw the inferred citation rank. A shared coordinate tells you where the containing result sat. It does not tell you which source came first.

## Sources

[1] Google Search Console Help, “What are impressions, position, and clicks?”: https://support.google.com/webmasters/answer/7042828?hl=en

[2] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
