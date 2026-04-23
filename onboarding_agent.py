#!/usr/bin/env python3
import os
import sys
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def extract_domain(url):
    """Extract domain from URL for file naming."""
    parsed = urlparse(url)
    domain = parsed.netloc if parsed.netloc else parsed.path
    domain = domain.replace('www.', '')
    return domain

def scrape_headings(url):
    """Scrape H1 and H2 tags from the given URL."""
    print(f"Scraping headings from {url}...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
        h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
        
        return {
            'h1': h1_tags,
            'h2': h2_tags
        }
    except requests.exceptions.RequestException as e:
        print(f"Error scraping headings from {url}: {e}")
        return {'h1': [], 'h2': []}

def scrape_llms_txt(url):
    """Attempt to scrape llms.txt from the root of the domain."""
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    llms_url = urljoin(base_url, '/llms.txt')
    
    print(f"Checking for llms.txt at {llms_url}...")
    try:
        response = requests.get(llms_url, timeout=10)
        if response.status_code == 200:
            print("Found llms.txt!")
            return response.text
        else:
            print(f"No llms.txt found (status code: {response.status_code}).")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching llms.txt: {e}")
        return None

def generate_strategy_brief(domain, headings, llms_content):
    """Generate the Agentic Strategy Brief using OpenAI API."""
    print("Generating Agentic Strategy Brief using OpenAI...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not found. Please set it in a .env file or environment variables.", file=sys.stderr)
        return None
        
    try:
        client = OpenAI(api_key=api_key)
        
        prompt = f"Create an Agentic Strategy Brief for the domain: {domain}.\n\n"
        
        prompt += "Site Headings:\n"
        prompt += "H1:\n" + "\n".join(f"- {h}" for h in headings.get('h1', [])) + "\n"
        prompt += "H2:\n" + "\n".join(f"- {h}" for h in headings.get('h2', [])) + "\n\n"
        
        if llms_content:
            prompt += "Content of llms.txt:\n"
            prompt += f"```\n{llms_content[:3000]}\n```\n\n" # Truncate to avoid huge prompts
        else:
            prompt += "No llms.txt provided.\n\n"
            
        prompt += """
Please analyze the provided information and structure the brief with the following sections:
1. Executive Summary
2. Target Audience & Value Proposition
3. Recommended AI Agent Interventions (where agents could assist or automate)
4. Strategic Next Steps

Format the output entirely in professional Markdown.
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a strategic AI consultant designing agentic workflows for businesses. Provide your insights strictly in professional Markdown format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating strategy brief from OpenAI: {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate an Agentic Strategy Brief for a given domain.")
    parser.add_argument("url", help="The target URL (e.g., https://example.com)")
    args = parser.parse_args()
    
    url = args.url
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
        
    domain = extract_domain(url)
    
    headings = scrape_headings(url)
    llms_content = scrape_llms_txt(url)
    
    brief_markdown = generate_strategy_brief(domain, headings, llms_content)
    
    if brief_markdown:
        output_filename = f"{domain}_strategy_brief.md"
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(brief_markdown)
            print(f"Success! Strategy brief saved to {output_filename}")
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Failed to generate the strategy brief.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
