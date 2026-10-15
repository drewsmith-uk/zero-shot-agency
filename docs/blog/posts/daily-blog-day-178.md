---
title: "Day 178: The Supplier Exit Rehearsal"
date: 2026-10-15
slug: "day-178-supplier-exit-rehearsal"
description: "A proposed handover exercise for a lead-routing workflow: retain the records, rebuild the necessary behaviour and keep enquiries moving when the automation supplier changes."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - architecture
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 178: The Supplier Exit Rehearsal

At the next automation renewal, reserve a session for leaving.

Not a cancellation negotiation. A rehearsal in which someone other than the incumbent supplier takes over a small, working part of the business process. The commercial question is whether enquiries can keep moving when the supplier relationship ends.

For Zero-Shot Agency, this is a proposed acceptance requirement, not a handover we have delivered. The exercise below uses a hypothetical lead-routing workflow and synthetic records. No migration, response time or revenue outcome has been measured.

<!-- more -->

## Set the exercise boundary

Imagine a company whose supplier operates an enquiry workflow: receive a form submission, assign a sales owner, notify that person and retain the follow-up status. Unrecognised requests go to a coordinator.

For this rehearsal, the company wants a replacement operator to perform those functions in a separate, company-controlled destination. That might eventually mean another platform; it does not assume that any particular pair of products supports migration.

Keep live enquiries outside the exercise. Agree the essential fields, routing decisions and notification destinations in advance. Use test recipients, not prospective customers. Name the person who will take responsibility for the destination and the person who can authorise a later live switch.

The incumbent may prepare the handover and answer questions. The replacement operator should then run the agreed route without the incumbent performing its everyday steps. Record anything that still requires their intervention.

## Lay out what must travel

A download is one component, not the whole handover.

Airtable's documentation provides a useful concrete boundary: a grid-view CSV contains visible field values, while record comments and field descriptions are excluded. Exporting an entire base as one file is not supported; tables require separate CSVs, and attachment files need separate handling.[1] A spreadsheet of leads should not be assumed to contain the system that works on them.

For the hypothetical exercise, separate these items:

- **Records:** the agreed lead fields, current owner and follow-up status, with a mapping to destination fields. Identify anything required that the export omits.
- **Behaviour:** routing rules, fallback assignment, notification content and any model instructions or custom logic actually used. Distinguish reusable configuration from behaviour that must be rebuilt.
- **Access:** company-authorised accounts and permissions for the destination. Arrange fresh authorisation where needed; do not put passwords or tokens in a handover document.
- **Connections:** who controls the form, event subscriptions and receiving endpoints; who can redirect or disable them; and which integrations need replacing.

These are proposed requirements to negotiate, not assets every supplier must or can transfer. Unsupported export formats, restricted components and unavailable permissions are constraints to resolve before promising an exit.

## Run the destination, not just the import

Ask the replacement operator to load synthetic leads representing the agreed routes. Check that their owners and follow-up states retain their intended meaning.

Then submit fresh test enquiries through the proposed replacement entry point. Does each reach its intended owner? Does the coordinator receive the unrecognised request? Can the team record follow-up and recognise a failed notification?

Test existing records separately from new arrivals. Airtable, for example, says newly created automations do not automatically run on existing matching records; its automations comprise configured triggers and actions.[2] Imported rows and working future behaviour are different acceptance questions. This is not a claim about how an unspecified destination handles imports.

Before any live move, agree how to account for enquiries arriving during the switch and avoid both routes sending the same notification. Specify who reconciles unfinished follow-ups and what temporary manual handling is acceptable. Do not shut down the old route merely because the destination contains rows.

## Price the smallest usable exit

For this workflow, the minimum useful handover is the lead information, essential routing and a team able to continue follow-up. Recreating every dashboard or historical convenience is a separate purchase.

Ask for the preparation, destination configuration, operator training and supported transition to be priced explicitly. Include overlapping service charges where necessary. Compare that cost with the commercial exposure of leaving enquiries unanswered—not just administrative time saved.

Native configuration can remain sufficient. Requiring an exit does not justify building a portable custom platform around a simple routing job. If rebuilding is unavoidable, make its scope and dependencies visible before renewal.

This sits within ZSA's agentic-workflow work downstream of discovery, including answer-led discovery. It is not a GEO ranking or citation tactic, a legal switching entitlement or a guarantee of universal portability.

End the rehearsal with a bounded decision: ready for a planned transition, specific gaps to fund, or a dependency the business consciously retains. Staying can be sensible. Staying because nobody knows how to keep the enquiries moving is a different commercial position.

## Sources

[1] Airtable Support, “Getting started with Airtable views”: https://support.airtable.com/articles/5189551686-getting-started-with-airtable-views

[2] Airtable Support, “Getting started with Airtable automations”: https://support.airtable.com/docs/getting-started-with-airtable-automations
