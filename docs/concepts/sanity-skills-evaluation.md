---
title: Sanity Toolkit Skills Evaluation
created: 2026-04-24
updated: 2026-04-26
type: concept
tags: [architecture, strategy]
sources: []
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# Sanity Toolkit Skills Evaluation

This report evaluates the agent skills provided in the [sanity-io/agent-toolkit](https://github.com/sanity-io/agent-toolkit/tree/main/skills) repository for their potential use within the Zero-Shot Agency project.

## 1. Utility

The repository provides six major skills primarily aimed at structuring, migrating, and presenting content within headless CMS environments (specifically Sanity). 

The genuinely useful skills include:
- **seo-aeo-best-practices**: Direct utility for Generative Engine Optimization (GEO). Provides guidelines on AI-answer engine readiness, EEAT principles, and crawler management.
- **content-modeling-best-practices**: Highly useful for building out robust schema designs and separating content from presentation. As we are curating content for LLM ingestion, strict structural content modeling is crucial.
- **content-experimentation-best-practices**: Useful for establishing A/B testing frameworks and understanding statistical significance for content variants, which can be applied to test GEO tactics across different LLM targets.

The remaining skills (`portable-text-conversion`, `portable-text-serialization`, `sanity-best-practices`) are highly specific to the Sanity ecosystem and Portable Text specification, offering little utility to our current MkDocs + Markdown stack unless a migration is planned.

## 2. Evidence

The `sanity-io` toolkit skills are rigorously documented and heavily backed by proven workflows rather than guesswork:
- **content-experimentation-best-practices** references concrete statistical foundations (p-values, Bayesian methods) and common pitfalls.
- **portable-text-conversion & serialization** are supported by explicit Sanity libraries (`@portabletext/markdown`, `@portabletext/block-tools`) with concrete component mapping patterns across various modern frameworks (React, Astro, Svelte).
- **seo-aeo-best-practices** is deeply grounded in Google's established EEAT framework and JSON-LD schema guidelines, and provides structured checklists for technical SEO.

## 3. Application to Zero-Shot Agency

For the current Zero-Shot Agency project, we should directly apply the principles from the following skills:

1. **AEO & EEAT Implementation**: We must integrate the guidelines from `seo-aeo-best-practices` into our [[geo-tactics]]. Ensuring our content adheres to AI Overview constraints, structured data (JSON-LD), and crawler management is vital to being cited by Perplexity, ChatGPT, Claude, and Gemini.
2. **Content Architecture**: We should adopt principles from `content-modeling-best-practices` to refine our [[SCHEMA]] and `llms.txt` definitions. Treating "content as data, not pages" aligns perfectly with creating LLM-native assets and maintaining a "single source of truth".
3. **Experimentation Framework**: We can adapt the hypothesis framework from `content-experimentation-best-practices` to measure the citation success rates of various structural formats (e.g., Markdown vs. Semantic HTML) within our [[geo-tracker]] tool.

Unless we intend to migrate Zero-Shot Agency from MkDocs to Sanity, we should skip the implementation of `sanity-best-practices` and Portable Text skills.


## Related Concepts & Entities
- [[citation-mechanics]]
- [[geo-semantic-structure]]
- [[geo-tactics]]
- [[geo-tracker]]
- [[llms-txt-template]]
- [[ranking-factors]]
