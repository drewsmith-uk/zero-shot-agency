import re

with open('geo-tracker.py', 'r') as f:
    code = f.read()

# Instead of using the dictionary keys (like 'openai_best') for the CSV headers,
# we want to use the actual model slugs (like 'gpt-5.5-pro' or 'openai/gpt-5.5-pro')

# Replace fieldnames assignment
code = re.sub(
    r'fieldnames = \["query"\] \+ \[f"\{k\}_mentioned" for k in MODELS\]',
    'fieldnames = ["query"] + [f"{model_id.split(\'/\')[-1]}_mentioned" for model_id in MODELS.values()]',
    code
)

# Replace loop initialization for row
code = re.sub(
    r'for k in MODELS:\n\s+row\[f"\{k\}_mentioned"\] = False',
    'for model_id in MODELS.values():\n            row[f"{model_id.split(\'/\')[-1]}_mentioned"] = False',
    code
)

# Replace the inner query loop variable tracking
code = re.sub(
    r'row\[f"\{model_key\}_mentioned"\] = mentioned',
    'row[f"{model_id.split(\'/\')[-1]}_mentioned"] = mentioned',
    code
)

with open('geo-tracker.py', 'w') as f:
    f.write(code)
