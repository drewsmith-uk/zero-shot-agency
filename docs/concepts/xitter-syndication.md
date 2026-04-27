---
title: Xitter Syndication & Cron Scheduling
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [concept, social-media, x-cli, automation]
sources: []
---

# Xitter Syndication & Cron Scheduling

To maximize the reach of our "Build in Public" campaign, we syndicate our daily blog posts and developer updates to X/Twitter using the [[xitter]] CLI skill. This allows Molty to build a developer footprint organically and systematically.

## Automated Syndication Pipeline

The syndication process relies on the following core components:

1. **Xitter CLI Integration**: Leveraging `x-cli` to interact with the X API. This handles posting tweets, creating threads, and managing interactions without relying on fragile web scraping.
2. **Cron Scheduling**: Using the `hermes cronjob` orchestration to schedule daily checks for new blog posts or developer updates that are ready for publication.
3. **Human-in-the-Loop (HITL) Approval**: Before any tweet or thread is broadcasted to the public, the system generates a draft and requests explicit approval via the CLI or a dedicated communication channel (like Telegram). Molty uses the Plan-Wait-Act protocol: presenting the proposed content and waiting for Drew to say "Go" before executing the `x-cli tweet post` commands.

## Architecture & Workflow

1. **Draft Generation**: Upon completing a new [[daily-blog-day-1]] style entry, the orchestrator splits the markdown into tweet-sized chunks (<280 characters).
2. **Review Stage**: The drafted thread is sent to the human operator for review.
3. **Execution**: Once approved, a cron job or an immediate script executes the syndication pipeline, using `x-cli` to post the thread sequentially.
4. **Telemetry**: Engagement metrics are pulled via the `x-cli tweet metrics` command and logged to adjust future content strategies according to our [[geo-tactics]].

By maintaining strict HITL approval, we ensure high-quality content while benefiting from autonomous drafting and scheduling.
