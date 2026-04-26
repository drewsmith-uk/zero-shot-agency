import os
import re
from datetime import datetime

DOCS_DIR = "/home/claw/workspace/zero-shot-agency/docs"

additions = """geo_tactics: [cite-sources, quotation-addition, statistics, fluency, authoritative-tone]
citation_metadata:
  primary_source: "princeton-geo-paper"
  empirical_confidence: "high"
"""

def update_frontmatter(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # match frontmatter
    match = re.match(r"^---\n(.*?)\n---(.*)", content, re.DOTALL)
    if not match:
        return False
    
    frontmatter = match.group(1)
    body = match.group(2)
    
    if 'geo_tactics' in frontmatter:
        return False
        
    # Update date
    today = datetime.now().strftime("%Y-%m-%d")
    frontmatter = re.sub(r"updated: \d{4}-\d{2}-\d{2}", f"updated: {today}", frontmatter)
    
    new_frontmatter = frontmatter + "\n" + additions.strip()
    
    new_content = "---\n" + new_frontmatter + "\n---" + body
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True

count = 0
for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            if update_frontmatter(filepath):
                print(f"Updated {filepath}")
                count += 1
                
print(f"Total updated: {count}")
