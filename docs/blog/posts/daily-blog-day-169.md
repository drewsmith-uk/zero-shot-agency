---
title: "Day 169: More Prompts Do Not Create More Treated Cases"
date: 2026-10-06
slug: "day-169-more-prompts-do-not-create-more-treated-cases"
description: "Two fictional GEO experiment sketches separate repeated answer captures from treatment replication, showing what a content-investment comparison must actually assign."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - benchmark
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 169: More Prompts Do Not Create More Treated Cases

A team rewrites one product guide, then asks an answer engine about it repeatedly. The report grows with every capture. The number of separately treated guides stays at one.

That distinction matters when a CMO asks whether to fund the same rewrite across a catalogue. More observations of one intervention are not more independently assigned cases of that intervention.

For Day 169, the design choice is where to spend an evaluation budget: deeper observation of one changed unit, or a comparison across separately assigned units. The two sketches below are fictional methodological planning—not an observed test, client case or validated ZSA method.

<!-- more -->

## Sketch one: observe one rewrite many times

Imagine a company adds a product-comparison section to one guide. Before and after publication, it repeatedly captures answers to a defined set of relevant buyer questions, recording whether the guide is cited. It samples different times and, separately, different engines.

The company has changed one guide. Each answer is an observation, not another guide receiving the change.

Those captures can describe citation frequency within the sampled questions and conditions, and reveal variation across runs. They cannot, by their number alone, establish that the rewrite caused a difference or would work across other guides. A before-and-after change could coincide with changes elsewhere, including the material available to the engine.

Penn State's repeated-measures guidance explains that multiple measurements of the same experimental unit cannot simply be assumed independent. It discusses models that accommodate their correlation, rather than discarding those measurements.[1]

Here the distinction is even more basic than choosing a statistical model: collecting another answer does not assign the content treatment again. Even independently generated answers about this guide would not turn it into several independently treated guides.

## Sketch two: assign the rewrite across comparable units

Now imagine the company can identify several comparable topic groups, each containing related product guides. For this sketch, the group—not each page or prompt—is the experimental unit: the entity assigned a treatment condition.

The proposed design randomly assigns each group to receive the comparison-section treatment or remain unchanged during the comparison. There would be multiple groups in each condition, with allocation specified before editing. NIST describes completely randomised designs as assigning factor levels randomly to experimental units.[2]

Outcome collection still uses buyer questions, engine-specific captures and repeated times. Those are sampling dimensions around each group. They do not multiply the number of assigned groups.

This creates treatment replication at a different level from sketch one. It also changes the work being purchased: the team must define comparable groups, deliver the same intended intervention consistently and preserve an untreated comparison—not merely collect more screenshots. Analysis would need to respect group assignment and the repeated observations within groups.

That is a design illustration, not a ready-to-run GEO experiment. No number of groups, captures or weeks is prescribed here; adequacy requires a separate design and power assessment.

## The boundary between groups must survive contact with the web

Topic labels alone cannot establish independence.

Two groups may draw on overlapping sources. Guides share a domain, internal links and possibly sitewide changes. A rewritten guide might influence answers classified under an untreated topic: that possibility is interference, where one unit's treatment affects another unit's outcome.

Google says AI Overviews and AI Mode may issue multiple related searches across subtopics and data sources when developing a response.[3] That makes a neat one-question-to-one-page mapping unsafe to assume. It does not prove that interference occurred in either fictional sketch.

Random assignment does not switch those connections off. Concurrent observation can help expose shared time trends, but does not guarantee that trends affect groups equally. Comparability, feasible randomisation and plausible separation must be examined before treating the groups as independent replications. A sitewide intervention may require a different assignment unit entirely.

If suitable units cannot be separated or the business cannot leave any unchanged, the proposed randomised comparison may be infeasible. A descriptive pilot can still be worthwhile; it should answer a narrower question rather than inherit a causal claim from the size of its report.

## Choose which uncertainty the budget should reduce

If the question is “How variable are the answers around this guide?”, repeated captures serve it directly.

If the question is “Does this content change improve citation outcomes across suitable guides?”, start with what can receive the treatment separately and what provides the comparison. Visibility would still not establish revenue return.

For the catalogue decision, ask the supplier to price those two jobs separately. Buy deeper observation when variability is the uncertainty. Investigate an assignable comparison when the investment depends on the intervention's effect. Do not buy the first and label it the second.

## Sources

[1] Penn State, STAT 502, “11 Introduction to Repeated Measures”: https://online.stat.psu.edu/stat502/Lesson11

[2] NIST/SEMATECH e-Handbook, “5.3.3.1. Completely randomized designs”: https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm

[3] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
