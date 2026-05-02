---
title: Subagent-Driven Development (SADD) SOP
created: 2026-05-02
updated: 2026-05-02
type: concept
tags: [concept, architecture, strategy]
geo_tactics: [authoritative-tone, fluency]
citation_metadata:
  primary_source: "zero-shot-agency"
  empirical_confidence: "high"
sources: []
---

# Subagent-Driven Development (SADD) SOP

Subagent-Driven Development (SADD) is our formal methodology for scaling AI output. By spawning autonomous subagents to handle distinct tasks in isolated contexts, we accelerate engineering and creative workflows while minimizing context window pollution for the orchestrator agent.

## Core Principles

1. **Context Isolation**: Subagents operate in independent terminal sessions with zero memory of the parent conversation. They must be fed explicit, self-contained goals and context.
2. **Parallel Execution**: Where possible, subagents should be spawned concurrently (batch mode) to tackle independent workstreams.
3. **Orchestrator Oversight**: The parent agent acts as the orchestrator. It verifies the final output via external observation (e.g., `git status`, file reads) and never blindly trusts a subagent's self-reported success.

## When to Spawn Subagents

- **Deep Reasoning**: Complex debugging, log analysis, or algorithmic design.
- **Creative Drafting**: Writing long-form content, blog posts, or dense documentation.
- **Context-Heavy Isolation**: Exploring a tangential topic without poisoning the main agent's context window.
- **Parallel Tasks**: Running multiple research queries or scraping different sites simultaneously.

## Context Boundaries

Subagents cannot access the parent's memory. When delegating:
- Provide absolute file paths.
- Copy/paste relevant error messages or required constraints into the `context` field.
- Explicitly state the target language, tone, and formatting requirements.
- Specify the required output format (e.g., "Return a JSON array of findings").

## Review Processes

Because subagent summaries are self-reports and potentially hallucinatory:
1. **Verification**: The orchestrator must always verify side-effects (e.g., `git status` to see created files, `cat` to verify content, `gh` CLI to confirm PRs).
2. **Validation**: Test code changes via native tools (`pytest`, `bash -n`, etc.) before committing.
3. **Iteration**: If a subagent fails, the orchestrator should not simply retry with the same prompt. Provide corrected context or handle the task directly.

## Git Branch Management & Protocols

Subagents and orchestrators must strictly adhere to the [[Zero-Blind-Commit Protocol]]:

1. **No Pushing to Main**: All work must be committed to an isolated branch (e.g., `drafts/[feature-name]`).
2. **Pull Requests Only**: Branches are merged exclusively via Pull Requests using `gh pr create --fill` or with a specified `--body-file`.
3. **Stop at PR**: Agents MUST NEVER merge Pull Requests. Human operators merge after review.
4. **Specific Staging**: Use `git add <specific_file_path>` to avoid staging workspace garbage. Never run `git add .` or `git add -A`.

## Toolsets

Subagents can be equipped with specific toolsets based on their role:
- `['terminal', 'file']` for coding.
- `['web', 'browser']` for research and scraping.
- Inherit the parent's toolset by default.
