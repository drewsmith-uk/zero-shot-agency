---
title: "Day 133: Stop Ranking GEO Tactics Without Naming the Domain"
date: 2026-08-31
slug: "day-133-stop-ranking-geo-tactics-without-naming-domain"
description: "A practical experimental-design memo for CMOs, Marketing Directors, and founders: choose GEO interventions by buyer job, content class, source truth, and measured outcome rather than applying a universal tactic leaderboard."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - GEO
  - AI visibility
  - experimental design
  - content strategy
  - budget control
geo_tactics:
  - "Define the buyer job and content class before selecting a GEO intervention; a useful change for one page type may be irrelevant or harmful for another."
  - "Test one bounded intervention against a documented baseline and comparison or holdout, using a metric that matches the decision the team needs to make."
  - "Add quotations, statistics, citations, or technical language only when credible source truth exists and the addition improves usefulness for the intended reader."
  - "Keep platform claims bounded and preserve Google's core Search guidance without treating llms.txt, special AI markup, arbitrary chunking, or over-focused structured data as required visibility switches."
---

# Day 133: Stop Ranking GEO Tactics Without Naming the Domain

Ask a GEO supplier which tactic works best and you may get a neat leaderboard: add statistics, quote experts, cite more sources, improve fluency, use authoritative language, introduce technical terms.

The list sounds actionable. It is also missing the decision that makes any item useful.

Useful for which content class? Helping which buyer do what? Supported by which source truth? Tested against which question and metric?

A statistic can clarify a research page and distort a service page when the number does not describe the service. Technical language can help a specialist and hinder an executive reader. Fluency can improve a page, but smoother prose does not repair an unsupported claim.

For CMOs, Marketing Directors, and founders, this is a budget-control problem. A universal checklist encourages teams to apply the same edits across unlike pages, then mistake activity for learning. The better question is not, “Which GEO tactic ranks first?” It is, “Which bounded intervention deserves a test on this content class for this buyer job?”

<!-- more -->

## The original research did not produce a permanent leaderboard

The original *GEO: Generative Engine Optimization* study provides useful hypotheses, not a universal operating recipe.

Its researchers built GEO-bench with 10,000 queries across different domains, intents, and difficulty levels. Their main controlled setup retrieved five Google results and used GPT-3.5 Turbo to generate cited responses. They measured experimental visibility through Position-Adjusted Word Count and Subjective Impression, and ran limited deployed-system testing on Perplexity.ai.

The study found that interventions including relevant quotations, substantiated statistics, credible citations, and fluency improvements performed well in its reported evaluations. It also found variation by domain, query, method, and metric. Combinations did not create one context-free winner.

Those boundaries matter. The experiment did not test every current version, account state, market, retrieval layer, or interface across ChatGPT, Claude, Perplexity, Gemini, and Google AI features. Its visibility metrics are not traffic, leads, conventional rankings, attribution, conversion, or revenue.

The durable finding is not “apply the winning tactic everywhere”. Source-content interventions can affect measured visibility under defined conditions, and their usefulness varies with those conditions.

## Name the content domain before the intervention

“Domain” should be practical, not academic. It is the combination of content class, subject constraints, buyer job, and available source truth that governs what a responsible edit can do.

Consider two generalised content classes.

The first is a regulatory explainer for a procurement lead comparing obligations. Its buyer job is to understand what applies, what does not, and which primary authority supports the distinction. Relevant citations may improve the page because the claim already depends on external rules. A sourced statistic might be useful if it answers a real evaluation question and its scope and date remain visible. An unsourced “authoritative” rewrite would be dangerous because confidence cannot substitute for legal accuracy.

The second is an implementation guide for a technical evaluator deciding whether a product fits an existing stack. Relevant technical terms may make interfaces, dependencies, and constraints easier to assess. A quotation could be ornamental rather than useful. Adding a broad industry statistic may distract from the buyer’s actual question: what must connect, who owns the work, and where does compatibility stop?

This contrast does not establish that citations always win for regulatory pages or technical terms always win for implementation guides. It identifies different hypotheses. The appropriate intervention still depends on the exact question, available evidence, baseline content, and measured outcome.

That distinction prevents tactic theatre. The team decides where one change could make a particular page more useful without changing what the organisation can support.

## Start with the buyer job, not the edit menu

A bounded experiment begins with a decision the reader needs to make.

“Improve our AI visibility” is too broad. “Help a procurement lead distinguish mandatory controls from optional practice” is a buyer job. “Help a technical evaluator verify whether the integration supports their environment” is another.

Once the job is named, the team can inspect the content class and source truth.

Ask:

- What is the page meant to help the buyer understand, compare, verify, or exclude?
- What facts, primary sources, product records, research, or approved claims already exist?
- Which part of the current page makes that decision unnecessarily difficult?
- What single intervention could address that difficulty without inventing evidence or broadening the offer?
- Which observation would justify retaining the change, and which would make the team stop?

This order protects usefulness. Statistics are not decorations. Quotations are not authority tokens. Citations should connect a material claim to a credible source. Technical language belongs where it increases precision for the intended reader, not where it makes ordinary copy sound specialised. Fluency should reduce friction without sanding away qualifications.

If the supporting truth does not exist, the tactic is unavailable. The next action is research, product clarification, or no edit—not fabrication.

## Use one intervention so the result can teach you something

Teams often rewrite a page by adding sources, statistics, technical terms, new headings, stronger assertions, and cleaner prose at once. If the recorded result changes, no one knows which change mattered. If usefulness declines, the team cannot isolate the cause.

A better test changes one bounded variable.

Suppose a comparison page accurately describes two implementation routes but forces a technical evaluator to infer the dependency difference. The intervention could be one concise, verified compatibility table using the terminology already present in approved product documentation. Do not simultaneously add customer quotations, a market statistic, new positioning, and a redesigned offer.

Record the baseline before changing anything: question wording, date, market, access context, visible sources, page state, and selected metric. Use a comparable unchanged page, held-out question set, or time-bounded baseline. This will not eliminate every confounder, but it is more informative than an unrecorded before-and-after impression.

The metric must match the decision. If the hypothesis concerns whether a technical constraint is represented accurately, evaluate accuracy and decision usefulness—not merely mention count. If the hypothesis concerns source visibility in a defined experiment, use the stated visibility measure and keep it separate from commercial outcomes. A larger number is not automatically a better buyer experience.

## A compact GEO intervention brief

Before approving a rewrite, require the following eight fields:

| Field | Required decision |
|---|---|
| **Buyer job** | What must the intended reader understand, compare, verify, or decide? |
| **Content class** | What kind of page is being tested, and what constraints govern it? |
| **Baseline** | What does the current page and recorded observation show before the change? |
| **Bounded intervention** | What single change will be made, using which verified source truth? |
| **Metric** | What observation matches the hypothesis without being promoted into a business outcome? |
| **Comparison or holdout** | What remains unchanged so the result has a useful reference point? |
| **Claim limit** | What can the result support, and what can it not establish? |
| **Stop or retain decision** | What threshold or finding will cause the team to keep, revise, or reverse the intervention? |

The structure gives leadership a reason to fund one test and a reason not to scale it. A result earns retention only when the named metric improves without creating new errors or reducing reader usefulness; otherwise the team revises or reverses the change.

## Scale the learning only as far as the evidence travels

A successful intervention on one implementation guide does not make technical terminology the new site-wide standard. It supports a narrower conclusion: this change helped this content class, for this buyer job, under these conditions, against this comparison, using this metric.

The next test may extend the hypothesis to a genuinely similar page. It should not jump from a technical guide to a founder narrative, regulatory explainer, pricing page, or customer story merely because the tactic now carries a green label.

The same restraint applies across answer surfaces. Observations from a controlled setup or one deployed system do not establish identical behaviour in current ChatGPT, Claude, Perplexity, Gemini, or Google experiences. Retrieval, generation, visible sources, user context, and product behaviour can differ and change.

For Google AI features, the ordinary Search guidance still applies. Google points to core Search eligibility, usefulness, accessibility, and quality. It does not require `llms.txt`, special AI markup, arbitrary chunking, or over-focused structured data as visibility switches.

The commercial value of this discipline is not a guaranteed uplift. It is controlled allocation. Marketing can stop paying for universal checklists, stop adding unsupported evidence, and stop scaling an intervention beyond the content class that earned it.

Do not ask which GEO tactic is best in the abstract.

Name the buyer job. Name the content class. Verify the source truth. Choose one bounded intervention. Match the metric to the decision. Keep a comparison. Write the claim limit before seeing the result. Decide in advance what would make you stop.

Only then has a tactic earned the right to be tested—and only the test can tell you whether it deserves to travel.