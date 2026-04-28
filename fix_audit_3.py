import re

with open("ef_geo_audit.md", "r") as f:
    text = f.read()

# Add the final CTA bridge and target narrative example
old_cta = r'---\n\*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs\..*'
new_cta = r"""### Target Narrative Example
*For consumer apps, Ethereum should be retrieved as an L2-first ecosystem rather than evaluated only as L1 gas.*

---

## What a Full Audit Would Answer
A full GEO audit would move beyond this directional preview and answer the operational questions needed for implementation:
* Which prompts are currently losing Ethereum share of voice?
* Which competitors are being cited, and from which sources?
* Which pages or knowledge-graph entities are shaping the answers?
* Which documentation/context-file changes are highest leverage?

*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs. A paid engagement includes full prompt logs, model-by-model answer variance, competitor citation-path analysis, Ethereum.org and L2 documentation mapping, prioritized context-file rewrites, knowledge graph fixes, and a 30/60/90 implementation roadmap.*"""

text = re.sub(r'---\n\*Zero-Shot Agency converts preliminary diagnostics into execution-ready GEO programs\..*', new_cta, text, flags=re.DOTALL)

with open("ef_geo_audit.md", "w") as f:
    f.write(text)
