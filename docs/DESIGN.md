---
version: alpha
name: Zero-Shot Agency
description: Technical Brutalism meets Generative Engine Optimization. Monochromatic, high information density, structural.
colors:
  primary: "var(--md-default-fg-color)"
  background: "var(--md-default-bg-color)"
  surface: "var(--md-code-bg-color)"
  border: "var(--md-typeset-table-color)"
  accent: "var(--md-accent-fg-color)"
typography:
  heading:
    fontFamily: "var(--md-code-font-family)"
    textTransform: "uppercase"
    letterSpacing: "0.05em"
  body:
    fontFamily: "var(--md-text-font-family)"
components:
  panel:
    backgroundColor: "{colors.surface}"
    border: "1px solid {colors.border}"
  card-grid:
    display: "grid"
---

## Overview

Technical Brutalism. The site should feel like a terminal, an IDE, or an engineering whitepaper. Flat hierarchies, no drop shadows, structural borders, and high-contrast typography.

## Colors

We rely entirely on MkDocs Material native CSS variables to ensure automatic light/dark mode switching.

- **Primary:** `var(--md-default-fg-color)` (Black/White depending on mode).
- **Background:** `var(--md-default-bg-color)`.
- **Surface:** `var(--md-code-bg-color)`. Used for cards and panels.
- **Border:** `var(--md-typeset-table-color)`. Used for all 1px structural borders.
- **Accent:** `var(--md-accent-fg-color)`. The ZSA primary blue accent. Used sparingly for links and specific highlights like `.zsa-hero-accent`.

## Typography

- **Headings (H2/H3 for sections):** Should leverage the monospace code font (`var(--md-code-font-family)`), be uppercase, and have slight letter spacing (`0.05em`).
- **Body:** Clean sans-serif (`var(--md-text-font-family)`).

## Components

DO NOT invent custom CSS classes for layouts. Use the following native elements:

- **`.grid.cards`**: Native MkDocs Markdown extension for rendering responsive card grids. Use this for feature lists, knowledge base links, etc.
- **`.zsa-panel`**: A bordered, padded box with a distinct background (`var(--md-code-bg-color)`) used for major distinct sections (like the Hero copy).
- **`.zsa-section-title`**: Applied to H2 elements to enforce the monospace brutalist typography.

## Do's and Don'ts

- **DO** use semantic HTML5.
- **DO** use existing MkDocs classes and variables.
- **DON'T** use inline styles (`style="..."`).
- **DON'T** use `!important` in CSS.
- **DON'T** create double-layered borders (e.g., placing a card grid inside a bordered panel).
- **DON'T** invent new margins or padding values without human approval.
