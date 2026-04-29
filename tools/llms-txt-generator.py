#!/usr/bin/env python3
"""
llms-txt-generator.py
A script to crawl a domain and generate a perfect llms.txt and llms-full.txt file
conforming to the llms.txt specification.

Usage:
    python llms-txt-generator.py https://example.com

Dependencies:
    pip install requests beautifulsoup4 markdownify
"""

import argparse
import os
import sys
import time
import urllib.parse
import urllib.robotparser

try:
    import requests
    from bs4 import BeautifulSoup
    import markdownify
except ImportError as e:
    print(f"Missing dependency: {e}", file=sys.stderr)
    print("Please install required dependencies:", file=sys.stderr)
    print("pip install requests beautifulsoup4 markdownify", file=sys.stderr)
    sys.exit(1)

def get_robots_parser(base_url):
    """Initializes and returns a robot parser for the given domain."""
    parsed_base = urllib.parse.urlparse(base_url)
    robots_url = f"{parsed_base.scheme}://{parsed_base.netloc}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        # Use a reasonable timeout for fetching robots.txt
        response = requests.get(robots_url, timeout=10)
        if response.status_code == 200:
            rp.parse(response.text.splitlines())
    except Exception as e:
        print(f"Warning: Could not read robots.txt from {robots_url}: {e}")
    return rp

def is_same_domain(url, base_domain):
    """Check if the URL belongs to the base domain."""
    parsed = urllib.parse.urlparse(url)
    return parsed.netloc == base_domain or parsed.netloc == ''

def normalize_url(url):
    """Normalize URL by removing fragments and trailing slashes."""
    parsed = urllib.parse.urlparse(url)
    # Remove fragment
    parsed = parsed._replace(fragment='')
    url = urllib.parse.urlunparse(parsed)
    if url.endswith('/'):
        url = url[:-1]
    return url

def crawl(start_url, max_pages=50, delay=0.5):
    """Crawls the domain starting from start_url."""
    visited = set()
    to_visit = [normalize_url(start_url)]
    parsed_start = urllib.parse.urlparse(start_url)
    base_domain = parsed_start.netloc
    
    rp = get_robots_parser(start_url)
    user_agent = "LLMsTxtGeneratorBot/1.0"
    headers = {"User-Agent": user_agent}
    
    pages_data = []
    
    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        url = normalize_url(url)
            
        if url in visited:
            continue
            
        if not rp.can_fetch(user_agent, url):
            print(f"Skipping {url} (disallowed by robots.txt)")
            continue
            
        print(f"Crawling ({len(visited)+1}/{max_pages}): {url}")
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            
            # Record as visited whether successful or not to avoid infinite retries
            visited.add(url)
            
            if resp.status_code != 200:
                print(f"  -> Failed: HTTP {resp.status_code}")
                continue
            
            # Only process HTML
            content_type = resp.headers.get('Content-Type', '')
            if 'text/html' not in content_type:
                print(f"  -> Skipping non-HTML content: {content_type}")
                continue
                
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            # Extract title
            title = url
            if soup.title and soup.title.string:
                title = soup.title.string.strip()
            elif soup.h1:
                title = soup.h1.get_text().strip()
                
            # Remove scripts, styles, and navigational elements to focus on main content
            for element in soup(["script", "style", "nav", "footer", "header", "noscript"]):
                element.extract()
                
            # Try to find the main content container
            main_content = soup.find('main') or soup.find('article') or soup.find(id='content') or soup.body
            
            if not main_content:
                print("  -> No main content found")
                continue
                
            # Convert to markdown
            md_content = markdownify.markdownify(str(main_content), heading_style="ATX", strip=['img'])
            md_content = md_content.strip()
            
            if not md_content:
                print("  -> Content was empty after markdown conversion")
                continue
                
            pages_data.append({
                'url': url,
                'title': title,
                'content': md_content
            })
            
            # Find links for further crawling
            for a in soup.find_all('a', href=True):
                href = a['href']
                full_url = urllib.parse.urljoin(url, href)
                
                # Only follow HTTP(S) links on the same domain
                if full_url.startswith('http') and is_same_domain(full_url, base_domain):
                    norm_url = normalize_url(full_url)
                    if norm_url not in visited and norm_url not in to_visit:
                        to_visit.append(norm_url)
                        
            time.sleep(delay) # Respectful delay
            
        except requests.RequestException as e:
            print(f"  -> Network error crawling {url}: {e}")
        except Exception as e:
            print(f"  -> Unexpected error crawling {url}: {e}")
            
    return pages_data

def generate_llms_txt(pages_data, domain, output_dir):
    """Generates llms.txt and llms-full.txt files."""
    llms_txt_path = os.path.join(output_dir, "llms.txt")
    llms_full_txt_path = os.path.join(output_dir, "llms-full.txt")
    
    # Generate llms.txt (index)
    try:
        with open(llms_txt_path, 'w', encoding='utf-8') as f:
            f.write(f"# {domain}\n\n")
            f.write(f"> Documentation and index for {domain}\n\n")
            f.write("## Content Pages\n\n")
            
            for page in pages_data:
                # Clean up title for markdown link
                title = page['title'].replace('[', '(').replace(']', ')')
                f.write(f"- [{title}]({page['url']})\n")
                
        # Generate llms-full.txt (concatenated content)
        with open(llms_full_txt_path, 'w', encoding='utf-8') as f:
            f.write(f"# {domain} - Full Content\n\n")
            
            for page in pages_data:
                f.write(f"## {page['title']}\n\n")
                f.write(f"Source: {page['url']}\n\n")
                f.write(page['content'])
                f.write("\n\n---\n\n")
                
        print(f"\nSuccess! Generated:")
        print(f"  - {llms_txt_path} ({len(pages_data)} pages indexed)")
        print(f"  - {llms_full_txt_path} (full markdown content)")
    except Exception as e:
        print(f"Error writing output files: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(
        description="Crawl a domain and generate llms.txt and llms-full.txt files."
    )
    parser.add_argument("url", help="Starting URL to crawl (e.g., https://example.com)")
    parser.add_argument("--max-pages", type=int, default=50, help="Maximum number of pages to crawl (default: 50)")
    parser.add_argument("--output", default=".", help="Output directory for the generated files (default: current directory)")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests in seconds (default: 0.5)")
    
    args = parser.parse_args()
    
    parsed = urllib.parse.urlparse(args.url)
    if not parsed.scheme or not parsed.netloc:
        print("Error: Invalid URL. Make sure to include http:// or https://", file=sys.stderr)
        sys.exit(1)
        
    print(f"Starting crawl for domain: {parsed.netloc}")
    print(f"Starting URL: {args.url}")
    print(f"Max pages: {args.max_pages}")
    print("-" * 40)
    
    pages_data = crawl(args.url, max_pages=args.max_pages, delay=args.delay)
    
    print("-" * 40)
    if pages_data:
        os.makedirs(args.output, exist_ok=True)
        generate_llms_txt(pages_data, parsed.netloc, args.output)
    else:
        print("No pages were successfully crawled. Check the URL and try again.")

if __name__ == "__main__":
    main()
