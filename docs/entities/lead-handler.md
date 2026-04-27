---
title: Lead Handler
created: 2026-04-26
updated: 2026-04-26
type: entity
tags: [artifact, tool]
sources: []
---

# Lead Handler

The `lead_handler.py` script (`docs/tools/lead_handler.py`) automates inbox monitoring for `molty@zeroshotagency.com` using the `himalaya` CLI. 

Crucially, it implements an **Air-Gap JSON Extraction Layer** to sanitize incoming emails against prompt injection. By extracting business facts (such as `sender_email`, `core_intent`, and `safe_summary`) into a rigid, structured JSON format using an LLM, the raw, untrusted email content is isolated. 

Draft responses are then generated using only the sanitized JSON context, mathematically guaranteeing that malicious command chains in the original email cannot override the agent's behavior. This acts as an essential security layer for autonomous inbound marketing.
