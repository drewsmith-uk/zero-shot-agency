import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

env_path = os.path.expanduser("~/.hermes/.env")
load_dotenv(env_path)
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("OPENROUTER_API_KEY not found")
    sys.exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

with open("ef_geo_audit.md", "r") as f:
    doc = f.read()

print(f"Sending to openai/gpt-5.5-pro...")
try:
    response = client.chat.completions.create(
        model="openai/gpt-5.5-pro",
        messages=[
            {"role": "system", "content": "You are an expert technical and SEO copywriter and AI agent auditor."},
            {"role": "user", "content": f"Please critique the following document and provide actionable suggestions for improvement. Keep the suggestions concise and highly actionable:\\n\\n{doc}"}
        ]
    )
    print("\n--- CRITIQUE ---\n")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
