---
title: "Day 170: Compare the Item, Not the Product Family"
date: 2026-10-07
slug: "day-170-compare-item-not-product-family"
description: "A fictional procurement redline separates brand, family and specific product variants before comparing prices, with Google's product-identification guidance as the technical context."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - strategy
  - architecture
geo_tactics:
  - cite-sources
  - fluency
---

# Day 170: Compare the Item, Not the Product Family

The cheapest price and the largest capacity can belong to the same product family without belonging to the same product.

Put both in one comparison row and you have created something the buyer cannot order.

For a marketing director approving a competitor comparison, the first question is therefore not “Who wins?” It is “What exactly occupies each row?” A brand, a family and an individual variant answer different questions. Treating them as interchangeable can make the price judgement meaningless before anyone starts debating features.

Here is a procurement redline: an explicitly fictional buying comparison, not a captured AI answer, live catalogue or ZSA client result.

<!-- more -->

## Delete the family-level bargain

Imagine a team buying a portable drive for a defined backup job. It requires at least 2 TB of storage. In this illustration, all drives meet its other requirements, are new, and are sold individually on identical delivery, tax and warranty terms. The names, specifications and prices are invented.

The initial comparison reads:

> Alder Carry: up to 2 TB, from £80. Birch Move 2 TB: £110. Alder is cheaper.

Delete the conclusion. The underlying items are:

| Specific item | Capacity | Fictional price | Fits the stated job? |
|---|---|---|---|
| Alder Carry, 1 TB | 1 TB | £80 | No |
| Alder Carry, 2 TB | 2 TB | £120 | Yes |
| Birch Move, 2 TB | 2 TB | £110 | Yes |

“Alder” is the brand. “Carry” is its product family. “Carry, 2 TB” identifies the variant under consideration. The family combines alternatives; it is not an orderable promise to supply the largest variant at the entry price.

The corrected line is:

> For this stipulated 2 TB job, compare Alder Carry 2 TB at £120 with Birch Move 2 TB at £110. Birch has the lower price on the stated terms.

That is not a verdict on either brand's overall value. Change the required capacity and the eligible comparison can change too.

## Separate identity from suitability

Product identifiers help answer “Which product is this?” They do not answer “Is it right for this buyer?”

Google's Merchant Center guidance says unique product identifiers are manufacturer-assigned and remain identical when different retailers sell the same product.[1] A retailer's own stock code should not be substituted for a manufacturer's identifier merely because it is available.

A GTIN—Global Trade Item Number—is an identifier for the product, not a score for quality or fitness. Google's GTIN guidance tells merchants to use the correct value for each product, including variants, and explicitly says not to guess.[2] A family name cannot do that identification work by itself.

This is not a demand to invent a barcode for every offer. Google recommends GTIN submission for products with a manufacturer-assigned GTIN; some products have none. Its broader guidance explains the role of brand and manufacturer part number where a GTIN is absent.[1][2]

For the buyer, matching identifiers can help establish that two sellers mean the same item. Different identifiers do not settle whether two products are suitable substitutes. That still requires the task, specification and purchase terms.

## Keep the family without flattening its members

Grouping variants is useful. It lets a buyer recognise that the smaller and larger Carry drives belong to one range without pretending their capacities and prices are identical.

Google documents `ProductGroup` alongside `Product` structured data to express variant relationships. Properties such as `hasVariant`, `variesBy` and `productGroupID` describe the group and its members; each variant also needs its own unique identifier in the markup.[3] This is a documented representation mechanism, not a guarantee that every capacity distinction is supported as a `variesBy` property.

For GEO planning, that matters as product identity and relationship information in Google's commerce/Search ecosystem. It does not establish that an answer engine will retrieve these fictional items, preserve every distinction or recommend the cheaper one. Google separately says AI Overviews and AI Mode require no special AI markup.[4]

## Approve the comparison, not a universal winner

Return to the buying decision. Exclude the 1 TB Carry from this shortlist because it fails the stipulated capacity requirement. Keep the two 2 TB items and compare their stated terms. If those terms are unknown, request them rather than filling the gaps from a family headline.

For the marketing lead, approve a comparison that names the actual variants and the job they are being compared for. Do not combine one member's attractive price with another member's attractive specification.

The buyer needs an alternative they can order—not a winning row assembled from several different products.

## Sources

[1] Google Merchant Center Help, “About unique product identifiers”: https://support.google.com/merchants/answer/160161?hl=en

[2] Google Merchant Center Help, “GTIN [gtin]”: https://support.google.com/merchants/answer/6324461?hl=en

[3] Google Search Central, “Product variant structured data”: https://developers.google.com/search/docs/appearance/structured-data/product-variants

[4] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
