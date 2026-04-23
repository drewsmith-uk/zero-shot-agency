import markdown
html = markdown.markdown("Hello [[World]]!", extensions=['wikilinks'])
print(html)