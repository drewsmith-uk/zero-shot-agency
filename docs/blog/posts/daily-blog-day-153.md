---
title: "Day 153: Before Calling It a GEO Experiment, Defend the Comparison"
date: 2026-09-20
slug: "day-153-defend-comparison-geo-experiment"
description: "A methods-referee note: leaving one service page unchanged does not establish a credible no-edit comparison when both services may encounter changed public material."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - GEO
  - measurement
  - causal inference
  - experimental design
  - AI visibility
geo_tactics:
  - "Define the allocation, intervention, observations, comparison and exposure assumptions before interpreting a GEO change causally."
  - "Treat an unchanged service page as a nominal comparison until the study explains whether responses for that service could use changed shared material."
  - "Use reserved questions to assess performance beyond the questions that shaped the work, not as an untreated causal control."
  - "Report before-and-after answer observations descriptively unless the causal comparison and its assumptions are defended."
---

# Day 153: Before Calling It a GEO Experiment, Defend the Comparison

Consider a hypothetical proposal. No agency study, answer-engine test or client result is being reported here.

The proposal calls itself a controlled GEO experiment. A company would revise an analytics-service page and a shared overview page, leave its advisory-service page unchanged, then compare recorded answers to questions about both services. If analytics visibility rises more, the proposal would attribute the difference to the edit.

The comparison has not yet earned that conclusion.

Leaving the advisory page unchanged does not establish that advisory answers were unaffected. If those answers consult the edited overview page, the nominal comparison may also be exposed to changed material. If they do not, that pathway may not matter. The study must state and investigate the exposure assumption rather than treating “we did not edit this page” as proof of no intervention.

CMOs, Marketing Directors and founders should ask whether the design supports the causal sentence beneath its chart.

<!-- more -->

## Unseen questions are not automatically untreated units

Reserved buyer questions can assess performance beyond the exact questions used to brief the work. They may reveal whether an improved explanation appears under adjacent wording, constraints or category language.

That is useful. It is not, by itself, a no-edit comparison.

A question can be unseen by the writing team while its answer is produced in an information environment containing the edited pages. Equally, we should not assume every question retrieves those pages. The holdout tells us that the question was withheld from the brief; it does not reveal which material influenced a response or what would have happened without the edit.

Call it a generalisation check when that is what the design supports. Do not promote it to causal evidence by renaming the question set “control”.

## Define the study before interpreting the chart

In this proposal, the allocation is by service line: analytics is labelled treated and advisory is labelled comparison. The intervention is a specified set of edits to the analytics and shared overview pages. The observations are recorded responses to service-specific questions under stated conditions.

Those definitions expose the unresolved issues. How was the allocation chosen? Which shared pages could responses for each service use? What evidence would make the comparison a defensible estimate of what would have happened without the edit? Repeating prompts creates more observations, but it does not turn them into independently randomised treatment units.

A standard simple comparison usually assumes that treatment allocated to one unit does not affect another unit's outcome. That assumption is often called no interference. It is not a law that makes causal inference impossible when units interact. Hudgens and Halloran show that researchers can instead define direct and indirect effects under an explicit interference structure and assignment design.[1]

The lesson is narrower: a GEO report using a simple treated-versus-untreated comparison must defend the allocation and exposure assumptions that make that contrast meaningful.

## Separate exposure risk from background change

Two problems can undermine the conclusion.

First, there is possible cross-unit exposure. If advisory responses use the changed overview page, the comparison may not represent an unaffected no-edit condition.

Second, platform and source conditions may change over time. That is another explanation for a before-and-after difference, not another form of spillover.

Google documents that its AI features can use query fan-out to issue multiple related searches and draw on a wider set of supporting sources. It also says indexing and serving are not guaranteed.[2] This makes source exposure a question to investigate; it does not prove that one edit affected another service, describe every answer engine, or reveal hidden retrieval.

## Run a methods-referee pass

Before accepting a causal interpretation, ask:

1. **Allocation:** What received the edit, what formed the comparison, and how were those units chosen?
2. **Intervention:** Which exact pages, claims or source records changed?
3. **Exposure:** Could comparison responses use changed shared material, and what evidence addresses that possibility?
4. **Observation:** Which response, surface, date, access context and visible sources were recorded?
5. **Alternative explanations:** Could time, platform or other source changes explain the difference?
6. **Claim:** Is the result descriptive, a generalisation check, or a causal estimate supported by the design?

Some settings may support causal estimation with specialist design and defensible assignment, comparison and exposure assumptions. This proposal has not established those conditions.

## Give descriptive evidence its proper job

A baseline can record displayed answers and visible sources under stated conditions. It can show whether an offer was represented clearly in the observations collected and whether performance differed across reserved questions. It cannot expose every retrieval step, establish that an edit caused a change, or prove buyer behaviour, conversion or revenue.

Before renewing or expanding GEO work, ask the supplier to state the intervention, comparison, exposure assumptions and alternative explanations. If those cannot be defended, keep the conclusion descriptive:

> We observed these answer changes under these recorded conditions. This design does not isolate the effect of the edit.

That sentence is not a retreat from measurement. It is the line between an observation and an experiment.

## Sources

[1] Hudgens, M. G., & Halloran, M. E. (2008). “Toward Causal Inference With Interference.” *Journal of the American Statistical Association*, 103(482), 832–842. https://www.treatment-effects.com/Hudgens-Halloran-2008.pdf

[2] Google Search Central. “Optimizing your website for generative AI features on Google Search.” https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
