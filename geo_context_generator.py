#!/usr/bin/env python3
import argparse
import os
import sys

GEO_RULESET = """# GEO Ruleset (Generative Engine Optimization)

1. **BOT-NATIVE ARCHITECTURE (SEMANTIC HTML)**: Never use a generic div/span when a semantic HTML5 element exists. Apply Schema microdata. *(Rationale: Prevents text-chunking errors during LLM scraping).*
2. **HIGH-DENSITY INFORMATION (EMPIRICAL BIAS)**: Eliminate corporate jargon/fluff. Replace qualitative claims with quantitative empirical data. *(Rationale: Boosts RAG cosine-similarity scores).*
3. **QUOTATION ADDITION**: Embed direct, attributed quotations from high-authority sources in technical content. *(Rationale: Mathematically reduces LLM generation effort, boosting citation probability).*
4. **MACHINE-READABLE SYNCING**: Format documentation for raw markdown extraction compatible with `llms.txt`. *(Rationale: Frictionless ingestion for AI crawlers).*
5. **STRUCTURAL FLUENCY**: Default to tables, definition lists, and bullets over long paragraphs. *(Rationale: Preserves entity relationships during tokenization).*
"""

FILES_TO_CREATE = [
    ".cursorrules",
    ".clinerules",
    "claude.md",
    "AGENTS.md"
]

def main():
    parser = argparse.ArgumentParser(description="Universal GEO Context Generator")
    parser.add_argument("target_dir", help="Target directory to generate GEO context files")
    args = parser.parse_args()

    target_dir = args.target_dir

    if not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir)
            print(f"Created target directory: {target_dir}")
        except Exception as e:
            print(f"Error creating directory {target_dir}: {e}", file=sys.stderr)
            sys.exit(1)

    for filename in FILES_TO_CREATE:
        filepath = os.path.join(target_dir, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(GEO_RULESET)
            print(f"Successfully generated: {filepath}")
        except Exception as e:
            print(f"Error writing to {filepath}: {e}", file=sys.stderr)
            
    print(f"\nCompleted! Generated GEO context files in: {target_dir}")

if __name__ == "__main__":
    main()
