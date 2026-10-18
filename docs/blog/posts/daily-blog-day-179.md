---
title: "Day 179: Give the Agent a Discount Mandate"
date: 2026-10-16
slug: "day-179-give-agent-discount-mandate"
description: "A source-based discount-policy teardown: separate API access from commercial authority, then check the exact concession an agent proposes before issuing it."
categories:
  - Build in Public
tags:
  - architecture
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 179: Give the Agent a Discount Mandate

“Offer a discount if it will help close the sale” leaves the agent deciding more than the wording of a reply.

Which customer qualifies? Which products? Can the concession combine with another promotion? When does it expire? A percentage ceiling answers only one part of that instruction.

For a founder delegating customer offers, the useful boundary is between preparing a concession and having authority to issue it. Shopify's discount API makes that distinction concrete: access to write discounts and the parameters of an individual discount sit in different places.

This is ZSA's proposed action-policy design, grounded in the documentation—not a deployed integration or a report of recovered margin.

<!-- more -->

## Read the permission and the proposed action separately

Shopify describes access scopes as controlling which store data an app can read and write. Its `discountCodeBasicCreate` operation requires `write_discounts` and creates a code-based percentage or fixed-amount discount.[1][2]

That requirement answers an access question. It does not express your company's decision that this customer may receive this concession on these goods. Nor does possessing a scope establish that every request will succeed; platform requirements still apply.

The operation accepts a separate discount input. Shopify documents buyer eligibility, qualifying items and value, start and end times, usage limits, minimum purchase requirements and permitted discount combinations.[3]

Those fields reveal why “the agent can discount” is an incomplete delegation. The business must decide what the agent may put into them.

## Translate the mandate into the offer's actual limits

I would define an owner-approved mandate outside the agent's conversation, then map it to the action being requested:

| Commercial decision | Documented input to examine | Proposed enforcement question |
|---|---|---|
| Who may receive the offer? | `context` | Does the selected buyer or audience fall within the authorised group? |
| What receives the reduction? | `customerGets` | Are the qualifying items and discount value within the mandate? |
| How long and how often? | `startsAt`, `endsAt`, `usageLimit`, `appliesOncePerCustomer` | Does the proposed availability and redemption exposure stay within the agreed limits? |
| What else may apply? | `combinesWith`, `minimumRequirement` | Are the combination rules and purchase conditions the business approved? |

The field descriptions are Shopify's; the enforcement questions are my proposed design.[3] Current input documentation uses `context` and marks `customerSelection` deprecated. An implementation should follow its chosen API version rather than copy an older example unquestioningly.

Crucially, an expiry, a redemption cap and once-per-customer use constrain different things. None substitutes for deciding which goods receive the reduction. Likewise, a maximum percentage cannot establish acceptable deal economics without knowing what that reduction applies to and what else the buyer receives.

## Route the proposal before creating the code

Under this design, the agent prepares structured offer parameters and a draft explanation. A separate execution service checks them against the stored mandate and trusted commercial data. The model's statement that it complied is not the check.

**Draft-only:** if the business has authorised preparation but not issuance, retain the proposal for approval. Do not create a redeemable code merely to give the reviewer something concrete to inspect.

**Bounded issue:** permit creation only when the actual buyer, items, value, timing, usage and combination settings satisfy the mandate. Any stipulated economic floor also needs a defined cost basis and current inputs. A missing cost must not become an assumed zero.

**Human exception:** hold a proposal that broadens the audience, includes excluded goods, permits unapproved combinations or cannot establish the required economics—even when its headline percentage is below the cap. The owner can approve a specific exception or decline it; the agent cannot expand its own mandate to finish the sale.

These are proposed routes, not Shopify features demonstrated here. To make them meaningful, the agent must not have another route to invoke the unrestricted write operation. The execution service should submit the checked parameters unchanged; a revised proposal needs another decision.

## Control the promise as well as the code

Shopify returns the created discount and a `userErrors` list describing execution errors.[2] An empty list is not evidence that your commercial owner approved the deal.

After creation, the proposed service should confirm the resulting settings before releasing the code. Customer-facing wording should come from those confirmed terms, not a fresh negotiation that adds free delivery or extends the expiry. Unresolved creation stays unresolved; the agent should not announce a usable offer.

The founder's decision is therefore specific: delegate preparation freely within its agreed scope, delegate issuance only inside an enforceable commercial mandate, and reserve exceptions for someone with authority to change the deal. Better persuasion should not quietly purchase a larger discount budget.

## Sources

[1] Shopify, “Shopify API access scopes”: https://shopify.dev/docs/api/usage/access-scopes

[2] Shopify, “discountCodeBasicCreate”: https://shopify.dev/docs/api/admin-graphql/latest/mutations/discountCodeBasicCreate

[3] Shopify, “DiscountCodeBasicInput”: https://shopify.dev/docs/api/admin-graphql/latest/input-objects/DiscountCodeBasicInput
