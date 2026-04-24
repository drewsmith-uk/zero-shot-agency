import re
from pathlib import Path

def on_config(config, **kwargs):
    blog_dir = Path("docs/blog/posts")
    posts = []
    if blog_dir.exists():
        for file in blog_dir.glob("*.md"):
            content = file.read_text(encoding="utf-8")
            title_match = re.search(r'^title:\s*["\']?(.*?)["\']?$', content, flags=re.MULTILINE)
            date_match = re.search(r'^date:\s*([\d-]+).*?$', content, flags=re.MULTILINE)
            if title_match and date_match:
                title = title_match.group(1)
                date_str = date_match.group(1)
                
                # Simple slugify matching Material MkDocs
                slug = title.lower()
                slug = re.sub(r'[^a-z0-9\s\-]', '', slug)
                slug = re.sub(r'[\s\-]+', '-', slug).strip('-')
                
                url = f"/blog/{date_str.replace('-', '/')}/{slug}/"
                posts.append({"title": title, "date_str": date_match.group(0), "url": url})
    
    # Sort descending based on exact date string
    posts.sort(key=lambda x: x["date_str"], reverse=True)
    top_3 = posts[:3]
    
    for item in config.get('nav', []):
        if 'Blog' in item:
            new_nav = [{"View All Posts": "blog/index.md"}]
            for p in top_3:
                new_nav.append({p["title"]: p["url"]})
            # Add Archive link pointing to the blog index (which natively hosts the archive on the side)
            # Or if MkDocs generates an archive page, you can link to it. Material MkDocs puts the archive right on the index page sidebar.
            # We will just link to the main blog feed which acts as the archive.
            item['Blog'] = new_nav
            break
            
    return config
