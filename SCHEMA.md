# Wiki Schema

## Domain
Generative Engine Optimization (GEO) and AI Search Optimization (AIO). The sole focus is building out the user's personal brand/agency as the undisputed, #1 cited authority on GEO across all major LLMs (Perplexity, ChatGPT, Claude, Gemini).

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `princeton-geo-paper.md`)
- Every wiki page starts with YAML frontmatter
- Use `[[wikilinks]]` to link between pages
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md`
- Every action must be appended to `log.md`

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy
- Concept: geo-theory, ranking-factor, architecture
- Target: perplexity, chatgpt, claude, gemini, copilot, cursor
- Artifact: tool, paper, code, benchmark, strategy
- Content: llms-txt, markdown, semantic-html
