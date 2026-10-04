---
title: "Day 168: Let Readers Use the Chart Without Seeing It"
date: 2026-10-05
slug: "day-168-let-readers-use-chart-without-seeing-it"
description: "An annotated research-chart commission: fund the visual, its short alternative and a complete text-and-data equivalent so readers can use the same information without relying on sight."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - benchmark
  - semantic-html
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 168: Let Readers Use the Chart Without Seeing It

The chart has a headline. The bars have labels. A reader using a screen reader encounters “Research findings”.

They have been told that research exists, but given none of it.

For a marketing director commissioning a benchmark report, the missing deliverable is substantial: a way to inspect the information without seeing the graphic. That belongs in the original research budget, alongside analysis, writing and visual design.

My proposed commissioning choice is to buy the chart and its complete text equivalent together. Below is a brief for one hypothetical graphic, not a delivered ZSA accessibility project or a tested publication.

<!-- more -->

## The research object everyone should receive

Imagine a report about barriers to adopting a workplace tool. Its illustrative chart shows the share of respondents selecting each barrier: integration difficulty, training time and purchase cost.

Every value below is invented solely to demonstrate the commission. There was no survey. Respondents in this fictional setup could select multiple barriers, so the categories are not parts of a whole.

The reader's job is to compare the barriers, retrieve an individual value and understand what the comparison means. Reading the headline alone cannot do all three.

W3C's Web Accessibility Initiative recommends a two-part text alternative for complex images: a short description identifying the image and a longer description representing its essential information. Its chart example includes scales, values, relationships and trends.[1] That gives this brief its structure.

## Deliverable: the visual comparison

**Commission:** a horizontal bar chart titled “Barriers to adopting a workplace tool — fictional illustration”. Label each barrier directly and show its percentage. Use a percentage axis starting at zero and ending at one hundred, with the same scale for every bar. State that multiple responses were allowed and that all figures are invented.

**Reader job:** compare the relative sizes visually, while retaining access to the precise values and the meaning of the measure.

Keep the chart. WAI notes that graphics can make information easier to understand, including for some people with cognitive and learning disabilities.[2] Providing a text equivalent should add another way to use the research, rather than remove the visual one.

## Deliverable: a short identification

**Proposed alternative text:**

> Bar chart comparing three adoption barriers in a fictional survey. Values and explanation appear under “Adoption barriers: full description”.

**Reader job:** identify the graphic and find its fuller equivalent without listening to the whole analysis inside an image label.

The named heading must actually exist in the published page. This is a proposed wording and destination, not an implemented link. “Research findings” would identify neither the subject nor the way to read it.

WAI explicitly describes identifying the location of an on-page long description in the alternative text.[1] The short alternative and the longer description work together.

## Adoption barriers: full description

**Proposed published text:**

> This fictional horizontal bar chart compares the percentage of respondents selecting each adoption barrier. Its axis runs from zero to one hundred percent. Integration difficulty is the most frequently selected barrier, training time is next, and purchase cost is least frequently selected. Multiple selections were allowed; these percentages do not divide respondents into exclusive groups. All values are invented for illustration.

| Barrier | Fictional respondents selecting it |
|---|---|
| Integration difficulty | 60% |
| Training time | 40% |
| Purchase cost | 20% |

**Reader job:** inspect the values and the relationship the bars communicate, without reconstructing the graphic from colour or position.

For this simple comparison, prose plus a properly structured table is the proposed equivalent. A more complex graphic might require explanations of connections, exceptions or other meaningful visual relationships. A data download alone should not be assumed to explain those.

The production brief should preserve table headers and navigable structure, and make this description available to everyone. WAI recommends broadly available long descriptions; it also warns that some association methods flatten structured content into continuous text.[1]

## Fund inclusion; keep the GEO claim bounded

This commission also aligns with Search guidance. Google says it uses alternative text alongside computer vision and page content to understand an image, and warns against stuffing alternatives with keywords.[3] Its AI-features guidance recommends making important content available in textual form, while retaining ordinary SEO foundations rather than special AI requirements.[4]

Those recommendations do not establish citation, ranking or conversion gains from this proposed chart treatment. No assistant's image-reading capability was tested here.

The commercial choice stands without that promise: budget for readers to obtain the research through more than one representation. Ask the supplier to deliver the visual, short identification and full equivalent as one publication unit, with accessibility evaluation included in the scope. This brief alone certifies no compliance.

The reader should get the comparison—not merely an announcement that a comparison is pictured.

## Sources

[1] W3C WAI, “Complex Images”: https://www.w3.org/WAI/tutorials/images/complex/

[2] W3C WAI, “Images Tutorial”: https://www.w3.org/WAI/tutorials/images/

[3] Google Search Central, “Google image SEO best practices”: https://developers.google.com/search/docs/appearance/google-images

[4] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
