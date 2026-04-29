import os
import glob

def on_pre_build(config, **kwargs):
    entries_dir = os.path.join(config['docs_dir'], 'logs', 'entries')
    out_file = os.path.join(config['docs_dir'], 'activity-log.md')
    
    if not os.path.exists(entries_dir):
        return
        
    files = sorted(glob.glob(os.path.join(entries_dir, '*.md')), reverse=True)
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write("---\ntitle: Agency Activity Log\n---\n\n# Agency Activity Log\n\n")
        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as entry:
                f.write(entry.read().strip() + "\n\n---\n\n")
