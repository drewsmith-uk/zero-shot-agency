import re

def update_file(filename, title, slug):
    with open(filename, 'r') as f:
        content = f.read()
    
    # Remove existing title and slug if any
    content = re.sub(r'^title:.*?\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^slug:.*?\n', '', content, flags=re.MULTILINE)
    
    # Insert title and slug after the first ---
    replacement = f"---\ntitle: \"{title}\"\nslug: {slug}\n"
    content = re.sub(r'^---\n', replacement, content)
    
    with open(filename, 'w') as f:
        f.write(content)

update_file('docs/blog/posts/daily-blog-day-6.md', 'Day 6: The 12-Model Matrix, Merge Conflicts, and the Brutal Audit', 'day-6-the-12-model-matrix-merge-conflicts-and-the-brutal-audit')
update_file('docs/blog/posts/daily-blog-day-7.md', 'Day 7: Scaling Agents & Hard AI Guardrails', 'day-7-scaling-agents-and-hard-ai-guardrails')
