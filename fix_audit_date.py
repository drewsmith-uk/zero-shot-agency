import re

with open("ef_geo_audit.md", "r") as f:
    text = f.read()

# Add the snapshot date after Methodology & Scope
old_note = r'> \*\*Note:\*\* This document is a free public overview'
new_note = r'> **Snapshot Date:** Findings reflect a directional review conducted in April 2026.\n> \n> **Note:** This document is a free public overview'

text = re.sub(old_note, new_note, text)

with open("ef_geo_audit.md", "w") as f:
    f.write(text)
