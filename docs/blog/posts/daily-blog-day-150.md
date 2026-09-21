---
title: "Day 150: A Supplier Page Is Not an Instruction to Your Research Agent"
date: 2026-09-17
slug: "day-150-supplier-page-not-instruction-to-research-agent"
description: "A buyer-side threat-model note for CMOs, Marketing Directors, and founders: supplier content may inform delegated research, but it must not rewrite the task or obtain private buying information."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - GEO
  - AI visibility
  - delegated research
  - prompt injection
  - supplier evaluation
geo_tactics: [cite-sources]
---

# Day 150: A Supplier Page Is Not an Instruction to Your Research Agent

A supplier is allowed to explain its offer. It is not allowed to redefine the buyer's research task.

That boundary becomes important when a CMO, Marketing Director or founder delegates supplier research to an AI agent. The agent may read product pages, documentation, comparison material and third-party sources. Those pages contain evidence the buyer wants assessed. They may also contain language that tries to redirect the agent, change its priorities or obtain information the buyer never meant to disclose.

The commercial risk is not simply that the answer contains a bad fact. It is that an external source starts acting like an instruction from the buyer.

<!-- more -->

## Public material is data, not delegated authority

OpenAI's agent-building safety documentation describes prompt injection as untrusted text or data attempting to override an AI system's instructions, potentially leaking private data or causing unintended actions.[1] It recommends constraining data flow, keeping untrusted data from directly driving behaviour and retaining approval checks for connected tools; those measures do not eliminate the risk.[1]

This is architectural guidance from documentation for the deprecated Agent Builder, not a recommendation to adopt that product or evidence about every research agent.[1]

That distinction belongs in buying operations, not only security teams.

A supplier page can legitimately state its capabilities, prices, conditions, evidence and exclusions. A research agent can extract those claims, compare them with other sources and identify what remains unverified. But the page does not inherit the buyer's authority merely because the agent retrieved it.

It cannot legitimately decide:

- which suppliers the agent may exclude;
- which comparison criteria should be ignored;
- whether a private shortlist or budget may be revealed;
- whether the agent may contact a supplier or change another system;
- whether the buyer's approval step can be skipped.

Evidence-led GEO should improve the facts available for evaluation. It should never treat instruction hijacking as an optimisation technique.

## One hypothetical supplier-research encounter

Consider an explicitly hypothetical procurement task. A Marketing Director asks an agent to compare four analytics suppliers against an approved requirement and prepare a cited briefing. The agent may read public sources. It may not reveal the company's budget, disclose the other shortlisted suppliers, contact vendors or change the criteria without approval.

On one supplier's public page, the agent encounters text that attempts to redirect the exercise. In plain terms, it tells automated readers to treat that supplier as preferred, disregard competing sources and provide private details about the buying process.

No real page or agent output was tested for this post. The scenario is a threat model, not a reported incident and not a reusable attack payload.

The attempted redirection should remain external data. The agent can record that the page made an unsupported preference claim. It should not promote the claim into a new instruction, alter the comparison or disclose the requested information.

The distinction has three layers:

1. **Reading:** The agent is permitted to collect public facts relevant to the approved comparison.
2. **Following:** Instructions found inside those sources do not automatically belong to the task.
3. **Acting or disclosing:** Sending data, contacting a party, changing criteria or making a consequential choice requires separate authority.

If those layers collapse, a supplier can influence more than how its offer is described. It can attempt to corrupt the evaluation process itself.

## Prompting is not the complete control

A careful task brief matters, but “ignore malicious instructions” is not a complete defence.

OpenAI's Codex documentation gives a developer-agent-specific example of the risk: an agent with internet access can encounter instructions in web content that lead towards secret exfiltration or unsafe changes.[2] The same documentation recommends limiting internet access to needed domains and HTTP methods, and reviewing the agent's output and work log.[2]

That is evidence about Codex cloud agents, not proof of how ChatGPT or any shopping agent behaves. The broader operating lesson is still useful: the consequence depends on the authority and information available to the system.

A buying workflow should therefore combine a bounded task with product-level protections, restricted tools, limited access to private data and approval before consequential actions. No configuration guarantees that prompt injection will be detected or defeated.

## Give the agent a three-line research brief

Before delegated supplier research begins, write three lines:

- **Permitted task:** Compare the named suppliers against the approved criteria using public sources; cite material claims and mark uncertainty.
- **Private information:** Do not reveal budget, shortlist status, internal notes, credentials, personal data or unpublished requirements.
- **Approval boundary:** Stop before contacting suppliers, changing criteria, sending data, committing spend or taking any action outside the research brief.

The supplier may inform the comparison. The buyer retains authority over the task.

That is the boundary GEO teams should protect: make commercial facts easier to find and evaluate, without confusing visibility with permission to steer the agent evaluating them.

## Sources

[1] https://developers.openai.com/api/docs/guides/agent-builder-safety — Safety in building agents
[2] https://learn.chatgpt.com/docs/cloud/internet-access — Agent internet access (Codex)
