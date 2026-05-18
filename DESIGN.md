---
version: alpha
name: Zero-Shot Agency
description: Technical Brutalism for an AI-native GEO agency. Structural, evidence-dense, monochrome-first, and built on MkDocs Material primitives.
colors:
  primary: "#111111"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  border: "#D0D0D0"
  accent: "#3366FF"
  inverse: "#FFFFFF"
typography:
  heading:
    fontFamily: "var(--md-code-font-family)"
    fontSize: 1.6rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.05em"
  body:
    fontFamily: "var(--md-text-font-family)"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "var(--md-code-font-family)"
    fontSize: 0.78rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.08em"
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
rounded:
  none: 0px
  sm: 2px
  md: 4px
components:
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.inverse}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  accent-marker:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.inverse}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  structural-rule:
    backgroundColor: "{colors.border}"
    rounded: "{rounded.none}"
    height: 1px
---

## Overview

Zero-Shot Agency uses **Technical Brutalism**: the site should feel closer to a terminal, IDE, diagnostic console, or engineering whitepaper than a generic SaaS landing page. The visual system exists to support evidence, trust, scanability, and conversion after an AI answer cites the site.

The default look is structural and information-dense: flat surfaces, crisp borders, strong hierarchy, restrained accent color, and minimal ornament. When an agent is uncertain, it should choose the simpler, more native MkDocs pattern.

This file controls visual and layout decisions. Content strategy, editorial angle, pricing, GEO methodology, and offer validation rules belong in the ZSA strategy docs and agent skills, not in DESIGN.md.

## Colors

The YAML color tokens above use representative hex values so DESIGN.md tools can parse and lint the file. **Implementation must prefer MkDocs Material CSS variables** so light and dark mode continue to work.

Use this mapping in ZSA code:

- **Primary text:** `var(--md-default-fg-color)`.
- **Background:** `var(--md-default-bg-color)`.
- **Surface / panel fill:** `var(--md-code-bg-color)`.
- **Border:** `var(--md-typeset-table-color)`.
- **Accent:** `var(--md-accent-fg-color)`, used sparingly for links, specific highlights, and rare high-emphasis markers.

Rules:

- Do not hardcode the representative hex values in site CSS unless a human explicitly approves it.
- Do not introduce new brand colors, gradients, or decorative color ramps.
- Use accent color as a signal, not decoration.
- Check any foreground/background pair in both light and dark mode.

## Typography

- **Section headings:** use `var(--md-code-font-family)`, uppercase styling, and slight letter spacing. This creates the technical/diagnostic feel.
- **Body text:** use `var(--md-text-font-family)` and preserve comfortable line height for high-density reading.
- **Labels / eyebrow text:** use monospace, small size, uppercase, and wider letter spacing.
- **Code and evidence:** preserve MkDocs Material's native code styling. Do not restyle code blocks into decorative cards.

Avoid:

- Decorative display fonts.
- Large marketing-style gradient headlines.
- Excessive centered text blocks.
- All-caps body copy.

## Layout

Use Markdown-native MkDocs structures first. Keep pages scannable and modular, but avoid decorative section stacking.

Preferred layout primitives:

- Native headings and paragraphs.
- MkDocs Material card grids using `{ .grid .cards }`.
- MkDocs admonitions when the content is genuinely a note, warning, tip, or example.
- Existing ZSA classes only where already supported by CSS, especially `.zsa-panel` and `.zsa-section-title`.

Spacing rules:

- Use existing MkDocs spacing and existing ZSA classes.
- Do not invent one-off margins or padding values.
- Do not stack bordered components inside other bordered components.
- Prefer one strong structural boundary over several nested boundaries.

## Elevation & Depth

ZSA is flat by default.

- Use 1px structural borders for separation.
- Use surface color differences for hierarchy.
- Avoid drop shadows, glow, glassmorphism, neumorphism, floating blobs, and depth effects.
- If hierarchy is unclear, improve heading structure or spacing before adding decoration.

## Shapes

- Corners are square or nearly square.
- Use `0px`, `2px`, or at most `4px` radius.
- Avoid pill-heavy SaaS styling except for small labels or native MkDocs components that already use it.
- Do not introduce organic shapes, waves, decorative blobs, or skewed section separators.

## Components

### Approved primitives

- **`.grid.cards` / `{ .grid .cards }`:** use for feature lists, service cards, resource lists, and related links.
- **`.zsa-panel`:** use for major proof blocks, hero copy, diagnostics, or sections that need clear separation from surrounding prose.
- **`.zsa-section-title`:** use for H2/H3 headings that need the brutalist monospace section treatment.
- **MkDocs admonitions:** use for actual notes, warnings, examples, or operational caveats.
- **Native Markdown tables:** use only when comparison data needs rows/columns. Keep them compact.
- **Accent markers:** use only for rare high-emphasis labels or status markers. Do not turn the accent into a broad color theme.
- **Structural rules:** use border-colored separators only when native headings, panels, or whitespace are insufficient.

### Card-grid example

Use Markdown attribute-list syntax. Do not wrap card grids in raw HTML.

```md
- **AI Visibility Baseline**

  Find where your brand appears, disappears, and gets misrepresented in AI answers.

- **GEO Content System**

  Build evidence-dense pages that retrieval systems can cite and humans can trust.

- **Agent Workflow Audit**

  Identify where autonomous workflows need approval gates, artefact checks, and hard constraints.

{ .grid .cards }
```

### Panel usage

Use `.zsa-panel` only for content that benefits from a strong structural boundary: proof, diagnostics, implementation notes, or a high-value conversion block.

Do not place `.grid.cards` inside `.zsa-panel` unless a human explicitly approves the visual sketch. This usually creates double borders and weakens hierarchy.

## Do's and Don'ts

Do:

- Use semantic Markdown and semantic HTML5 in templates.
- Use MkDocs Material variables and native components.
- Keep the interface sparse, structural, and evidence-forward.
- Prefer reusable CSS and existing classes over one-off styling.
- Preserve light/dark mode behavior.
- Use visual hierarchy to make claims, proof, and next steps easier to scan.

Don't:

- Do not use raw HTML in Markdown pages unless Drew explicitly approves that exception.
- Do not use inline styles (`style="..."`).
- Do not use `!important`.
- Do not create arbitrary new spacing, margins, colors, borders, or shadows.
- Do not add generic SaaS gradients, blobs, confetti, glass panels, or decorative illustrations.
- Do not create double-layered borders, especially card grids inside bordered panels.
- Do not make visual changes that only work in one color scheme.

## Agent Workflow

Before editing ZSA UI, agents must:

1. Read this `DESIGN.md` file.
2. Check existing page and CSS patterns before inventing new structure.
3. Use Markdown-native MkDocs primitives before raw HTML or new CSS.
4. If a new visual pattern is required, produce a standalone design sketch or implementation plan first and wait for approval.
5. Do not modify CSS or templates for a new layout until the design direction is approved.
6. After implementation, run `mkdocs build`.
7. For layout, typography, or visual changes, request human visual review; a successful build is not visual QA.

## UI Review Checklist

Before considering a UI change ready, verify:

- It uses `DESIGN.md`, MkDocs variables, and existing structural classes.
- It avoids raw HTML in Markdown unless explicitly approved.
- It avoids inline styles and `!important`.
- It works in both light and dark mode.
- It does not introduce arbitrary spacing, color, shadow, or radius values.
- It does not nest bordered structures unnecessarily.
- It improves scanability, trust, evidence, or conversion rather than merely decoration.
- It keeps content strategy separate from visual implementation rules.
