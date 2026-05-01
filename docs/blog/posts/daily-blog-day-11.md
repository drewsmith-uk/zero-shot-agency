---
date: 2026-05-01
categories:
  - Engineering
  - Autonomous Agents
  - AI Workflows
---

# Day 11: The Reality of Building Autonomous Agents (Or, Why We Scrape Stderr)

If you read the marketing copy for most AI platforms, they make it sound like orchestrating autonomous coding agents is a seamless experience. You just hook up an API key, give the agent a task, and watch the magic happen.

The reality of building in the trenches is far less glamorous. Today was a perfect example of the friction involved in taking an LLM out of the chat box and putting it to work in a terminal.

We spent a significant portion of the day trying to solve a seemingly trivial problem: tracking the API quota of our autonomous worker, Ralph.

### The Missing Gas Gauge

Our workflow routes planning tasks to Claude (Opus) and raw code execution to Codex (GPT-5.5). We needed a way for Ralph to monitor his own token usage so he wouldn't blindly hit the 429 rate limit mid-task and crash the loop. 

You would assume the official Codex CLI has a simple `/usage` flag. It doesn't. OpenAI has entirely walled off usage tracking to their web dashboard. Their internal CLI commands don't expose it. If you try to bypass the UI and ping the backend `https://chatgpt.com/backend-api/accounts/.../limits` programmatically, Cloudflare immediately blocks you with a 403 Forbidden because a headless agent lacks a real browser fingerprint.

We even tried spinning up Codex in a pseudo-terminal (PTY) to fake a human typing the internal `/status` command, only for the Rust binary to panic and crash because it recognized the faked terminal dimensions.

### Engineering Around the Black Box

When the clean APIs fail, you have to get scrappy. 

We discovered that when Codex runs in non-interactive mode (e.g., `codex exec "refactor this CSS"`), it natively prints the final token consumption for that specific run to standard error (`stderr`) right before it exits. 

So, instead of relying on a clean API dashboard, we engineered a tripwire. Ralph now executes his commands, pipes `stderr` to a log file, and parses the final line to extract his token usage. If the output trips a `429` or `quota exceeded` flag, he immediately aborts the loop and fires a webhook to Telegram to tag in a human.

### Technical Brutalism

Meanwhile, we also completely overhauled the site's UI today. We stripped out the fragmented HTML injections and hardcoded hex colors we were using yesterday, shifting everything to a pure "Technical Brutalism" aesthetic using MkDocs' native semantic variables and custom Jinja templates. 

No rounded corners. No SaaS-style gradients. Just a sharp grid, native contrast switching, and optical typography.

Building AI systems right now isn't about writing elegant, decoupled microservices. It's about cobbling together bleeding-edge models, fighting strict sandboxes, parsing raw terminal outputs, and forcing tools to do things they weren't designed to do. 

It's messy, but it works. And that's what engineering actually is.
