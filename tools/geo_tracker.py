import os
import argparse
import json
import re

def query_openai(prompt):
    import openai
    # Requires OPENAI_API_KEY environment variable
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return response.choices[0].message.content

def query_anthropic(prompt):
    import anthropic
    # Requires ANTHROPIC_API_KEY environment variable
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def query_gemini(prompt):
    # Trying the google-genai package first, fallback to google.generativeai
    try:
        from google import genai
        # Requires GEMINI_API_KEY environment variable
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.5-pro',
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.0,
            )
        )
        return response.text
    except ImportError:
        import google.generativeai as genai_legacy
        genai_legacy.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))
        model = genai_legacy.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt, generation_config={"temperature": 0.0})
        return response.text

def analyze_ranking(text, target):
    """
    Basic GEO analysis:
    - Checks if the target is mentioned.
    - Counts how many times it appears.
    - Finds the approximate position in the response (first mention index).
    """
    matches = list(re.finditer(re.escape(target), text, re.IGNORECASE))
    count = len(matches)
    mentioned = count > 0
    first_mention_index = matches[0].start() if mentioned else -1
    
    return {
        "mentioned": mentioned,
        "mention_count": count,
        "first_mention_index": first_mention_index
    }

def main():
    parser = argparse.ArgumentParser(description="Baseline GEO Ranking Tracker")
    parser.add_argument("--query", required=True, help="The prompt/query to ask the models")
    parser.add_argument("--target", required=True, help="The target website or concept to track")
    parser.add_argument("--output", default="geo_results.json", help="Output JSON file for results")
    args = parser.parse_args()

    results = {
        "query": args.query,
        "target": args.target,
        "engines": {}
    }

    engines = {
        "OpenAI (GPT-4o)": query_openai,
        "Anthropic (Claude 3.7)": query_anthropic,
        "Google (Gemini)": query_gemini
    }

    for name, func in engines.items():
        print(f"Querying {name}...")
        try:
            output_text = func(args.query)
            analysis = analyze_ranking(output_text, args.target)
            results["engines"][name] = {
                "success": True,
                "analysis": analysis,
                "raw_output": output_text
            }
            print(f"  -> Mentioned: {analysis['mentioned']} | Count: {analysis['mention_count']} | First Index: {analysis['first_mention_index']}")
        except Exception as e:
            print(f"  -> Error: {e}")
            results["engines"][name] = {
                "success": False,
                "error": str(e)
            }

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
