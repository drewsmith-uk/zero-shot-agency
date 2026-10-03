---
title: "Day 167: Commission the Free Sample of Your Paid Publication"
date: 2026-10-04
slug: "day-167-commission-free-sample-paid-publication"
description: "A proposed lead-in experiment for a fictional specialist publication: let readers sample the editorial product while testing a sustainable subscription offer."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - GEO
  - subscription publishing
  - flexible sampling
  - content strategy
  - Google Search
geo_tactics:
  - cite-sources
  - fluency
---

# Day 167: Commission the Free Sample of Your Paid Publication

A specialist publication has to give a prospective subscriber something worth reading before asking them to pay for more.

How much should that first reading experience deliver?

Treat the answer as an editorial commission. Someone must choose the useful material a non-subscriber receives, the promise made at the paywall and the expense the publisher can sustain. Leaving those choices to a default subscription setting leaves part of the product undesigned.

For Day 167, here is a proposed experiment memo for a fictional industrial-energy publication. No publisher, subscriber behaviour or commercial result was observed. The proposal is to test a lead-in: a useful opening portion of each selected article, followed by paid access to the remainder.

<!-- more -->

## Commission: a useful opening, consistently offered

The fictional publication sells analysis to factory managers comparing energy investments. Its proposed pilot would cover one recurring analysis series for six weeks. That duration is an illustrative planning choice, not a recommended industry benchmark.

Each free opening would explain the investment question, identify the operating conditions under discussion and offer one complete editorial insight. The paid remainder would develop the comparison, assumptions and worked analysis. An editor would choose the boundary at a natural stopping point rather than cut every article after the same word count.

The reader should know before starting that the full analysis requires a subscription. At the boundary, show what remains, the subscription terms and a sign-in route for existing subscribers. Let someone leave with the opening they were offered; do not turn it into an unexpected registration demand halfway through.

This costs editorial time. The commission must budget for writing an opening that stands on its own without pretending to contain the whole answer.

## Why start with a lead-in?

Google's flexible-sampling guidance describes two approaches: metering gives readers a quota of articles before a subscription or login barrier; lead-in exposes a portion of an article without showing it in full. Google encourages cautious experimentation and says there is no single optimal sampling value across businesses.[1]

For this proposed series, choose lead-in because the editor wants every new reader to encounter the same kind of sample. It also makes the experiment's editorial question explicit: can a partial reading experience communicate enough value to justify subscribing?

A meter would let readers inspect complete analyses, potentially giving them a better understanding of the publication. That remains a credible alternative. The proposed lead-in deliberately sacrifices that fuller experience to retain the detailed analysis within the paid offer. Neither Google's examples nor this memo establish which would perform better for this publication.

## Brief discovery alongside the reading experience

The technical brief would ask for the selected articles, including their paid sections, to be eligible for Google indexing. Google's paywall guidance says Googlebot, and Googlebot-News where applicable, must be able to access content the publisher wants crawled and indexed. It describes paywall structured data that helps Google distinguish restricted content from cloaking.[2]

Reader access still needs its own enforcement. Google advises choosing an implementation that does not supply restricted content to the browser if it must not be accessible there.[2] Marking a passage as paid does not itself protect it.

Search previews need an explicit editorial choice too. Google documents `data-nosnippet` for excluding sections from snippets and `max-snippet` for limiting snippet length; its paywall guidance says AI Overviews and AI Mode are subject to Search preview controls.[2]

For those AI features, a supporting page must be indexed and eligible for a Search snippet. There is no special AI markup requirement, and serving is not guaranteed.[3] These Google-specific arrangements do not grant access to every AI crawler or promise subscription income.

## Review the offer before extending it

Before launch, the editor and commercial lead should agree a spending cap and minimum evidence needed to decide whether to continue. Use appropriately collected aggregate readership, paid starts, cancellations and reader feedback to assess the offer. Include the extra editorial work in its cost.

Pause early if the implementation exposes restricted material or denies subscribers their purchased access. At the planned review, stop expansion if the sample budget is exhausted or the evidence is too thin to justify extending the pilot. A handful of subscriptions would not, by itself, establish a durable improvement.

The unresolved trade-off is editorial: a generous opening may satisfy the reader without a purchase; a thin one may never communicate why the publication deserves payment.

Commission that choice deliberately. The free sample is part of what the publication makes.

## Sources

[1] Google Search Central, “Flexible Sampling general guidance”: https://developers.google.com/search/docs/appearance/flexible-sampling

[2] Google Search Central, “Structured data for subscription and paywalled content”: https://developers.google.com/search/docs/appearance/structured-data/paywalled-content

[3] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
