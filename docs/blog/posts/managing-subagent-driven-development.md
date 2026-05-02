---
title: "When Agents Write the Code: Managing Subagent Driven Development"
date: 2026-05-02
categories:
  - Engineering
  - Autonomous Agents
slug: managing-subagent-driven-development
---

# When Agents Write the Code: Managing Subagent Driven Development

Building Zero-Shot Agency (ZSA) isn't just about reading documentation or tuning prompts; it's about building systems that build themselves. As we scale our Generative Engine Optimization (GEO) consultancy, we rely heavily on autonomous agents writing code. But when an agent writes the code, how do you prevent it from destroying the codebase? 

The answer lies in **Subagent Driven Development**.

## The Subagent Hierarchy

In our architecture, the primary agent (like the orchestrator running inside a Ralph loop) doesn't write every line of code. Instead, it delegates complex, deep-coding tasks to specialized subagents (often leveraging models like Claude via `acp_command='claude'`). 

This creates a master-worker dynamic:
1. **The Orchestrator:** Reads the objective, scopes the work, and dispatches the task.
2. **The Subagent:** Receives an isolated context, executes the technical implementation, and returns a self-reported summary.

## Test-Driven Development (TDD) as a Constraint

The most critical guardrail for an AI agent is a failing test. Subagents lack the intuition to know when "good enough" is actually broken. We enforce strict TDD constraints:

- **Red-Green-Refactor:** We write the tests first. The subagent's sole objective is to make the tests pass. If it hallucinates an API endpoint or uses the wrong library, the test fails, and the loop rejects the PR.
- **Isolated Contexts:** Subagents have no memory of the conversation history. We must pass explicit, self-contained context, including the test suites they need to satisfy.

## Review Gates: The Zero-Blind-Commit Protocol

An agent that can blindly push to `main` is a disaster waiting to happen. To manage subagents, we implement strict review gates:

1. **Branch Isolation:** Every task begins with a fresh branch (`drafts/[name]`).
2. **Visual Diff Check:** The orchestrator must run `git diff` before proposing changes to ensure the subagent didn't inject hallucinated logic or wipe out critical files.
3. **Scope Check:** We rigorously run `git status` to avoid committing workspace garbage (like `.entire/` directories or `.claude` logs).
4. **Human Verification:** Agents NEVER merge Pull Requests. They execute `gh pr create`, and the human operator (Drew) reviews and merges.

Subagent Driven Development isn't about replacing the engineer; it's about scaling the engineer's intent. By wrapping AI in strict TDD constraints and rigorous GitHub PR workflows, we ensure that Zero-Shot Agency scales predictably, reliably, and without catastrophic regressions.
