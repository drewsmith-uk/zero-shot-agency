#!/usr/bin/env python3
import os
import sys
import argparse
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

def fetch_page_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        h1_tags = [tag.get_text(strip=True) for tag in soup.find_all('h1')]
        h2_tags = [tag.get_text(strip=True) for tag in soup.find_all('h2')]
        
        return {
            "h1": h1_tags,
            "h2": h2_tags
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return {"h1": [], "h2": []}

def fetch_llms_txt(base_url):
    parsed = urlparse(base_url)
    llms_url = f"{parsed.scheme}://{parsed.netloc}/llms.txt"
    try:
        response = requests.get(llms_url, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.RequestException:
        return None

def generate_strategy_brief(domain, content, llms_text):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not found. Please set it in a .env file.", file=sys.stderr)
        sys.exit(1)
        
    client = OpenAI(api_key=api_key)
    
    prompt = f"Analyze the following information scraped from {domain} and generate an 'Agentic Strategy Brief'.\n\n"
    
    if content['h1'] or content['h2']:
        prompt += "Website Headers (H1 and H2):\n"
        for h1 in content['h1']:
            prompt += f"- H1: {h1}\n"
        for h2 in content['h2']:
            prompt += f"- H2: {h2}\n"
        prompt += "\n"
    else:
        prompt += "No H1 or H2 headers were successfully extracted from the website.\n\n"
    
    if llms_text:
        prompt += "llms.txt contents:\n"
        prompt += f"{llms_text}\n\n"
    else:
        prompt += "No llms.txt file was found for this domain.\n\n"
        
    prompt += ("Please provide a professional Agentic Strategy Brief formatted in Markdown. "
               "Include a summary of the site's apparent purpose, potential areas where AI agents could add value, "
               "and recommended next steps for onboarding this domain into an agentic framework.")

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert AI strategist and technical consultant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate an Agentic Strategy Brief for a domain.")
    parser.add_argument("url", help="The target URL to analyze (e.g., https://example.com)")
    args = parser.parse_args()
    
    url = args.url
    if not url.startswith("http"):
        url = "https://" + url
        
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    print(f"Scraping content from {url}...")
    content = fetch_page_content(url)
    
    print(f"Checking for llms.txt at {domain}...")
    llms_text = fetch_llms_txt(url)
    if llms_text:
        print("Found llms.txt.")
    else:
        print("No llms.txt found.")
        
    print("Generating Agentic Strategy Brief via OpenAI API...")
    brief = generate_strategy_brief(domain, content, llms_text)
    
    # Output to concepts/ directory
    output_dir = Path("concepts")
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / f"{domain.replace(':', '_')}-strategy.md"
    try:
        with open(output_file, "w") as f:
            f.write(brief)
        print(f"Strategy Brief successfully written to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
