---
title: "Day 184: The Latest Payment Notification Can Be Old News"
date: 2026-10-21
slug: "day-184-latest-payment-notification-can-be-old-news"
description: "A worked delivery-order comparison shows why distinct invoice notifications need reconciliation before an agent-assisted workflow prepares a payment chase."
categories:
  - Build in Public
tags:
  - architecture
  - strategy
geo_tactics:
  - cite-sources
  - fluency
---

# Day 184: The Latest Payment Notification Can Be Old News

An invoice-created notification describes something that happened. It does not establish that the customer still owes payment when the notification arrives.

Stripe explicitly says it does not guarantee delivery in generation order. Its example includes receiving `invoice.paid` before `invoice.created`, with the API available to retrieve missing objects.[1] Both notifications can be genuine. Neither needs to be a duplicate for an arrival-driven workflow to make the wrong decision.

For a founder commissioning agent-assisted payment follow-up, that distinction belongs in the acceptance brief: should this input add to the history, or justify contacting the customer now?

<!-- more -->

## Hold the invoice still; reverse the deliveries

Here is a source-based counterexample, not a captured payment trace or a ZSA deployment. We consider only two distinct snapshot events for one invoice: `invoice.created`, followed in generation order by `invoice.paid`. Other events are outside the comparison.

Stipulate that payment has completed before either notification reaches our handler, and that the invoice remains paid throughout both cases. Each current-resource lookup succeeds and confirms that condition. These are modelling assumptions, not API responses we collected.

Compare two proposed designs:

- **Arrival-driven:** a created notification puts the invoice on a payment-follow-up list; a paid notification removes it. These are deliberately inadequate local rules, not Stripe behaviour. Creation alone does not establish an overdue debt.
- **Reconciled:** either notification prompts a check of the current invoice in the correct account. A confirmed paid invoice stays off the payment-chase list. The original event remains in the history.

| Delivery case | Notification being handled | Arrival-driven list action | Reconciled decision under the stipulated paid state |
|---|---|---|---|
| Generation order, first delivery | `invoice.created` | Add to follow-up | Do not queue a chase |
| Generation order, second delivery | `invoice.paid` | Remove from follow-up | Keep off chase list |
| Reverse order, first delivery | `invoice.paid` | Remove from follow-up | Keep off chase list |
| Reverse order, second delivery | `invoice.created` | Add to follow-up again | Keep off chase list; retain creation history |

The arrival-driven design ends with different instructions for the same paid invoice. Even the generation-order case briefly creates an inappropriate follow-up candidate. A later correction cannot retract a message already sent during that interval.

The reconciled design reaches the same no-chase decision at every step because the stipulated current condition is the same—not because it reconstructed a perfect event sequence.

## Keep history without turning it into a command

Stripe distinguishes snapshot handlers, which can read the object as it was at event time, from fetching the latest API resource. Thin notifications use a different handling model, retrieving the related object; they should not be treated as equivalent snapshot payloads.[1]

For this design, the historical record answers “what occurred?” The current invoice check answers a narrower operational question: “is a payment chase warranted now?” Recording creation remains correct after payment. Reopening collection merely because that record arrived late does not.

Nor can a uniqueness check settle the question. Stripe recommends tracking event IDs to recognise repeated deliveries. Our two events are distinct, so that check would admit both. Sorting snapshot `created` timestamps is no substitute: Stripe records them in seconds, warns that distinct events can share a timestamp, and explicitly says not to use them to determine event order.[1]

## Make reconciliation govern the customer action

My proposed rule is to prepare a chase only when the current invoice and applicable business terms establish that payment is due, follow-up is appropriate, and the workflow has permission. A failed lookup means unresolved—not unpaid. Conflicting information goes to an owner rather than becoming a confident customer message.

A current fetch is not a transaction lock across the billing system and the message sender. The implementation must coordinate concurrent handlers for the same invoice, prevent stale work overwriting a newer decision, and recheck eligibility before releasing a queued message. Those are design requirements, not guarantees supplied by this example.

The paid assumption is deliberately bounded. It does not settle refunds, disputes or other invoices, and it is not a universal instruction to ignore everything after payment.

Before accepting the workflow, ask the supplier to demonstrate generation-order, reverse-order and repeated deliveries separately, plus an unavailable current-state lookup. Inspect the resulting chase decisions and held work, not just successful delivery indicators. Stripe recommends acknowledging delivery before complex processing; that acknowledgement is not evidence that the business action is complete.[1]

Let the agent help compose an appropriate message. Do not let the last notification to arrive decide whether the customer deserves one.

## Sources

[1] Stripe, “Receive Stripe events in your webhook endpoint”: https://docs.stripe.com/webhooks?locale=en-GB
