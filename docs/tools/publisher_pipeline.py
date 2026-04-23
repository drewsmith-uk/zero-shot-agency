#!/usr/bin/env python3
import sys
import os
import subprocess
import json
import re
import shutil
import argparse

def check_tools():
    missing = []
    for tool in ['git', 'x-cli', 'himalaya']:
        if not shutil.which(tool):
            missing.append(tool)
    if missing:
        print(f"Error: Required tools missing: {', '.join(missing)}")
        sys.exit(1)

def extract_title_and_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        sys.exit(1)
        
    title = None
    
    # Try to find YAML frontmatter title
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        body = frontmatter_match.group(2)
        
        # Look for title: "Something" or title: Something
        title_match = re.search(r'^title:\s*"?([^"\n]+)"?', frontmatter, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
    else:
        body = content
        
    if not title:
        # Look for first H1
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
            
    if not title:
        title = os.path.basename(filepath)
        
    return title, body, content

def git_push(filepath, title):
    print("Git: Adding, committing and pushing...")
    try:
        subprocess.run(['git', 'add', filepath], check=True)
        commit_msg = f"Publish: {title}"
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("Git push successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")
        sys.exit(1)

def split_for_twitter(text):
    chunks = []
    # Split by paragraphs
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
    
    current_chunk = ""
    for p in paragraphs:
        # If adding the paragraph exceeds 275 characters, start a new chunk
        if len(current_chunk) + len(p) + 2 <= 275:
            if current_chunk:
                current_chunk += "\n\n" + p
            else:
                current_chunk = p
        else:
            if current_chunk:
                chunks.append(current_chunk)
            
            # If the single paragraph itself is too long, we split by words
            if len(p) > 275:
                words = p.split()
                temp_chunk = ""
                for w in words:
                    if len(temp_chunk) + len(w) + 1 <= 275:
                        if temp_chunk:
                            temp_chunk += " " + w
                        else:
                            temp_chunk = w
                    else:
                        chunks.append(temp_chunk)
                        temp_chunk = w
                if temp_chunk:
                    current_chunk = temp_chunk
            else:
                current_chunk = p
    if current_chunk:
        chunks.append(current_chunk)
        
    return chunks

def post_to_twitter(chunks):
    if not chunks:
        return
        
    print(f"Twitter: Posting thread with {len(chunks)} tweets...")
    previous_id = None
    
    for i, chunk in enumerate(chunks):
        cmd = ['x-cli', '-j', 'tweet']
        if previous_id:
            cmd.extend(['reply', previous_id, chunk])
        else:
            cmd.extend(['post', chunk])
            
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            try:
                data = json.loads(result.stdout)
                tweet_id = data.get('id')
                if not tweet_id:
                    print(f"Warning: Could not parse tweet ID from output: {result.stdout}")
                    break
                previous_id = str(tweet_id)
                print(f"Posted tweet {i+1}/{len(chunks)}: ID {tweet_id}")
            except json.JSONDecodeError:
                print(f"Error decoding JSON from x-cli: {result.stdout}")
                break
        except subprocess.CalledProcessError as e:
            print(f"Error posting to twitter: {e.stderr or e.stdout}")
            break
            
def send_substack(title, content):
    email = os.environ.get('SUBSTACK_EMAIL')
    if not email:
        print("Warning: SUBSTACK_EMAIL environment variable not set. Skipping Substack email.")
        return
        
    print(f"Substack: Sending email to {email}...")
    email_template = f"To: {email}\nSubject: {title}\n\n{content}\n"
    
    try:
        process = subprocess.Popen(
            ['himalaya', 'template', 'send'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=email_template)
        
        if process.returncode != 0:
            print(f"Error sending Substack email: {stderr}")
        else:
            print("Substack email sent successfully.")
    except Exception as e:
        print(f"Error invoking himalaya: {e}")

def main():
    parser = argparse.ArgumentParser(description="Publish a markdown draft to Git, Twitter, and Substack.")
    parser.add_argument('filepath', help='Path to the markdown file')
    args = parser.parse_args()
    
    check_tools()
    
    filepath = args.filepath
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
        
    title, body, raw_content = extract_title_and_content(filepath)
    print(f"Found title: {title}")
    
    # 1. Git push
    git_push(filepath, title)
    
    # 2. Twitter thread
    chunks = split_for_twitter(body)
    post_to_twitter(chunks)
    
    # 3. Substack email
    send_substack(title, raw_content)
    
    print("Publishing pipeline completed.")

if __name__ == '__main__':
    main()
