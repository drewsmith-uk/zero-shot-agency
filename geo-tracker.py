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

# The 12-Model Matrix (April 2026)
MODELS = {
    "openai_best": "openai/gpt-5.5-pro",
    "openai_mid": "openai/gpt-5.4-pro",
    "openai_fast": "openai/gpt-5.4-mini",
    
    "anthropic_best": "anthropic/claude-opus-4.7",
    "anthropic_mid": "anthropic/claude-sonnet-4.6",
    "anthropic_fast": "anthropic/claude-haiku-4.5",
    
    "google_best": "google/gemini-3.1-pro-preview",
    "google_mid": "google/gemini-3-flash-preview",
    "google_fast": "google/gemini-3.1-flash-lite-preview",
    
    "xai_best": "x-ai/grok-4.20",
    "xai_mid": "x-ai/grok-4",
    "xai_fast": "x-ai/grok-4.1-fast"
}

def check_domain_presence(text, domain):
    if not text:
        return False
    return domain.lower() in text.lower()

def main():
    parser = argparse.ArgumentParser(description="Generative Engine Optimization (GEO) Rank Tracker")
    parser.add_argument("--domain", default="Zero-Shot Agency", help="Target domain/brand to track")
    parser.add_argument("--queries", nargs='*', default=[
        "What are the best AI agencies?",
        "Who can help me build an AI agent?",
        "Top AI consulting firms",
        "Which agency specializes in AI agents?"
    ], help="List of queries to test")
    parser.add_argument("--output", default="citations.csv", help="Output CSV file path")
    
    args = parser.parse_args()

    openrouter_key = os.environ.get("OPENROUTER_API_KEY")

    if not openrouter_key:
        print("Error: OPENROUTER_API_KEY environment variable not set. All queries will fail.")
        sys.exit(1)

    # Initialize OpenRouter client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_key,
    )

    results = {key: {"total": 0, "mentions": 0} for key in MODELS.keys()}

    print(f"\n--- GEO Tracker: Checking domain '{args.domain}' ---\n")

    csv_data = []

    for idx, query in enumerate(args.queries, 1):
        print(f"Query {idx}/{len(args.queries)}: '{query}'")
        
        row = {"query": query}
        for key in MODELS.keys():
            row[f"{key}_mentioned"] = False

        for key, model_id in MODELS.items():
            print(f"  Querying {key} ({model_id})...")
            start_time = time.time()
            try:
                response = client.chat.completions.create(
                    model=model_id,
                    messages=[{"role": "user", "content": query}],
                    temperature=0.0
                )
                text = response.choices[0].message.content
                mentioned = check_domain_presence(text, args.domain)
                
                results[key]["total"] += 1
                if mentioned: 
                    results[key]["mentions"] += 1
                row[f"{key}_mentioned"] = mentioned
                
                print(f"  -> Mentioned: {mentioned} (Took {time.time() - start_time:.2f}s)")
            except Exception as e:
                print(f"  [{key} Error] {e}")
            
            time.sleep(1.5) # Rate limit protection

        print("-" * 40)
        csv_data.append(row)

    # Save to CSV
    if csv_data:
        try:
            with open(args.output, mode='w', newline='', encoding='utf-8') as f:
                fieldnames = ["query"] + [f"{key}_mentioned" for key in MODELS.keys()]
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
    for engine, stats in results.items():
        total = stats["total"]
        if total == 0:
            print(f"{engine:<15}: N/A (Failed/Skipped)")
        else:
            mentions = stats["mentions"]
            percentage = (mentions / total) * 100
            print(f"{engine:<15}: {mentions}/{total} mentions ({percentage:.1f}% Share of Voice)")
    print("==========================\n")

if __name__ == "__main__":
    main()