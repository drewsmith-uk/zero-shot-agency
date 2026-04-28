with open('docs/blog/posts/daily-blog-day-3.md', 'r') as f:
    content = f.read()

# Replace the messy frontmatter
content = content.replace('title: "Day 3: The "Drafts via PR" Workflow"\n', '')
content = content.replace('title: "Day 3: Developer-Grade Publishing & Preventing Hallucination Leaks"\n', '  empirical_confidence: "high"\n')

# Put the proper title at the top
content = content.replace('---\nslug:', '---\ntitle: "Day 3: Developer-Grade Publishing & Preventing Hallucination Leaks"\nslug:')

with open('docs/blog/posts/daily-blog-day-3.md', 'w') as f:
    f.write(content)

