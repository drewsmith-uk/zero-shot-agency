---
title: Subagent-Driven Development (SADD) SOP
created: 2026-05-02
updated: 2026-05-02
type: concept
tags: [concept, strategy]
geo_tactics: [fluency, authoritative-tone]
---

# Subagent-Driven Development (SADD) SOP

Subagent-Driven Development (SADD) is a methodology for parallelizing complex tasks across specialized autonomous AI agents with isolated context boundaries. This Standard Operating Procedure (SOP) formalizes how we spawn, review, and merge subagent work at Zero-Shot Agency.

## 1. When to Spawn Subagents

Subagents should be instantiated for tasks that are:
- **Highly Parallelizable:** Tasks with minimal shared state, such as researching different concepts simultaneously.
- **Deeply Specialized:** Tasks requiring extensive reasoning in an isolated domain (e.g., deep code refactoring, system architecture design).
- **Context Heavy:** Tasks that would flood the primary orchestrator's context window.

Do **NOT** use subagents for minor mechanical tasks, single file patches, or trivial tool usage. Use direct CLI tools or scripts.

## 2. Handling Context Boundaries

- **Strict Isolation:** Subagents have no memory of the overarching conversation. The orchestrator must provide absolute file paths, detailed error messages, and explicit constraints.
- **Verification over Trust:** Subagents self-report their completion. The orchestrator must manually verify side-effects (e.g., checking if a file was written, reading back its contents) before proceeding.
- **Timeboxing:** Avoid long-running subagents. If a task is durable, use the `cronjob` or `background` flags instead of `delegate_task`.

## 3. Subagent Review Processes

All subagent output must undergo a strict review process by the orchestrator:
- **The Visual Diff Check:** Run `git diff` against subagent changes. Look out for duplicate lines, unintended deletions, or malformed syntax.
- **The Scope Check:** Run `git status` to ensure untracked files or hidden agent directories (e.g., `.entire/`) haven't been picked up.
- **The Syntax Check:** Run native syntax validators on any code modified by the subagent (e.g., `python -m py_compile` or `bash -n`).

## 4. Git Branch Management

Zero-Shot Agency enforces strict Git protocols to maintain codebase integrity.

- **No Main Commits:** Never commit directly to the `main` branch.
- **Branching Convention:** Check out branches using the format `drafts/[name]` for content or `feature/[name]` for code (e.g., `drafts/issue-166-sadd-sop`).
- **PRs Only:** All subagent work must be merged via Pull Requests. The orchestrator or human loop script creates the PR.
- **Zero-Blind-Commit:** Agents must never execute `git commit` or push blindly. Stage exactly the files meant to be committed using `git add <specific_file_path>`. The Ralph loop script will handle the final commit and push.

## Related Links
- [[strategy]]
- [[geo-tactics]]
