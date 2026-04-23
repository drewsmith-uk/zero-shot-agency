import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from dotenv import load_dotenv
from openai import OpenAI
import sys

# Load environment variables
load_dotenv()

def fetch_html_content(url):
    """Fetches the HTML content of a given URL."""
    try:
        # Adding some standard headers to prevent basic blocks
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}", file=sys.stderr)
        return None

def extract_headings(html_content):
    """Extracts H1 and H2 tags from HTML content."""
    if not html_content:
        return []
    
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        headings = []
        
        for tag in soup.find_all(['h1', 'h2']):
            text = tag.get_text(strip=True)
            if text:
                headings.append(f"{tag.name.upper()}: {text}")
                
        return headings
    except Exception as e:
        print(f"Error parsing HTML: {e}", file=sys.stderr)
        return []

def fetch_llms_txt(domain_url):
    """Fetches the llms.txt file from the root of the domain."""
    parsed_url = urlparse(domain_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    llms_txt_url = urljoin(base_url, "/llms.txt")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(llms_txt_url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"llms.txt not found at {llms_txt_url} (status: {response.status_code})", file=sys.stderr)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching llms.txt: {e}", file=sys.stderr)
        return None

def generate_strategy_brief(domain_url, headings, llms_txt_content):
    """Uses OpenAI API to generate an Agentic Strategy Brief."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.", file=sys.stderr)
        return None
        
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}", file=sys.stderr)
        return None
    
    headings_text = "\n".join(headings) if headings else "No headings found."
    llms_text = llms_txt_content if llms_txt_content else "No llms.txt found."
    
    prompt = f"""
You are an expert AI Strategist. Based on the following information scraped from a client's website ({domain_url}), create an 'Agentic Strategy Brief'.
This brief should outline how AI agents could be integrated into their business model, potential use cases, and automation opportunities.

Website Headings (H1/H2):
{headings_text}

Contents of llms.txt:
{llms_text}

Format the output strictly as a clean Markdown file with appropriate headers, bullet points, and actionable insights. Do not include any conversational filler.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional AI consultant and strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate an Agentic Strategy Brief from a domain URL.")
    parser.add_argument("url", help="The domain URL to scrape (e.g., https://example.com)")
    parser.add_argument("-o", "--output", help="Output file name (default: strategy_brief.md)", default="strategy_brief.md")
    
    args = parser.parse_args()
    url = args.url
    
    # Ensure URL has a scheme
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
        
    print(f"Scraping {url} for headings...")
    html_content = fetch_html_content(url)
    headings = extract_headings(html_content)
    
    print(f"Checking for llms.txt at {url}...")
    llms_txt_content = fetch_llms_txt(url)
    
    print("Generating Agentic Strategy Brief using OpenAI...")
    brief_content = generate_strategy_brief(url, headings, llms_txt_content)
    
    if brief_content:
        try:
            output_path = args.output
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(brief_content)
            print(f"\nSuccess! Strategy brief saved to {output_path}")
        except IOError as e:
            print(f"Error writing to file {output_path}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Failed to generate the strategy brief.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
