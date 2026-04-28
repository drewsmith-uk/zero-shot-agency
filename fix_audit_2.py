import re

with open("ef_geo_audit.md", "r") as f:
    text = f.read()

text = text.replace(r"**Methodology & Scope:** We tested five core architectural \"buying themes\" across representative frontier models to map Ethereum's structural narrative within AI retrieval systems.", r"**Methodology & Scope:** Testing covered multiple frontier LLM and AI-search systems using repeated prompt variants across five core architectural \"buying themes\" to map Ethereum's structural narrative within AI retrieval systems.")

old_cta = r'---\n\*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs\.'
old_cta_escaped = r'---\\n\*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs\.'

new_cta = r"""### Target Narrative Example\n*For consumer apps, Ethereum should be retrieved as an L2-first ecosystem rather than evaluated only as L1 gas.*\n\n---\n\n## What a full audit would answer:\n* Which prompts are currently losing Ethereum share of voice?\n* Which competitors are being cited, and from which sources?\n* Which pages or knowledge-graph entities are shaping the answers?\n* Which documentation/context-file changes are highest leverage?\n\n*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs."""

if r'---\n*Zero-Shot' in text:
    text = re.sub(r'---\n\*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs\.', new_cta, text)
elif r'---\n\*Zero-Shot' in text:
     text = re.sub(r'---\n\\\*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs\.', new_cta, text)
elif r'---\n*Zero-Shot' in text.replace(r'\n', '\n'):
    text = text.replace(r'---\n*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs.', new_cta.replace('\n', r'\n'))

with open("ef_geo_audit.md", "w") as f:
    f.write(text.replace('\\n', '\n').replace('\\"', '"'))
