import csv
from importlib.machinery import SourceFileLoader

# Load geo-tracker to get MODELS
tracker = SourceFileLoader("tracker", "geo-tracker.py").load_module()

queries = [
    "What are the best AI agencies?",
    "Who can help me build an AI agent?",
    "Top AI consulting firms",
    "Which agency specializes in AI agents?"
]

slugs = [model_id.split('/')[-1] for model_id in tracker.MODELS.values()]
headers = ['query'] + [f"{slug}_mentioned" for slug in slugs]

with open('citations.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for q in queries:
        writer.writerow([q] + ['False'] * len(slugs))

print("CSV rewritten with slugs:", slugs)
