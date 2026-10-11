---
title: "Day 174: Give Each Language Edition Its Own Address"
date: 2026-10-11
slug: "day-174-give-each-language-edition-own-address"
description: "A hypothetical bilingual reading path shows why a translated publication needs an address readers can open, share and revisit—not just a page that changes with the visitor."
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

# Day 174: Give Each Language Edition Its Own Address

A reader sends a colleague the French guide. The colleague opens the link and gets English.

The translation exists. The link simply did not carry the reader's choice with it.

That is the publishing problem I would put ahead of a language-selector demonstration. A marketing team funding translated content needs more than a screen that changes language. It needs editions people can open directly, pass to someone else and return to later.

The reading path below is hypothetical, not a ZSA implementation or an observed visitor journey. It sketches one English–French guide and the difference between selecting a language for a session and publishing a reachable edition.

<!-- more -->

## Follow the address, not the visitor

Imagine a company publishes a guide to choosing workshop lighting. Its first design uses one address, `/guide`, and changes the text according to a saved language preference. In this stipulated design, a reader can choose French, but copying the address does not preserve that choice. A colleague without the same preference receives the default English text.

Nothing here requires a bad translation. The failure is that the edition lives inside the visitor's settings rather than in the address being shared.

Now give the guide two stable destinations. These are illustrative paths on the same hypothetical site, not live pages:

- `/en/workshop-lighting/` opens the English edition.
- `/fr/eclairage-atelier/` opens the French edition.

The French reader copies the French address. Their colleague opens that edition without first reproducing the sender's browser settings. A bookmark leads back to the same language edition, although the publication itself may later be updated.

This is not a claim that a URL freezes a document in time. It preserves a route to the chosen edition.

## Let the reader cross between editions

Place a visible language choice on each page, linking to the corresponding guide—not merely the other language's homepage. Someone reading French can choose English without restarting their search through the site.

In this proposed design, the page respects the edition requested instead of forcing a different one based on presumed location or language. A recommendation to switch can remain an invitation.

Google's multilingual-site guidance recommends different URLs for language versions rather than changing a page's language through cookies or browser settings. It also advises against automatic language redirects, which can prevent users and search engines from viewing all versions, and suggests hyperlinks that let readers choose.[1]

The reader-facing benefit is concrete: the publisher offers a destination, not a guessing game about who arrived.

## Give Google the relationship as well as the pages

The same distinction matters for discovery. Google warns that it might not crawl, index or rank every variation of locale-adaptive content. Googlebot sends requests without an `Accept-Language` header; its default IP addresses appear US-based, although Google also crawls from other countries.[2] Do not assume the crawler will recreate every visitor setting needed to reveal an edition.

For the hypothetical guide, publish both pages and describe their relationship using Google's documented `hreflang` mechanism. This tells Google that they are localized alternatives. Google's guidance requires each language version to list itself and its alternates, with reciprocal references between versions.[3]

Those annotations are not the translation. Google says it determines page language algorithmically rather than from `hreflang`; its multilingual guidance points to visible page content.[1][3] Translating the navigation around an English article would not deliver the French guide promised in this sketch.

Nor does French mean France. A language edition can serve readers in several countries. Google's annotation format distinguishes a language from an optional region.[3] Publishing French text does not establish local delivery, support or commercial availability.

## Keep the investment on the publication

For GEO, the supported claim is narrow: this follows Google's documented approach to exposing language versions and describing their relationship. It does not establish how every answer engine discovers translations or promise that any edition will be recommended.

Google's AI Overviews and AI Mode require supporting pages to be indexed and eligible for a Search snippet. There is no special AI markup requirement, and meeting the requirements does not guarantee inclusion.[4]

The publishing choice still stands without an uplift forecast. For this guide, I would fund two complete reader editions with direct addresses and links between them, rather than accept a language toggle as the whole deliverable.

A translation should be somewhere the reader can go—not something the site shows only when it guesses correctly.

## Sources

[1] Google Search Central, “Managing multi-regional and multilingual sites”: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites

[2] Google Search Central, “How Google crawls locale-adaptive pages”: https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages

[3] Google Search Central, “Tell Google about localized versions of your page”: https://developers.google.com/search/docs/specialty/international/localized-versions

[4] Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
