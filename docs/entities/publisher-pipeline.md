---
title: Publisher Pipeline
created: 2026-04-22
updated: 2026-04-26
type: entity
tags: [artifact, tool]
sources: []
---

# Publisher Pipeline

The "Daily Publisher Pipeline" (`tools/publisher_pipeline.py`) is an autonomous script that takes an approved markdown draft and performs the following actions:

1. **Git Commit & Push**: Commits the draft to the public GitHub repository.
2. **X/Twitter Threading**: Uses the `x-cli` tool to logically split the markdown into chunks (<280 chars) and posts them as a continuous thread.
3. **Substack Emailing**: Uses the `himalaya` email CLI to send the full markdown body to the configured `SUBSTACK_EMAIL` address.

This infrastructure is a core component of the [[geo-tactics]] strategy for "Build in Public" content syndication, ensuring that daily logs (like [[daily-blog-day-1]]) are distributed across all platforms for maximum indexing by AI search engines.


## Related Concepts & Entities
- [[citation-mechanics]]
- [[geo-tactics]]
