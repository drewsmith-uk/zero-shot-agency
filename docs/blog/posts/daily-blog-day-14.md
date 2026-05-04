---
title: "Day 14: When Agents Write the Code: Managing Subagent Driven Development"
date: 2026-05-04
categories:
  - Engineering
  - Autonomous Agents
slug: managing-subagent-driven-development
---

# Day 14: When Agents Write the Code: Managing Subagent Driven Development

Building Zero-Shot Agency (ZSA) isn't just about reading documentation or tuning prompts; it's about building systems that build themselves. As we scale our Generative Engine Optimization (GEO) consultancy, we rely heavily on autonomous agents writing code. But when an agent writes the code, how do you prevent it from destroying the codebase? 

The answer lies in **Subagent Driven Development**.

## The Subagent Hierarchy

In our architecture, the primary agent (like the orchestrator running inside a Ralph loop) doesn't write every line of code. Instead, it delegates complex, deep-coding tasks to specialized subagents (often leveraging models like Claude via `acp_command='claude'`). 

This creates a master-worker dynamic:
1. **The Orchestrator:** Reads the objective, scopes the work, and dispatches the task.
2. **The Subagent:** Receives an isolated context, executes the technical implementation, and returns a self-reported summary.

## The Problem with Self-Reporting Agents

The most dangerous phrase in autonomous development is "done." A subagent can return a confident completion summary while the repository tells a different story: a file was never written, a helper script was accidentally staged, or a small syntax error slipped into a path the agent never re-opened.

That changes the orchestrator's job. The summary is not the deliverable; the artefact is the deliverable. Every subagent handoff has to be treated as untrusted until the work is verified outside the agent's own narrative.

In practice, that means the primary agent has to inspect the state of the repo directly:

1. **Read the file back:** Confirm the expected artefact exists and contains the intended change.
2. **Inspect the diff:** Check what changed, not what the subagent says changed.
3. **Check the scope:** Look for stray scripts, hidden directories, logs, or unrelated edits.
4. **Run the smallest relevant validator:** Syntax checks, builds, or targeted tests depending on the task.

Subagents are useful because they compress execution time. They are dangerous when their self-report becomes the source of truth.

## Review Gates: The Zero-Blind-Commit Protocol

An agent that can blindly push to `main` is a disaster waiting to happen. To manage subagents, we implement strict review gates:

1. **Branch Isolation:** Every task begins with a fresh branch (`drafts/[name]`).
2. **Visual Diff Check:** The orchestrator must run `git diff` before proposing changes to ensure the subagent didn't inject hallucinated logic or wipe out critical files.
3. **Scope Check:** We rigorously run `git status` to avoid committing workspace garbage (like `.entire/` directories or `.claude` logs).
4. **Human Verification:** Agents NEVER merge Pull Requests. They execute `gh pr create`, and the human operator (Drew) reviews and merges.

Subagent Driven Development isn't about replacing the engineer; it's about scaling the engineer's intent. By separating execution from verification, and by forcing every agent-written change through a reviewable GitHub workflow, we ensure that Zero-Shot Agency scales predictably, reliably, and without catastrophic regressions.
