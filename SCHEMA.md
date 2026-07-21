# Wiki Schema

## Domain
Generative Engine Optimization (GEO) and AI Search Optimization (AIO). The sole focus is building out the user's personal brand/agency as the undisputed, #1 cited authority on GEO across all major LLMs (Perplexity, ChatGPT, Claude, Gemini).

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `princeton-geo-paper.md`)
- Every wiki page starts with YAML frontmatter
- Use [[wikilinks]] to link between pages
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md`
- `docs/logs/entries/` is a historical archive of the retired Ralph workflow. Do not add routine task logs there unless a new entry is explicitly requested for a durable incident or experiment record.

## Task Sources and Delivery Records
- Work may originate from an approved chat brief, the active sprint in `.hermes/sprints.md`, a Hermes Kanban task, or an explicitly scoped GitHub issue.
- GitHub issues are optional inputs and alerts, not a universal autonomous task queue. Automated monitors may open an issue for human triage, but agents must not automatically claim every open issue.
- Pull Requests are the canonical integration and review record for repository changes. PR descriptions must identify scope, verification evidence, and any relevant task or issue.
- Historical plans, logs, and issue descriptions provide context, not current truth. Verify them against maintained strategy, current task state, and the repository before acting.

## GitHub CLI and Pull Requests
- **AGENTS MUST NEVER MERGE PULL REQUESTS.** Only human operators are authorized to merge. Agents must stop after `gh pr create`.
- **Pull Request Bodies:** When using `gh pr create` with multiline bodies, NEVER use inline `--body "text\ntext"`. Bash does not parse `\n` in double quotes correctly. ALWAYS use a heredoc or `--body-file` to preserve real newlines. (e.g., `gh pr create --body-file pr_body.txt`)

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

## Blog Posts
- Blog Post Titles: MUST follow the exact format "Day X: [Subtitle]". NEVER use the phrase "Daily Collaboration Blog" in the `title:` frontmatter or the H1.
- All blog posts must be saved in `docs/blog/posts/` and contain a valid H1 (`# Day X: ...`).
- Ensure frontmatter contains the correct `date` and `categories` as required by the MkDocs blog plugin.

## Autonomous Agent Operational Protocol (Verify-Before-PR)
All AI agents (including Hermes and delegated subagents) MUST adhere to the **Zero-Blind-Commit Protocol** before executing `git commit` or opening a Pull Request. You may not rely on the human user as your compiler or linter.

1. **The Visual Diff Check:** Run `git diff` or `git diff --staged` to visually read the lines you are changing. Check for duplicate lines, unintended deletions, or malformed syntax.
2. **The Scope Check:** Run `git status` to ensure you haven't accidentally scooped up untracked workspace files, hidden agent directories (e.g., `.entire/`), or utility scripts.
3. **The Syntax Check:** Validate the code natively before pushing:
   - Python: `python3 -m py_compile script.py`
   - Bash: `bash -n script.sh`
