#!/usr/bin/env python3
"""
onboarding_agent.py

Takes a domain URL as input, scrapes the site for H1/H2 tags and the llms.txt file,
and uses the OpenAI API to generate an 'Agentic Strategy Brief' formatted in Markdown.
Outputs a clean markdown file.

Also supports --analyze-gaps <query> to perform semantic gap analysis on competitor sites.
"""

import os
import sys
import argparse
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
from urllib.parse import urlparse
from pathlib import Path

def setup_env():
    """Load environment variables and ensure OpenAI API key is present."""
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        sys.stderr.write("Error: OPENAI_API_KEY environment variable is missing. Please set it in a .env file.\n")
        sys.exit(1)

def scrape_headers(url: str) -> dict:
    """Scrape H1 and H2 tags from the given URL."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        h1s = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
        h2s = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
        
        return {"h1": h1s, "h2": h2s}
    except requests.RequestException as e:
        sys.stderr.write(f"Warning: Failed to fetch or parse {url} for headers. Error: {e}\n")
        return {"h1": [], "h2": []}

def fetch_llms_txt(url: str) -> str:
    """Fetch the llms.txt file from the root of the domain."""
    parsed_url = urlparse(url)
    llms_url = f"{parsed_url.scheme}://{parsed_url.netloc}/llms.txt"
    
    try:
        response = requests.get(llms_url, timeout=10)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        sys.stderr.write(f"Warning: Failed to fetch llms.txt from {llms_url}. Error: {e}\n")
    return ""

def generate_strategy_brief(domain: str, headers: dict, llms_text: str) -> str:
    """Generate the strategy brief using OpenAI API."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"Please generate an Agentic Strategy Brief for the domain: {domain}.\n\n"
    
    prompt += "### Scraped Headers (H1 and H2)\n"
    if headers["h1"]:
        prompt += "**H1 Tags:**\n" + "\n".join(f"- {h1}" for h1 in headers["h1"]) + "\n"
    if headers["h2"]:
        prompt += "**H2 Tags:**\n" + "\n".join(f"- {h2}" for h2 in headers["h2"]) + "\n"
    if not headers["h1"] and not headers["h2"]:
        prompt += "No H1 or H2 tags were found on the website.\n"
        
    prompt += "\n### llms.txt Content\n"
    if llms_text:
        prompt += f"```text\n{llms_text}\n```\n"
    else:
        prompt += "No llms.txt file found at the root of the domain.\n"
        
    prompt += "\nBased on the information above, provide a professional Agentic Strategy Brief formatted in Markdown. Include a summary of the site's apparent purpose, potential areas where AI agents could add value, and recommended next steps for onboarding this domain into an agentic framework."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a strategic AI consultant analyzing website data to build agentic onboarding briefs."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        sys.stderr.write(f"Error: OpenAI API request failed. Details: {e}\n")
        sys.exit(1)

def save_brief(domain: str, content: str):
    """Save the markdown brief to a file."""
    output_dir = Path("concepts")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"{domain.replace(':', '_')}_strategy_brief.md"
    filepath = output_dir / filename
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Success: Agentic Strategy Brief saved to {filepath}")
    except IOError as e:
        sys.stderr.write(f"Error: Could not save brief to {filepath}. Details: {e}\n")
        sys.exit(1)

def perform_gap_analysis(query: str):
    """Search DuckDuckGo, scrape top results, and generate Semantic Gap Injection."""
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        sys.stderr.write("Error: duckduckgo-search library is missing. Please add it to requirements.txt and install it.\n")
        sys.exit(1)

    print(f"Searching web for query: '{query}'...")
    results = []
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
    except Exception as e:
        sys.stderr.write(f"Warning: DuckDuckGo search failed. Error: {e}\n")
    
    if not results:
        sys.stderr.write("No search results found.\n")
        return
        
    scraped_data = []
    for res in results:
        url = res.get("href")
        if not url:
            continue
        print(f"Scraping {url}...")
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            h1s = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
            h2s = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
            h3s = [h3.get_text(strip=True) for h3 in soup.find_all('h3')]
            
            scraped_data.append({
                "url": url,
                "title": res.get("title", ""),
                "snippet": res.get("body", ""),
                "h1": h1s,
                "h2": h2s,
                "h3": h3s
            })
        except Exception as e:
            sys.stderr.write(f"Warning: Failed to scrape {url}. Error: {e}\n")
            
    print("Generating Semantic Gap Injection with OpenAI...")
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"Please analyze the top search results for the query: '{query}' and identify semantic gaps.\n\n"
    prompt += "### Competitor Data (Top Search Results)\n"
    
    for idx, data in enumerate(scraped_data):
        prompt += f"**Result {idx+1}: {data['title']}**\n"
        prompt += f"URL: {data['url']}\n"
        prompt += f"Snippet: {data['snippet']}\n"
        if data['h1']:
            prompt += "H1: " + " | ".join(data['h1']) + "\n"
        if data['h2']:
            prompt += "H2: " + " | ".join(data['h2'][:5]) + " (truncated)\n"
        prompt += "\n"
        
    prompt += "Based on the competitor data above, identify the semantic gaps (topics, keywords, questions, or themes) that are missing or underrepresented across these top competitors. Generate a 'Semantic Gap Injection' Markdown document. Output the markdown."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an SEO and content strategy expert analyzing competitor content to find semantic gaps and opportunities."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        content = response.choices[0].message.content
        
        output_dir = Path("concepts")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        safe_query = "".join([c if c.isalnum() else "_" for c in query]).strip("_")
        filename = f"{safe_query}_gap_analysis.md"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Success: Semantic Gap Injection saved to {filepath}")
    except Exception as e:
        sys.stderr.write(f"Error: API request or file save failed. Details: {e}\n")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Scrape a domain and generate an Agentic Strategy Brief, or perform gap analysis.")
    parser.add_argument("url", nargs="?", help="The target domain URL (e.g., https://example.com) for strategy brief")
    parser.add_argument("--analyze-gaps", type=str, help="Search the web for the query, scrape top results, and identify semantic gaps.")
    args = parser.parse_args()

    if not args.url and not args.analyze_gaps:
        parser.print_help()
        sys.exit(1)

    setup_env()

    if args.analyze_gaps:
        perform_gap_analysis(args.analyze_gaps)
    
    if args.url:
        url = args.url
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
            
        domain = urlparse(url).netloc
        if not domain:
            sys.stderr.write("Error: Invalid URL provided.\n")
            sys.exit(1)

        print(f"Scraping headers from {url}...")
        headers = scrape_headers(url)

        print(f"Checking for llms.txt at {domain}...")
        llms_text = fetch_llms_txt(url)

        print("Generating Agentic Strategy Brief...")
        brief_content = generate_strategy_brief(domain, headers, llms_text)

        save_brief(domain, brief_content)

if __name__ == "__main__":
    main()
