#!/usr/bin/env python3
import os
from pathlib import Path

SITE_DIR = Path("site")
BASE_URL = "https://zeroshotagency.com/"

def get_title_from_html(html_path):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            import re
            match = re.search(r'<title>(.*?)</title>', content)
            if match:
                return match.group(1).replace(' - Zero-Shot Agency', '')
    except:
        pass
    return html_path.stem.replace('-', ' ').title()

def get_content_from_md(md_path):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

import re

def get_title_from_md_content(content):
    match = re.search(r'^title:\s*["\']?(.*?)["\']?$', content, flags=re.MULTILINE)
    if match: return match.group(1)
    match = re.search(r'^#\s+(.*)$', content, flags=re.MULTILINE)
    if match: return match.group(1)
    return ""

def build_md_title_map():
    mapping = {}
    for root, _, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                path = Path(root) / file
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        title = get_title_from_md_content(content)
                        if title:
                            norm = re.sub(r'[^a-zA-Z0-9]', '', title).lower()
                            mapping[norm] = path
                except:
                    pass
    return mapping

def main():
    if not SITE_DIR.exists():
        print("Error: site/ directory not found. Run 'mkdocs build' first.")
        return

    title_map = build_md_title_map()

    pages = []
    for root, _, files in os.walk(SITE_DIR):
        for file in files:
            if file.endswith('.html'):
                html_path = Path(root) / file
                rel_path = html_path.relative_to(SITE_DIR)
                
                if str(rel_path) == '404.html':
                    continue
                    
                url_path = str(rel_path).replace('index.html', '')
                if url_path.endswith('.html'):
                    url_path = url_path[:-5] + '/'
                    
                full_url = f"{BASE_URL}{url_path}"
                title = get_title_from_html(html_path)
                
                # Try to find corresponding markdown file
                md_path = Path("docs") / str(rel_path).replace('.html', '.md')
                if not md_path.exists():
                    md_path = Path("docs") / str(rel_path).replace('/index.html', '.md')
                if not md_path.exists():
                    md_path = Path("docs") / str(rel_path).replace('index.html', 'index.md')
                if not md_path.exists():
                    norm_title = re.sub(r'[^a-zA-Z0-9]', '', title).lower()
                    if norm_title in title_map:
                        md_path = title_map[norm_title]
                    
                content = get_content_from_md(md_path) if md_path.exists() else ""
                
                # Strip frontmatter from content
                import re
                content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
                
                pages.append({
                    'url': full_url,
                    'title': title,
                    'content': content
                })

    print(f"Found {len(pages)} pages.")
    
    llms_txt_path = SITE_DIR / "llms.txt"
    llms_full_txt_path = SITE_DIR / "llms-full.txt"
    
    with open(llms_txt_path, 'w', encoding='utf-8') as f:
        f.write(f"# Zero-Shot Agency\n\n")
        f.write(f"> Documentation and index for Zero-Shot Agency\n\n")
        f.write("## Content Pages\n\n")
        for page in sorted(pages, key=lambda x: x['url']):
            f.write(f"- [{page['title']}]({page['url']})\n")
            
    with open(llms_full_txt_path, 'w', encoding='utf-8') as f:
        f.write(f"# Zero-Shot Agency - Full Content\n\n")
        for page in sorted(pages, key=lambda x: x['url']):
            if not page['content'].strip():
                continue
            f.write(f"## {page['title']}\n\n")
            f.write(f"Source: {page['url']}\n\n")
            f.write(page['content'])
            f.write("\n\n---\n\n")
            
    print("Generated site/llms.txt and site/llms-full.txt successfully.")

if __name__ == '__main__':
    main()
