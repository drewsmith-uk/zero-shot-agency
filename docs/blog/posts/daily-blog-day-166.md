---
title: "Day 166: Keep Product Research Open When Stock Runs Out"
date: 2026-10-03
slug: "day-166-keep-product-research-open-when-stock-runs-out"
description: "A merchandising decision card for keeping useful product information available while choosing honestly between in-stock sales, temporary stockouts, future orders and retirement."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - GEO
  - ecommerce
  - product discovery
  - merchandising
  - Google Merchant Center
geo_tactics:
  - cite-sources
  - fluency
---

# Day 166: Keep Product Research Open When Stock Runs Out

Keep the specifications available when the shelf is empty.

A buyer researching a product may still need its dimensions, compatibility or care instructions before deciding whether to wait. Removing that information because checkout is unavailable makes a stock decision do the work of a publishing decision.

For a merchandising or marketing lead, the useful distinction is between the product someone can investigate and the transaction the shop can currently offer. A temporary stockout can close purchasing while leaving research open.

The practical choice is what to retain, what to stop selling and when to accept a future order.

<!-- more -->

## Choose the state before changing the page

Use this compact decision card for an explicitly hypothetical desk lamp. It describes alternative merchandising states, not a ZSA experiment, observed customer journey or measured result.

| Lamp's commercial state | Google's Merchant Center treatment | Useful page and buyer action |
|---|---|---|
| Available and orders can be fulfilled | `in_stock` | Show availability and enable purchase |
| Temporarily unavailable; no orders accepted | `out_of_stock` | Keep useful specifications accessible; clearly show the stockout and disable purchase |
| Unreleased; advance orders accepted | `preorder`, with `availability_date` | Explain the release state and expected shipping date before accepting an order |
| Previously released; unavailable now, but orders accepted for later shipment | `backorder`, with `availability_date` | Explain the wait and expected shipping date before accepting an order |
| Permanently retired from sale | Remove the discontinued product from Merchant Center product data | Decide separately whether the page still earns its place as a reference |

The Merchant Center column follows Google's availability guidance.[1] The page-retention choices are merchandising recommendations, not a promise that an unavailable product will appear in Shopping or an AI answer.

Google distinguishes preorder from backorder: preorder is for new products that have not been released. A familiar lamp awaiting replenishment belongs in the backorder category if the shop accepts orders. Calling every future shipment a preorder loses that distinction.

## Keep the research; choose the commitment

For the temporarily sold-out lamp, retain what helps someone evaluate it: measurements, materials, compatibility and the difference between variants. Put the stock status where the purchase decision happens. A restock-notification option, if offered, should be described as a notification request rather than an order or reservation.

That leaves the buyer with a useful choice: wait for news, compare an available alternative or continue researching. It does not require a speculative delivery date to keep the page worthwhile.

Accepting money for later delivery is a different choice. Google requires an availability date for preorder and backorder submissions, visible on the landing page, and says those pages must display the expected shipping date.[1] Where the date is an estimate, describe it as such. If there is no defensible shipping estimate, keeping orders closed is preferable to inventing one for the data field.

Retirement needs another decision. Google says to remove permanently discontinued products from product data rather than leave them marked out of stock.[1] That instruction concerns the commerce data source; it is not a blanket instruction to erase every corresponding web page. An archived lamp page could still explain care or compatibility, clearly labelled as retired. Keep it for that purpose, not as a disguised live offer.

## Give Google the same stock decision

Google requires availability to agree across product data, the landing page, checkout and structured data where present. A mismatch can lead to product disapproval. Variant availability must also match: one available finish does not make every lamp finish available.[1]

Before reopening sales, inspect the exact variant a buyer can select, the action checkout permits and the status submitted to Merchant Center. Conversely, use the appropriate destination or pause controls when the aim is to stop promotion of an available product; Google explicitly warns against using `out_of_stock` for that purpose.[1]

These are documented commerce requirements. They do not establish an instant stock refresh across answer engines.

## Preserve a useful destination, without promising selection

For Google's AI Overviews and AI Mode, a supporting page must be indexed and eligible for a Search snippet. Google gives no guarantee of indexing or serving, and requires no special AI markup.[2] Retaining a useful product page therefore preserves material people can consult; it does not secure an AI recommendation.

The merchandising brief can be simple: keep research useful through a temporary stockout, accept future orders only on stated terms, and retire obsolete offers deliberately. Decide what the customer can learn separately from what they can buy today.

## Sources

[1] Google Merchant Center Help, “Availability [availability]”: https://support.google.com/merchants/answer/6324448?hl=en

[2] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
