---
version: alpha
name: ZSA Technical Brutalism
description: High-signal, structural IDE aesthetic. Brutal honesty and empirical proof.
colors:
  dark_bg: "#0d1117"
  dark_paper: "#161b22"
  dark_ink: "#c9d1d9"
  dark_muted: "#8b949e"
  dark_line: "#30363d"
  dark_accent: "#58a6ff"
  
  light_bg: "#f6f8fa"
  light_paper: "#ffffff"
  light_ink: "#111827"
  light_muted: "#6b7280"
  light_line: "#d1d5db"
  light_accent: "#2563eb"
  
typography:
  fontFamily: '"Geist", -apple-system, BlinkMacSystemFont, sans-serif'
  fontFamilyMono: '"Geist Mono", monospace'
spacing:
  border: 1px
rounded:
  all: 0px
components:
  card:
    border: "{spacing.border} solid var(--md-typeset-color)"
    rounded: "{rounded.all}"
---

## Overview
Technical Brutalism. This is a terminal-inspired, architectural approach designed to strip away "SaaS pop-art" aesthetics (like heavy drop shadows and thick borders) in favor of high-signal clarity.

## Implementation Rules (MkDocs Material)
To implement this holistically without fighting the MkDocs Material theme:
1. **Never use `!important`**. Scope overrides by prefixing with `.md-typeset` or `[data-md-color-scheme="slate"]`.
2. **Variable Mapping**: Map our palette directly to Material's native variables in `extra_css`.
   - `var(--bg)` maps to `--md-default-bg-color`
   - `var(--paper)` maps to `--md-code-bg-color` or custom panel backgrounds
   - `var(--line)` overrides `--md-typeset-table-color` or structural borders.
3. **Zero Radius**: Override `--md-border-radius` to `0px` globally to ensure brutalist sharp corners.
4. **Grid/Structure**: Apply the 1px `var(--line)` borders to `.md-content`, `.md-nav`, and `.md-header` to create the wireframe/IDE layout effect.