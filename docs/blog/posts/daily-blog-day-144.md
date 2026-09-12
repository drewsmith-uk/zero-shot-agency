---
title: "Day 144: Decide What an AI Crawler May Do Before You Block It"
date: 2026-09-11
slug: "day-144-decide-what-ai-crawler-may-do-before-blocking"
description: "A purpose-specific access teardown for CMOs, Marketing Directors, and founders: separate search discovery, model training, prompt-time grounding, and user-requested retrieval before making an AI crawler decision."
categories:
  - Build in Public
  - Generative Engine Optimization
tags:
  - GEO
  - AI crawlers
  - robots.txt
  - content access
  - model training
geo_tactics:
  - "Define the business purpose behind each provider-specific access decision instead of treating every AI-labelled crawler as one category."
  - "Separate automated search discovery, model training, prompt-time grounding, and user-triggered retrieval using current first-party documentation for each provider."
  - "Record what a directive is documented to affect, what it does not affect, and which important access paths sit outside that control."
  - "Preserve ordinary security and consent boundaries: robots.txt manages compliant crawling preferences, not confidential-content protection or universal enforcement."
---

# Day 144: Decide What an AI Crawler May Do Before You Block It

“Block AI bots” sounds like one policy decision.

It can conceal several different business decisions:

- Should this page be eligible for automated search discovery?
- May its content be considered for model training?
- May it support prompt-time grounding in a provider's products?
- What happens when a user explicitly asks a product to visit it?

Those purposes are not interchangeable. Current first-party documentation from OpenAI and Google assigns different controls and semantics to some of them.[1][2][3]

A blanket allow or deny can therefore express a policy the business never meant to choose.

For CMOs, Marketing Directors, and founders, the question should come before the directive: **which use of this public content do we want to permit, restrict, or investigate?**

<!-- more -->

## One provider can document several access purposes

OpenAI's crawler documentation makes the split unusually explicit.[1]

`OAI-SearchBot` is used to surface websites in ChatGPT's search features. OpenAI says sites opted out of that crawler will not be shown in ChatGPT search answers, although they may still appear as navigational links.

`GPTBot` has a different stated purpose. It crawls content that may be used to train OpenAI's generative AI foundation models. OpenAI says disallowing it indicates that the site's content should not be used for that training purpose.

OpenAI documents a third route, `ChatGPT-User`, for certain actions initiated by users in ChatGPT and Custom GPTs. It is not an automatic web crawler and is not used to determine Search inclusion. Because a user initiates those visits, OpenAI says robots.txt rules may not apply.

That is not one “OpenAI access” switch. It is a documented separation between automatic search crawling, potential training use, and some user-triggered visits.

Google's controls draw a different boundary.

Google says `Googlebot` crawl preferences affect Google Search, including all Google Search features.[2] Its Search Central guidance says that, to be eligible as a supporting link in AI Overviews or AI Mode, a page must be indexed and eligible to appear in Search with a snippet. Eligibility does not guarantee crawling, indexing, serving, or inclusion.[3]

`Google-Extended` is a separate control token. Google says publishers can use it to manage whether content Google crawls may be used for training future Gemini models and for grounding in specified Gemini and Vertex AI experiences. Google also says this control does not affect inclusion or ranking in Google Search.[2]

The categories do not map perfectly between providers. Google-Extended covers documented training and grounding uses; OpenAI distinguishes its Search crawler, training crawler, and certain user-triggered visits. A policy copied from one provider's vocabulary cannot safely be treated as a universal AI policy.

## A training restriction is not automatically a discovery restriction

Consider a hypothetical B2B software company. This is an illustrative policy choice, not a configuration we have deployed or an observed result.

The company publishes product pages, technical guidance, and original research. It wants public pages to remain eligible for ordinary Google Search and ChatGPT search discovery. It also wants to restrict specified model-training uses while its legal, publishing, and commercial teams review the trade-off.

At the level of the two providers' current documentation, that intention is purpose-specific:

| Business intention | OpenAI's documented distinction | Google's documented distinction |
|---|---|---|
| Preserve automatic search discovery | Manage `OAI-SearchBot` for ChatGPT search | Manage `Googlebot` for Google Search, including its AI features |
| Restrict documented training use | Manage `GPTBot` | Manage `Google-Extended` |
| Understand other access paths | Review `ChatGPT-User`, whose user-initiated visits may not follow robots.txt | Note that Google-Extended also covers specified prompt-time grounding uses |

This table is a decision aid, not a ready-to-paste robots.txt file. Path scope, rule precedence, current product documentation, server controls, and the site's existing directives still need technical review.

For this fictional company, the OpenAI choice is clear enough to take to technical review: preserve the documented ChatGPT search path through `OAI-SearchBot` while using `GPTBot` to express its training restriction. The Google choice is not identical. Because `Google-Extended` groups future Gemini training with specified grounding in Gemini Apps and Vertex AI, the company defers that restriction until it decides whether losing those grounding uses is acceptable. It does not invent a training-only Google setting. Google states that the eventual `Google-Extended` choice would not affect inclusion or ranking in Google Search, including Search's own AI features.

None of these choices promises the desired outcome. Allowing the relevant search crawler only avoids that particular crawl restriction; it does not by itself make a page indexed, snippet-eligible, or eligible for a Google AI supporting link, and it does not guarantee retrieval, citation, recommendation, position, or traffic. Restricting a training crawler does not establish what happened to material collected previously, control another provider, or secure confidential information.

## Ask four questions before changing access

A useful access review can stay compact.

### 1. What content are we deciding about?

Separate public marketing pages, documentation, licensed material, customer-only resources, personal data, and confidential systems. Sensitive content should be protected with authentication and appropriate security controls, not entrusted to robots.txt.

### 2. What processing purpose concerns us?

Name the concern precisely: automatic discovery, Search inclusion, model training, prompt-time grounding, a user-requested fetch, or something else. “AI use” is too broad to produce an intentional rule.

### 3. Which provider's current control addresses it?

Use the provider's first-party documentation, exact token, stated affected products, and stated exceptions. Do not infer that a similarly named bot has the same purpose, or that one provider's control applies across the market.

### 4. What trade-off are we accepting?

Name the consequence of the exact control. In this example, the `GPTBot` restriction expresses the company's OpenAI training preference without restricting `OAI-SearchBot`; a future `Google-Extended` restriction would bundle named Gemini training and grounding uses while leaving Google Search inclusion and ranking unaffected. The company defers the second choice because it has not accepted the grounding consequence. The decision belongs to the teams accountable for content rights, security, discovery, and commercial reach—not to a generic “block AI” checklist.

## Robots.txt is a preference layer, not a security boundary

The distinction matters because robots.txt is often asked to do work it was not designed to do.

Google describes robots.txt as a way to manage crawler access, mainly to prevent request overload; it explicitly warns that it is not a mechanism for keeping a page out of Google.[4] OpenAI likewise documents crawler-specific preferences and notes a user-triggered case in which robots.txt may not apply.[1]

A compliant crawler directive is not authentication. It does not revoke access already granted elsewhere, settle licensing questions, stop copying by every actor, or protect a private document whose URL is exposed.

Keep confidential material behind real access controls. Treat crawler policy as one documented layer in a wider publishing and security decision.

## Write the purpose next to the rule

For our discovery work at Zero-Shot Agency, the proposed review question is now:

> Which documented processing purpose does this access decision permit or restrict, for which provider and content scope?

That is a proposed review discipline, not a claim that we have changed a live configuration, measured crawler behaviour, or established a universal legal standard.

For every decision, retain a short record:

- provider and exact control;
- content scope;
- intended processing purpose;
- documented effect and exceptions;
- business owner and review date.

The record prevents a technically valid directive from surviving after its commercial purpose has been forgotten. It also makes later review possible when provider documentation or product boundaries change.

Do not begin with “allow AI” or “block AI”.

Begin with the use you are deciding about. Then choose the narrowest documented control that expresses that decision without pretending it controls more than it does.

## Sources

[1] https://developers.openai.com/api/docs/bots — OpenAI, “Overview of OpenAI Crawlers”

[2] https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers — Google Crawling Infrastructure, “Google's common crawlers” (`Googlebot` and `Google-Extended` entries)

[3] https://developers.google.com/search/docs/appearance/ai-features — Google Search Central, “AI features and your website”

[4] https://developers.google.com/search/docs/crawling-indexing/robots/intro — Google Search Central, “Introduction to robots.txt”
