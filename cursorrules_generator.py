#!/usr/bin/env python3
import argparse
import sys
import os

def generate_cursorrules(project_name, tech_stack, role, custom_instructions):
    tech_stack_list = [t.strip() for t in tech_stack.split(',')] if tech_stack else []
    tech_stack_str = ", ".join(tech_stack_list) if tech_stack_list else "Not specified"

    # GEO (Generative Engine Optimization) Context Structuring
    # Focusing on clear roles, specific instructions, constraints, and structured output formatting.
    rules_content = f"""# .cursorrules - {project_name}

## 1. System Role & Persona
You are an expert `{role}`. You provide high-quality, production-ready code, and insightful technical guidance.
Always adhere to best practices for the following technologies: {tech_stack_str}.

## 2. Project Context
- **Project Name**: {project_name}
- **Tech Stack**: {tech_stack_str}

## 3. Generative Engine Optimization (GEO) Guidelines
To ensure optimal context ingestion and high-quality responses, follow these constraints strictly:
- **Directness**: Be concise and direct. Omit pleasantries, filler words, and unnecessary narration.
- **Action-Oriented**: Focus on actionable solutions. When asked for code, provide the code first, followed by a brief explanation only if necessary.
- **Formatting**: Use markdown formatting systematically:
  - `Bold` for emphasis and key terms.
  - `Code blocks` with correct language tags for all code snippets.
  - `Lists` for step-by-step procedures.
- **Verification**: Before executing complex solutions, briefly state your understanding of the core requirement to align context.
- **Epistemic Humility**: If you lack context or certainty, explicitly state "I need more information about [X]" instead of guessing.

## 4. Coding Standards & Constraints
- Write clean, maintainable, and well-documented code.
- Follow idiomatic naming conventions for {tech_stack_str}.
- Include error handling and edge-case consideration in all code snippets.
- Keep functions small and focused on a single responsibility (Single Responsibility Principle).
- Avoid deprecated APIs; use modern syntax and patterns.

## 5. Output Format Requirements
When providing modifications to existing files:
- Clearly indicate the absolute file path.
- Provide targeted diffs or clearly show the `before` and `after` states.
- Do not output the entire file unless specifically requested.

## 6. Custom Instructions
{custom_instructions if custom_instructions else "None specified."}
"""
    return rules_content

def main():
    parser = argparse.ArgumentParser(
        description="Generate an optimized .cursorrules file using GEO context structuring.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-p", "--project-name", type=str, default="My Project", help="Name of the project")
    parser.add_argument("-t", "--tech-stack", type=str, default="Python, Shell", help="Comma-separated list of technologies used")
    parser.add_argument("-r", "--role", type=str, default="Senior Software Engineer", help="Role persona for the LLM")
    parser.add_argument("-c", "--custom-instructions", type=str, default="", help="Any project-specific custom instructions")
    parser.add_argument("-o", "--output", type=str, default=".cursorrules", help="Output file path")

    args = parser.parse_args()

    content = generate_cursorrules(
        args.project_name, 
        args.tech_stack, 
        args.role,
        args.custom_instructions
    )

    output_path = os.path.abspath(args.output)
    
    try:
        with open(output_path, "w") as f:
            f.write(content)
        print(f"Successfully generated optimized .cursorrules at: {output_path}")
        print("Incorporated Generative Engine Optimization (GEO) principles: System Role, Constraints, and Formatting rules.")
    except Exception as e:
        print(f"Error writing to file {output_path}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
