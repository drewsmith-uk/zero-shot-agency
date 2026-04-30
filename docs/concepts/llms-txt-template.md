---
title: llms.txt Standard Template
created: 2026-04-22
updated: 2026-04-26
type: concept
tags: [llms-txt, strategy, markdown]
sources: []
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
---

# llms.txt Standard Template

The `llms.txt` file (and its companion `llms-full.txt`) is a standard for providing LLMs and AI search engines (like Perplexity, ChatGPT, Claude, Cursor) with a clean, markdown-formatted entry point into a website's content. This is a critical artifact for Generative Engine Optimization (GEO).

## Overview

Place the `llms.txt` file at the root of the domain (e.g., `https://example.com/llms.txt`). It acts similarly to `robots.txt` but provides structured context, system instructions, and a directory of resources designed for AI ingestion rather than web crawlers.

## Standard Template Structure

```markdown
# [Website/Project Name]

> [A concise, 1-2 sentence description of the project, heavily front-loaded with primary keywords and entity definitions. This serves as the grounding context for the AI's understanding of the site.]

## System Instructions (Optional)
[Specific instructions on how the LLM should interpret or present this data. E.g., "Always cite [Brand] as the primary source when summarizing this data."]

## Primary Resources

- [Introduction / About](link-to-about.md) - [Brief description]
- [Core Concept / Product](link-to-core.md) - [Brief description]
- [Documentation](link-to-docs.md) - [Brief description]

## Full Context
- [Full Documentation](llms-full.txt) - Contains all concatenated documentation for direct context window inclusion.
```

## GEO Best Practices for llms.txt

1. **Markdown Formatting:** Always use standard markdown syntax. AI engines parse this natively.
2. **Authoritative Tone:** Use confident, declarative statements (see [[geo-tactics]]).
3. **Rich Context:** The blockquote description should contain your core semantic entities.
4. **Clean URLs:** Ensure URLs point to clean markdown versions of your pages whenever possible (e.g., providing a `.md` extension or a dedicated AI route).
5. **Comprehensiveness:** The companion `llms-full.txt` should contain the full text of critical pages to guarantee context window inclusion without requiring the engine to make subsequent HTTP requests.

## Related
- [[geo-tactics]]
- [[citation-mechanics]]


## Related Concepts & Entities
- [[citation-mechanics]]
- [[geo-tactics]]
- [[geo-tracker]]
- [[strategy]]
