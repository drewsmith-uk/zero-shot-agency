---
title: "The Princeton GEO Paper: What the Original Study Actually Found"
description: "A source-linked analysis of the original GEO study, including GEO-bench, the nine methods tested, the reported visibility gains and the paper's limitations."
created: 2026-04-22
updated: 2026-08-21
type: entity
tags: [paper, geo-theory]
sources: [raw/papers/princeton-geo-paper.md]
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# The Princeton GEO Paper: What the Original Study Actually Found

- **Full title:** GEO: Generative Engine Optimization
- **Authors:** Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande
- **Published:** Submitted to arXiv in November 2023, revised in June 2024, and published at KDD 2024
- **Link:** [arXiv:2311.09735 [cs.IR]](https://arxiv.org/abs/2311.09735)

The paper by researchers affiliated with Princeton University, IIT Delhi and independent research teams introduced **Generative Engine Optimization (GEO)** as a framework for measuring and improving how source content appears inside generated answers. It remains an important starting point for the field, but its results need to be read in the context of the systems, metrics and limitations the researchers actually tested.

## What the researchers tested

The researchers created **GEO-bench**, a benchmark containing 10,000 queries drawn from nine sources and spanning different domains, difficulty levels and query intents.

Their main experimental generative engine retrieved the top five Google results for a query and passed those sources to GPT-3.5 Turbo to produce a cited response. They sampled five responses for each condition to reduce random variation and also tested selected methods against Perplexity.ai as a deployed generative engine.

The paper measured visibility using **Position-Adjusted Word Count**, which combines how much source material appears with where it appears, and **Subjective Impression**, a model-evaluated score covering relevance, influence, uniqueness, prominence, amount of cited material, likelihood of a click and diversity.

These are experimental visibility metrics. They are not equivalent to organic traffic, revenue, conventional search rankings or a guaranteed citation rate across current AI products.

## The nine GEO methods

The study evaluated nine ways to modify source content:

1. **Authoritative:** make the writing more persuasive and authoritative.
2. **Statistics Addition:** add relevant quantitative evidence where available.
3. **Keyword Stuffing:** add more query-related keywords, following a traditional SEO tactic.
4. **Cite Sources:** add relevant citations to credible sources.
5. **Quotation Addition:** add relevant quotations from credible sources.
6. **Easy-to-Understand:** simplify the language.
7. **Fluency Optimization:** improve clarity and fluency.
8. **Unique Words:** add distinctive terminology.
9. **Technical Terms:** add relevant technical language.

## What the results showed

The strongest methods improved visibility substantially in the paper's controlled evaluation. Quotation Addition, Statistics Addition, Cite Sources and Fluency Optimization performed well across the reported metrics, while Keyword Stuffing did not. The best result was approximately **41% improvement in Position-Adjusted Word Count** and **28% improvement in Subjective Impression** relative to the unmodified baseline.

The result is often shortened to “GEO improves visibility by up to 40%.” That is directionally faithful to the abstract, but it should not be read as a universal uplift. Method performance varied by domain, query and measurement method. Combining methods could help, but the useful combination depended on the source and context.

## What the paper did not prove

The study did not establish that these tactics produce a 40% increase in clicks, leads, revenue or Google rankings. The authors explicitly state that they did not evaluate effects on conventional search rankings.

Other limits matter when applying the work now:

- The controlled engine used five Google results and GPT-3.5 Turbo, which is not the same as today's consumer answer interfaces.
- The deployed-system test covered Perplexity.ai, not every current model, account mode or search surface.
- Generative engines, retrieval layers and user queries change over time.
- GEO-bench labels were manually inspected but can still contain subjective interpretation or error.
- Larger context windows and different retrieval systems may change how source position affects visibility.

The paper therefore supports a testable set of hypotheses, not a permanent checklist or guaranteed ranking formula.

## What this means for GEO work now

The durable lesson is not to mechanically add statistics, quotations or technical terms to every page. Content changes need credible evidence, a clear fit with the query and testing against the actual surfaces that matter to the buyer.

For Google AI features, the paper should not be used to claim that `llms.txt`, special AI markup, arbitrary chunking or over-focused structured data are required visibility switches. Google's current guidance still points back to the core Search requirements for crawlability, indexability, usefulness and quality.

ZSA uses the paper as an evidence source within a broader measurement process: define commercially relevant questions, capture exact outputs and visible sources, label uncertainty, compare competitors and decide whether the real gap sits in content, technical access, public proof, positioning or the buyer route.

For a current diagnostic rather than a historical paper summary, read more about our [AI Visibility Baseline](../ai-visibility-baseline.md).

## Related Concepts & Entities

- [[citation-mechanics]]
- [[geo-tactics]]
- [[ranking-factors]]
