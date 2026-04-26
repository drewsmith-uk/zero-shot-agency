import csv
import os
import datetime

def generate_leaderboard(csv_path="citations.csv", output_path="docs/leaderboard.md"):
    if not os.path.exists(csv_path):
        print(f"Error: Could not find {csv_path}. Please ensure citations.csv exists.")
        return

    # Create docs dir if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    counts = {}
    total_queries = 0
    models = []

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Find model columns
            if not reader.fieldnames:
                print("Error: citations.csv is empty or missing headers.")
                return
            
            for field in reader.fieldnames:
                if field.endswith('_mentioned'):
                    model_name = field.replace('_mentioned', '')
                    models.append(model_name)
                    counts[model_name] = 0
            
            for row in reader:
                total_queries += 1
                for model in models:
                    field_name = f"{model}_mentioned"
                    val = row.get(field_name, "").strip().lower()
                    if val == "true":
                        counts[model] += 1
                        
    except Exception as e:
        print(f"Error reading {csv_path}: {e}")
        return

    if total_queries == 0:
        print("Warning: No queries found in citations.csv.")
        total_queries = 1  # Avoid division by zero, though stats will be 0

    # Calculate SOV and sort by SOV descending
    results = []
    for model in models:
        mentions = counts[model]
        sov = (mentions / total_queries) * 100 if total_queries > 0 else 0
        results.append((model, mentions, sov))
    
    results.sort(key=lambda x: x[2], reverse=True)

    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Generate Markdown
    md_lines = []
    md_lines.append("---")
    md_lines.append("title: GEO Leaderboard")
    md_lines.append(f"created: {date_str}")
    md_lines.append("type: concept")
    md_lines.append("tags: [geo-tracker, leaderboard]")
    md_lines.append("---\n")
    
    md_lines.append("# Prompt Share of Voice Leaderboard\n")
    md_lines.append("This leaderboard tracks the Prompt Share of Voice (SOV) for various AI models based on generative engine optimization results. The SOV percentage represents how often a model was mentioned across all tracked queries.\n")
    
    md_lines.append(f"**Total Queries Evaluated:** {total_queries}\n")
    
    md_lines.append("| Rank | Model | Mentions | Prompt SOV |")
    md_lines.append("|------|-------|----------|------------|")
    
    for idx, (model, mentions, sov) in enumerate(results, 1):
        md_lines.append(f"| {idx} | {model} | {mentions} | {sov:.1f}% |")
        
    md_lines.append("\n---")
    md_lines.append(f"*Last Updated: {timestamp_str}*")

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_lines) + "\n")
        print(f"Successfully generated {output_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")

if __name__ == "__main__":
    generate_leaderboard()
