from docs.tools.blog_hook import on_config
import yaml
with open("mkdocs.yml") as f:
    config = yaml.safe_load(f)
on_config(config)
for item in config['nav']:
    if 'Blog' in item:
        print(item['Blog'])
