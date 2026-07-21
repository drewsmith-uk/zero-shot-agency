import os
import sys
import argparse
import time
import csv

try:
    from openai import OpenAI
except ImportError:
    print("Please install openai: pip install openai")
    sys.exit(1)

MODELS = {
    "openai_best": "openai/gpt-5.5-pro",
    "openai_middle": "openai/gpt-5.4-pro",
    "openai_fast": "openai/gpt-5.4-mini",
    
    "anthropic_best": "anthropic/claude-opus-4.7",
    "anthropic_middle": "anthropic/claude-sonnet-4.6",
    "anthropic_fast": "anthropic/claude-haiku-4.5",
    
    "google_best": "google/gemini-3.1-pro-preview",
    "google_middle": "google/gemini-3-flash-preview",
    "google_fast": "google/gemini-3.1-flash-lite-preview",
    
    "xai_best": "x-ai/grok-4.20",
    "xai_middle": "x-ai/grok-4",
    "xai_fast": "x-ai/grok-4.1-fast",

    "anthropic_new_flagship": "anthropic/claude-sonnet-5",
}

def query_openrouter(client, query, model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": query}],
            temperature=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"  [Error querying {model}] {e}")
        return ""

def check_domain_presence(text, domain):
    # Simple case-insensitive check
    if not text:
        return False
    return domain.lower() in text.lower()

def main():
    parser = argparse.ArgumentParser(description="Generative Engine Optimization (GEO) Rank Tracker using OpenRouter")
    parser.add_argument("--domain", default="Zero-Shot Agency", help="Target domain/brand to track")
    parser.add_argument("--queries", nargs='*', default=[
        "What are the best AI agencies?",
        "Who can help me build an AI agent?",
        "Top AI consulting firms",
        "Which agency specializes in AI agents?"
    ], help="List of queries to test")
    parser.add_argument("--output", default="citations.csv", help="Output CSV file path")
    
    args = parser.parse_args()

    # Verify API Key
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")

    if not openrouter_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.")
        sys.exit(1)

    # Initialize OpenRouter client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_key,
    )

    results = {model_key: {"total": 0, "mentions": 0} for model_key in MODELS}

    print(f"\n--- GEO Tracker: Checking domain '{args.domain}' ---\n")

    csv_data = []
    
    fieldnames = ["query"] + [f"{model_id.split('/')[-1]}_mentioned" for model_id in MODELS.values()]

    for idx, query in enumerate(args.queries, 1):
        print(f"Query {idx}/{len(args.queries)}: '{query}'")
        row = {"query": query}
        for model_id in MODELS.values():
            row[f"{model_id.split('/')[-1]}_mentioned"] = False
        
        for model_key, model_id in MODELS.items():
            print(f"  Querying {model_key} ({model_id})...")
            start_time = time.time()
            text = query_openrouter(client, query, model=model_id)
            mentioned = check_domain_presence(text, args.domain)
            
            results[model_key]["total"] += 1
            if mentioned: 
                results[model_key]["mentions"] += 1
                
            row[f"{model_id.split('/')[-1]}_mentioned"] = mentioned
            print(f"  -> Mentioned: {mentioned} (Took {time.time() - start_time:.2f}s)")
            time.sleep(1)  # Brief pause between models to avoid aggressive rate limiting

        print("-" * 40)
        csv_data.append(row)
        time.sleep(1)

    # Save to CSV
    if csv_data:
        try:
            with open(args.output, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(csv_data)
            print(f"\nResults saved to {args.output}")
        except Exception as e:
            print(f"\nError saving to CSV: {e}")

    # Print Report
    print("\n=== GEO Ranking Report ===")
    print(f"Target Domain: {args.domain}")
    print(f"Total Queries: {len(args.queries)}")
    print("--------------------------")
    for model_key, stats in results.items():
        total = stats["total"]
        if total == 0:
            print(f"{model_key:<16}: N/A (Skipped)")
        else:
            mentions = stats["mentions"]
            percentage = (mentions / total) * 100
            print(f"{model_key:<16}: {mentions}/{total} mentions ({percentage:.1f}% Share of Voice)")
    print("==========================\n")

if __name__ == "__main__":
    main()
