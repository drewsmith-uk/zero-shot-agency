---
title: "Day 180: Not Every Filter Needs a Search Page"
date: 2026-10-17
slug: "day-180-not-every-filter-needs-search-page"
description: "A hypothetical catalogue route sketch separates useful shopping filters from worthwhile search destinations, using Google's guidance on faceted navigation."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - architecture
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 180: Not Every Filter Needs a Search Page

A customer wants to narrow the shelves. That does not mean the business needs to publish a search destination for every possible arrangement of them.

Colour, width, material, price and sort order can all help someone shop. Letting those choices generate crawlable combinations is a separate publishing decision—not an automatic benefit of having a useful interface.

For Zero-Shot Agency, the following is a proposed catalogue-planning approach, not a delivered optimisation or measured result. The seller, routes and buying situations are hypothetical.

<!-- more -->

## Draw the routes before multiplying them

Imagine an office-furniture seller planning its desk catalogue. A visitor can filter by width, finish and storage, then sort by price. The marketing team wants people to discover both the range and useful subsets of it.

I would sketch these routes before deciding which filter URLs search crawlers should encounter:

| Route | Job for the shopper | Proposed discovery role |
|---|---|---|
| Desks | Explore the overall range | Main category destination |
| Desks for small rooms | Start with a space constraint | Candidate dedicated destination |
| An individual desk | Inspect and buy a specific item | Product destination |
| Oak finish, selected width, lowest price first | Refine the current shopping session | Useful interface state; not automatically a search destination |

The distinction is not broad versus narrow. A narrow selection can be commercially valuable. The question is whether it deserves to be an entrance to the catalogue, rather than merely an adjustment after someone has arrived.

“Desks for small rooms” is only a candidate here. Before creating that destination, I would want a useful selection and a coherent way to help someone choose: dimensions, clearance considerations and the trade-off between work surface and floor space. Renaming a thin filter result would not supply those things.

Conversely, an oak-finish selection could deserve its own destination if finish is a meaningful starting point for this seller's customers. The sketch is not a universal ban on colour or material pages. It asks merchandising to make a choice instead of inheriting every combination the software can generate.

## Keep the controls without exposing every combination

Google's faceted-navigation guidance describes how parameter-based filters can generate very large URL spaces. Crawlers may need to fetch apparently new URLs before discovering that they offer little value; spending crawling on those URLs can slow discovery of useful ones.[1]

That is the engineering reason to separate shopping flexibility from crawlable inventory. It is not evidence that this hypothetical seller—or every small catalogue—has a crawl-budget problem.

Google's crawl-budget guide is aimed primarily at very large or rapidly changing sites and certain indexing backlogs. It explicitly says many sites do not need that advanced work.[2] A marketing director should not buy a dramatic crawl-efficiency programme merely because a shop has filters.

For the sketch, preserve the customer's ability to narrow and reorder the desk range. Keep the intended category, selected destination and product pages available for discovery. Then have the technical team choose how the remaining filter states behave, based on the platform and which URLs genuinely need potential indexing.

Google documents different approaches for facets that do and do not need potential indexing. It also says canonical links may reduce crawling over time, but are less effective for controlling this than its preferred approaches.[1] A canonical tag is not an instant stop-crawling switch.

Nor is robots.txt a removal instruction. It controls crawling; a blocked URL can still appear in Google Search.[3] Blocking access also prevents Google from reading a page-level instruction there. This sketch is not a recipe for removing existing pages or blocking every filtered category.

## Give the worthwhile entrances a chance

For GEO, the connection is specific to Google's Search system. To be eligible as a supporting link in AI Overviews or AI Mode, a page must be indexed and eligible for a Search snippet. There are no additional technical requirements.[4]

Crawling a page does not ensure indexing. Indexing does not promise a ranking or selection in an AI response. Reducing crawlable combinations does not guarantee that Google will redirect effort to the destinations marketing prefers.[2][4]

The commercial decision still matters without an uplift forecast. In this hypothetical catalogue, fund the entrances that help customers begin a useful buying journey, while retaining the filters that help them finish it.

The desk shopper should keep the controls. The business should choose which combinations become destinations.

## Sources

[1] Google Crawling Infrastructure, “Managing crawling of faceted navigation URLs”: https://developers.google.com/crawling/docs/faceted-navigation

[2] Google Crawling Infrastructure, “Optimize your crawl budget”: https://developers.google.com/crawling/docs/crawl-budget

[3] Google Search Central, “Introduction to robots.txt”: https://developers.google.com/search/docs/crawling-indexing/robots/intro

[4] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
