import urllib.request
import json
import re
import csv
import subprocess
import sys

CSV_PATH = 'citations.csv'

def fetch_openrouter_models():
    url = "https://openrouter.ai/api/v1/models"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return [m['id'] for m in data.get('data', [])]
    except Exception as e:
        print(f"Error fetching: {e}")
        return []

def get_latest_flagship_models(models):
    openai_models = [m for m in models if re.match(r'^openai/gpt-[0-9]+(\.[0-9]+)?(-pro)?$', m)]
    openai_latest = sorted(openai_models, key=lambda x: [int(p) if p.isdigit() else p for p in re.split(r'(\d+)', x)])[-1] if openai_models else None
    
    anthropic_models = [m for m in models if re.match(r'^anthropic/claude-(opus|sonnet)-[0-9]+(\.[0-9]+)?$', m)]
    anthropic_latest = sorted(anthropic_models, key=lambda x: [int(p) if p.isdigit() else p for p in re.split(r'(\d+)', x)])[-1] if anthropic_models else None
    
    google_models = [m for m in models if re.match(r'^google/gemini-[0-9]+(\.[0-9]+)?-pro(-preview)?$', m)]
    google_latest = sorted(google_models, key=lambda x: [int(p) if p.isdigit() else p for p in re.split(r'(\d+)', x)])[-1] if google_models else None
    
    return [m for m in [openai_latest, anthropic_latest, google_latest] if m]

def main():
    models = fetch_openrouter_models()
    if not models:
        print("Failed to fetch models")
        sys.exit(1)
        
    latest_models = get_latest_flagship_models(models)
    
    # Extract slugs without provider
    new_slugs = [m.split('/')[1] for m in latest_models]
    new_cols = [f"{slug}_mentioned" for slug in new_slugs]
    
    with open(CSV_PATH, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    if not rows:
        print("CSV is empty")
        sys.exit(1)
        
    header = rows[0]
    
    added_models = []
    for col in new_cols:
        if col not in header:
            added_models.append(col.replace('_mentioned', ''))
            header.append(col)
            for row in rows[1:]:
                row.append("False")
                
    if added_models:
        with open(CSV_PATH, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"Added new models to CSV: {added_models}")
        
        issue_title = f"New Flagship LLM Models Detected: {', '.join(added_models)}"
        issue_body = f"The automated LLM monitor has detected new flagship models from OpenRouter:\n\n"
        for m in added_models:
            issue_body += f"- {m}\n"
        issue_body += "\nThese have been added to the `citations.csv` header. The old models will be deprecated in 30 days."
        
        try:
            subprocess.run([
                "gh", "issue", "create",
                "--title", issue_title,
                "--body", issue_body,
                "--label", "enhancement"
            ], check=True)
            print("Successfully created GitHub issue.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create GitHub issue: {e}")
    else:
        print("No new models to add.")

if __name__ == "__main__":
    main()
