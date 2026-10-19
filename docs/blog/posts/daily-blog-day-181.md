---
title: "Day 181: Stars Do Not Travel with the Widget"
date: 2026-10-18
slug: "day-181-stars-do-not-travel-with-widget"
description: "A review-feature teardown: distinguish own-company testimonials, item-specific product reviews and Google Business Profile ratings before promising stars in Search."
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

# Day 181: Stars Do Not Travel with the Widget

A customer rating can be genuine, clearly displayed and still ineligible for the Google Search star feature the marketing team expects.

The missing ingredient is not necessarily more reviews or better code. It can be the relationship between the reviewed business and the page displaying the reviews.

For Day 181, I am separating three rating contexts that a single “add review stars” brief can conceal. This is a source-based teardown for Zero-Shot Agency, not an implementation report. The company and page briefs below are hypothetical; no live results, ratings or commercial outcomes were measured.

<!-- more -->

## One company, three different displays

Imagine Mere Lighting, a fictional lighting retailer with a showroom. It wants customer feedback on its own website and a clearer understanding of where ratings can appear in Google.

Its proposed pages share a visual motif: stars beside customer comments. That resemblance does not give them the same eligibility.

### Company page: reviews of Mere itself

**Page brief:** publish customers' accounts of the retailer's advice, delivery and service on Mere's own website. Embed the reviews through a third-party widget.

**Feature reading:** Google's review-snippet guidance says that when the reviewed entity controls reviews about itself, its pages using `LocalBusiness` or another `Organization` type are ineligible for the star review feature. Its explicit example includes reviews about a business on that business's website, whether placed directly in structured data or through an embedded third-party widget.[1]

The widget's external origin does not remove that restriction. Nor does the fact that real customers supplied the comments. This is a rule about the review's publishing context, not a finding that Mere's feedback is fabricated.

I would keep this page's purpose reader-facing: help someone understand what customers experienced when dealing with Mere. Specific accounts of advice or delivery can supply useful detail without a promised Search decoration. That is a proposed editorial use, not a measured conversion benefit.

### Product page: reviews of a particular lamp

**Page brief:** publish reviews collected from users about one named desk lamp, alongside that lamp's description. Keep the retailer's service feedback separate.

**Feature reading:** `Product` is among Google's supported reviewed-item types. The review guidance requires information about a specific item, not a category or list, and says marked-up review content must be readily available to users on the page.[1]

This creates a potential review-rich-result route, not automatic qualification. Required properties, the relevant feature policies and Google's general structured-data guidelines still apply. Google also says not to aggregate reviews or ratings from other websites.[1][2]

The product brief therefore cannot be fulfilled by copying Mere's company rating onto every lamp. A comment about helpful showroom staff does not become an assessment of a lamp's performance because the template labels it `Product`. Google's general rules require structured data to represent the page's content truthfully and prohibit misleading markup.[2]

The distinction is not “our website cannot have review markup”. It is that this lamp needs its own applicable review content and eligibility assessment. Even correctly marked-up content is not guaranteed a rich result.[2]

### Business Profile: ratings on Google's local surface

**Display brief:** understand the showroom's review score in Google Business Profile, separately from the company's own web pages.

Google's Business Profile guidance describes review scores for local places and businesses on Search and Maps. It defines the score as the average of ratings published on Google for that place or business.[4]

That is a separate context from adding review structured data to Mere's website. The own-company restriction above should not be read as an instruction that Google must suppress the showroom's Business Profile rating. Equally, seeing a rating there does not establish eligibility for stars beside Mere's own website result.[1][4]

## A Search snippet is not necessarily a review snippet

There is another distinction for a GEO brief. Google's AI Overviews and AI Mode require a supporting page to be indexed and eligible to appear in Search with a snippet; Google specifies no additional technical requirements or special schema for those AI features.[3]

That requirement is not a demand for a starred review rich result. Treating the two meanings of “snippet” as interchangeable would turn a feature-specific restriction into an unsupported claim about AI eligibility.

Nothing in these rules establishes that adding testimonials makes ChatGPT, Claude or Perplexity recommend Mere. They describe particular Google surfaces, not a universal rating-to-recommendation mechanism.

For Mere, the useful split is now clear: retain company testimony for readers, assess genuine lamp-specific reviews for the relevant rich-result route, and treat the Business Profile score separately. Do not attach one portable “Search stars included” promise to all three.

The stars may look alike. The feature belongs to the reviewed item and its publishing context—not to the widget.

## Sources

[1] https://developers.google.com/search/docs/appearance/structured-data/review-snippet
[2] https://developers.google.com/search/docs/appearance/structured-data/sd-policies
[3] https://developers.google.com/search/docs/appearance/ai-features
[4] https://support.google.com/business/answer/4801187?hl=en
