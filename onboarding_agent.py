#!/usr/bin/env python3
"""
onboarding_agent.py

This script serves as an automated onboarding agent. It takes a domain URL,
scrapes the main page for H1 and H2 tags, attempts to read the /llms.txt file,
and uses the OpenAI API to generate an "Agentic Strategy Brief" formatted in Markdown.
"""

import argparse
import logging
import os
import sys
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def setup_environment():
    """Loads environment variables and initializes the OpenAI client."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OPENAI_API_KEY not found. Please set it in your environment or a .env file.")
        sys.exit(1)
    return OpenAI(api_key=api_key)

def fetch_url(url):
    """Fetches text content from a given URL with basic error handling."""
    try:
        logging.info(f"Fetching content from {url}...")
        # Include a user agent to prevent basic blocking
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; OnboardingAgent/1.0)'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            logging.info(f"404 Not Found for {url} (This is normal for missing /llms.txt files).")
        else:
            logging.error(f"HTTP Error for {url}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch {url}: {e}")
        return None

def extract_headings(html_content):
    """Extracts H1 and H2 tags from HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
    h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
    return h1_tags, h2_tags

def generate_strategy_brief(client, domain, h1_tags, h2_tags, llms_txt_content):
    """Generates an Agentic Strategy Brief using the OpenAI API."""
    logging.info("Generating Agentic Strategy Brief via OpenAI API...")
    
    system_prompt = (
        "You are an expert AI Strategist. Your task is to generate a comprehensive "
        "'Agentic Strategy Brief' formatted in Markdown based on the provided website data."
    )
    
    # Construct the user payload
    user_content = f"Target Domain: {domain}\n\n"
    
    if h1_tags:
        user_content += "H1 Tags:\n" + "\n".join(f"- {h}" for h in h1_tags) + "\n\n"
    else:
        user_content += "H1 Tags: None found.\n\n"
        
    if h2_tags:
        user_content += "H2 Tags:\n" + "\n".join(f"- {h}" for h in h2_tags) + "\n\n"
    else:
        user_content += "H2 Tags: None found.\n\n"
    
    if llms_txt_content:
        # Truncate llms.txt if it's abnormally large to avoid blowing up the context window
        user_content += f"llms.txt Content:\n{llms_txt_content[:10000]}\n\n" 
    else:
        user_content += "llms.txt Content: Not found or inaccessible.\n\n"

    user_content += (
        "Please provide a structured Strategy Brief including the following sections:\n"
        "1. **Executive Summary**\n"
        "2. **Value Proposition Analysis** (Based on headings/messaging)\n"
        "3. **Agentic Automation Opportunities** (How AI agents can assist this specific business/project)\n"
        "4. **Technical & LLM Integration Strategy** (Referencing llms.txt details if available)\n"
        "5. **Recommended Next Steps**\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Can be swapped to gpt-4-turbo or others if needed
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Failed to generate brief with OpenAI API: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Scrape a website and generate an Agentic Strategy Brief.")
    parser.add_argument("url", help="The full domain URL to analyze (e.g., https://example.com)")
    args = parser.parse_args()

    # 1. Setup environment and API keys
    client = setup_environment()
    
    # Parse URL properly
    url = args.url
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
        
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc or parsed_url.path
    
    # 2. Scrape main page for H1/H2
    html_content = fetch_url(url)
    h1_tags, h2_tags = [], []
    if html_content:
        h1_tags, h2_tags = extract_headings(html_content)
    else:
        logging.warning(f"Could not retrieve HTML content for {url}. Brief will be minimal.")

    # 3. Scrape llms.txt
    llms_url = f"{parsed_url.scheme}://{domain_name}/llms.txt"
    llms_txt_content = fetch_url(llms_url)
    
    if not html_content and not llms_txt_content:
        logging.error("Failed to retrieve any content (HTML or llms.txt). Exiting.")
        sys.exit(1)

    # 4. Generate Brief
    brief_content = generate_strategy_brief(client, domain_name, h1_tags, h2_tags, llms_txt_content)
    
    if not brief_content:
        logging.error("Failed to generate brief. Exiting.")
        sys.exit(1)

    # 5. Save output
    safe_domain = domain_name.replace('.', '_')
    output_filename = f"brief_{safe_domain}.md"
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(brief_content)
        logging.info(f"Success! Agentic Strategy Brief saved to: {os.path.abspath(output_filename)}")
    except IOError as e:
        logging.error(f"Failed to save the brief to {output_filename}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
