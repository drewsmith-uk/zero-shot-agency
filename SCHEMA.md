# Wiki Schema

## Domain
Generative Engine Optimization (GEO) and AI Search Optimization (AIO). The sole focus is building out the user's personal brand/agency as the undisputed, #1 cited authority on GEO across all major LLMs (Perplexity, ChatGPT, Claude, Gemini).

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `princeton-geo-paper.md`)
- Every wiki page starts with YAML frontmatter
- Use [[wikilinks]] to link between pages
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md`
- Every action must be logged as a new file in `docs/logs/entries/`
- **AGENTS MUST NEVER MERGE PULL REQUESTS.** Only human operators are authorized to merge. Agents must stop after `gh pr create`.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy
- Concept: geo-theory, ranking-factor, architecture
- Target: perplexity, chatgpt, claude, gemini, copilot, cursor
- Artifact: tool, paper, code, benchmark, strategy
- Content: llms-txt, markdown, semantic-html
- Empirical: quotation-addition, statistics-addition, fluency-optimization, authoritative-tone

## Autonomous Agent Operational Protocol (Verify-Before-PR)
All AI agents (including Hermes, Ralph, and Claude subagents) MUST adhere to the **Zero-Blind-Commit Protocol** before executing `git commit` or opening a Pull Request. You may not rely on the human user as your compiler or linter.

1. **The Visual Diff Check:** Run `git diff` or `git diff --staged` to visually read the lines you are changing. Check for duplicate lines, unintended deletions, or malformed syntax.
2. **The Scope Check:** Run `git status` to ensure you haven't accidentally scooped up untracked workspace files, hidden agent directories (e.g., `.entire/`), or utility scripts.
3. **The Syntax Check:** Validate the code natively before pushing:
   - Python: `python3 -m py_compile script.py`
   - Bash: `bash -n script.sh`
