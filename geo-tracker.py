import os
import sys
import argparse
import time

try:
    from openai import OpenAI
except ImportError:
    print("Please install openai: pip install openai")
    sys.exit(1)

try:
    from anthropic import Anthropic
except ImportError:
    print("Please install anthropic: pip install anthropic")
    sys.exit(1)

try:
    import google.generativeai as genai
except ImportError:
    print("Please install google-generativeai: pip install google-generativeai")
    sys.exit(1)

def query_openai(client, query, model="gpt-4o"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": query}],
            temperature=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"  [OpenAI Error] {e}")
        return ""

def query_anthropic(client, query, model="claude-3-7-sonnet-20250219"):
    try:
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": query}],
            temperature=0.0
        )
        return response.content[0].text
    except Exception as e:
        print(f"  [Anthropic Error] {e}")
        return ""

def query_gemini(query, model="gemini-1.5-pro"):
    try:
        gemini_model = genai.GenerativeModel(model)
        response = gemini_model.generate_content(query, generation_config={"temperature": 0.0})
        return response.text
    except Exception as e:
        print(f"  [Gemini Error] {e}")
        return ""

def check_domain_presence(text, domain):
    # Simple case-insensitive check
    if not text:
        return False
    return domain.lower() in text.lower()

def main():
    parser = argparse.ArgumentParser(description="Generative Engine Optimization (GEO) Rank Tracker")
    parser.add_argument("--domain", required=True, help="Target domain to track (e.g., 'example.com')")
    parser.add_argument("--queries", required=True, nargs='+', help="List of queries to test")
    
    args = parser.parse_args()

    # Verify API Keys
    openai_key = os.environ.get("OPENAI_API_KEY")
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    gemini_key = os.environ.get("GEMINI_API_KEY")

    if not openai_key:
        print("Warning: OPENAI_API_KEY environment variable not set. GPT-4o queries will fail.")
    if not anthropic_key:
        print("Warning: ANTHROPIC_API_KEY environment variable not set. Claude queries will fail.")
    if not gemini_key:
        print("Warning: GEMINI_API_KEY environment variable not set. Gemini queries will fail.")

    # Initialize clients
    openai_client = OpenAI(api_key=openai_key) if openai_key else None
    anthropic_client = Anthropic(api_key=anthropic_key) if anthropic_key else None
    
    if gemini_key:
        genai.configure(api_key=gemini_key)

    results = {
        "gpt-4o": {"total": 0, "mentions": 0},
        "claude-3.7": {"total": 0, "mentions": 0},
        "gemini": {"total": 0, "mentions": 0}
    }

    print(f"\\n--- GEO Tracker: Checking domain '{args.domain}' ---\\n")

    for idx, query in enumerate(args.queries, 1):
        print(f"Query {idx}/{len(args.queries)}: '{query}'")
        
        # GPT-4o
        if openai_client:
            print("  Querying GPT-4o...")
            start_time = time.time()
            text = query_openai(openai_client, query)
            mentioned = check_domain_presence(text, args.domain)
            results["gpt-4o"]["total"] += 1
            if mentioned: results["gpt-4o"]["mentions"] += 1
            print(f"  -> Mentioned: {mentioned} (Took {time.time() - start_time:.2f}s)")
        else:
            print("  Skipping GPT-4o (No API Key)")

        # Claude 3.7
        if anthropic_client:
            print("  Querying Claude 3.7...")
            start_time = time.time()
            text = query_anthropic(anthropic_client, query)
            mentioned = check_domain_presence(text, args.domain)
            results["claude-3.7"]["total"] += 1
            if mentioned: results["claude-3.7"]["mentions"] += 1
            print(f"  -> Mentioned: {mentioned} (Took {time.time() - start_time:.2f}s)")
        else:
            print("  Skipping Claude 3.7 (No API Key)")

        # Gemini
        if gemini_key:
            print("  Querying Gemini...")
            start_time = time.time()
            text = query_gemini(query)
            mentioned = check_domain_presence(text, args.domain)
            results["gemini"]["total"] += 1
            if mentioned: results["gemini"]["mentions"] += 1
            print(f"  -> Mentioned: {mentioned} (Took {time.time() - start_time:.2f}s)")
        else:
            print("  Skipping Gemini (No API Key)")

        print("-" * 40)
        time.sleep(1)  # Brief pause between queries to avoid rate limits

    # Print Report
    print("\\n=== GEO Ranking Report ===")
    print(f"Target Domain: {args.domain}")
    print(f"Total Queries: {len(args.queries)}")
    print("--------------------------")
    for engine, stats in results.items():
        total = stats["total"]
        if total == 0:
            print(f"{engine.upper():<12}: N/A (Skipped)")
        else:
            mentions = stats["mentions"]
            percentage = (mentions / total) * 100
            print(f"{engine.upper():<12}: {mentions}/{total} mentions ({percentage:.1f}% Share of Voice)")
    print("==========================\\n")

if __name__ == "__main__":
    main()
