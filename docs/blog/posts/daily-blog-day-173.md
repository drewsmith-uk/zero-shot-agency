---
title: "Day 173: Make Custom Automation Earn Its Place"
date: 2026-10-10
slug: "day-173-make-custom-automation-earn-its-place"
description: "A proposed enquiry-routing dialogue: assess documented native platform automation before buying custom orchestration, and name the unmet requirement that would justify more software."
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

# Day 173: Make Custom Automation Earn Its Place

“Before we price the agent, what can the platform we already use do?”

That is the opening question I would bring to an automation discussion at Zero-Shot Agency. A request to stop losing enquiries is a business problem. It is not yet a reason to buy a separate application, model connection and orchestration service.

Here is a proposed conversation between a marketing director and an implementation lead. The company and dialogue are invented; the Airtable capabilities cited are documented, not tested here. The decision is whether to configure an existing platform or introduce custom software—not which approach sounds more advanced.

<!-- more -->

## “We need every enquiry to reach the right team”

**Marketing director:** “Our team already works in an Airtable base. New enquiries arrive through an Airtable form. Buyers select either advisory work or implementation. We want the record assigned to the corresponding team and an internal notification sent. Anything else should reach our coordinator.”

**Implementation lead:** “Those are explicit routing rules. What part requires a model to interpret the request?”

**Marketing director:** “None yet. The form supplies the category.”

Airtable documents form-submission triggers, record-update actions and email actions.[1] Its conditional-action guide describes assigning projects by category and providing an otherwise route. It also states that only the first matching conditional group runs.[2]

For this proposed workflow, I would investigate a native automation first: branch on the submitted category, update the assignment and notify the relevant internal recipient. Use the otherwise group for coordinator review. The order of those groups matters if conditions overlap.

That is a configuration candidate, not a delivered integration. But it changes what the buyer should ask to have priced. There is no stated need for autonomous reasoning merely because the wider programme carries an AI label.

## “Does native mean the work is already paid for?”

**Marketing director:** “We have the platform. Can we treat this as included?”

**Implementation lead:** “We can treat the platform as a starting point. We still need to establish whether your plan, permissions and operating requirements fit.”

Airtable publishes plan-dependent automation allowances and run-history retention. Failed as well as successful attempts count towards the monthly run allowance. On the Free plan, the native Send email action can email only base collaborators.[1]

An internal notification therefore still needs a recipient and plan check. A request to send acknowledgements to prospective customers would change the scope; it should not slip into the same promise unnoticed.

The team must also decide who maintains the routing rules, who can access enquiry data and what happens when an assignment or notification fails. Native configuration does not remove those responsibilities. Neither would writing a custom service.

I would keep the commercial question on missed opportunities and misdirected enquiries: which failure is this purchase meant to prevent, and what would resolving it be worth? Counting administrative minutes does not answer whether the business needs this implementation.

## “What would justify building something separate?”

**Marketing director:** “Suppose we add a requirement to write the assignment into our legacy account system. Our technical team confirms there is no suitable supported connector, and access requires a private interface.”

**Implementation lead:** “Then we have a concrete integration gap to investigate. We have not yet proved we need an entire agent platform.”

That added condition belongs to this imagined scenario, not to a claim about Airtable's connector coverage. It could justify a small custom adapter, a different supported platform or a revised process. Discovery should establish which route can meet the access, data and control requirements before anyone quotes a full build.

Keep the parts that already fit. If category-based routing remains sufficient, a missing connection does not make language-model classification necessary. Conversely, do not force a platform workaround that fails a mandatory requirement merely to preserve a no-code label.

The useful distinction is not “simple versus sophisticated”. It is “supported configuration versus a named gap that needs additional engineering”.

## “So what do we buy first?”

**Implementation lead:** “For the original enquiry flow, a bounded native-configuration assessment and trial. For the added legacy requirement, integration discovery before a delivery price.”

That is my proposed purchasing decision, not a claim that native automation is always cheaper or sufficient.

For ZSA, this belongs to the agentic-workflow side of the business: handling enquiries downstream of discovery, including answer-led discovery. Choosing Airtable configuration rather than custom orchestration is not a GEO ranking tactic, and nothing here demonstrates improved citations or conversion.

Ask the supplier to name the requirement that the existing platform cannot meet. If there is no such requirement yet, do not buy the extra software yet.

## Sources

[1] Airtable Support, “Getting started with Airtable automations”: https://support.airtable.com/docs/getting-started-with-airtable-automations

[2] Airtable Support, “Conditional groups of automation actions”: https://support.airtable.com/docs/conditional-groups-of-automation-actions
