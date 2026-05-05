#!/bin/bash
# The Ralph Loop for the GEO Wiki

WIKI_DIR="$HOME/workspace/zero-shot-agency"
STATE_FILE="$WIKI_DIR/run-state.txt"
LOG_FILE="$WIKI_DIR/latest_agent.log"
MAX_TASKS=5

# Send all output of this script to the log file so the dashboard can read it
exec >> "$LOG_FILE" 2>&1

# Initialize state file
if [ ! -f "$STATE_FILE" ]; then
    echo "RUNNING" > "$STATE_FILE"
fi

next_blog_date() {
    python3 - <<'PY'
import datetime as dt
import json
import re
import subprocess
from pathlib import Path

repo = Path.cwd()
date_re = re.compile(r"^date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", re.MULTILINE)
dates = []

for post in (repo / "docs/blog/posts").glob("*.md"):
    match = date_re.search(post.read_text(encoding="utf-8", errors="ignore"))
    if match:
        dates.append(dt.date.fromisoformat(match.group(1)))

try:
    prs_json = subprocess.check_output(
        ["gh", "pr", "list", "--state", "open", "--json", "number"],
        text=True,
        stderr=subprocess.DEVNULL,
    )
    prs = json.loads(prs_json)
except Exception:
    prs = []

for pr in prs:
    number = str(pr.get("number", ""))
    if not number:
        continue
    try:
        diff = subprocess.check_output(
            ["gh", "pr", "diff", number, "--patch"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        continue

    in_blog_post = False
    for line in diff.splitlines():
        if line.startswith("diff --git "):
            in_blog_post = "docs/blog/posts/" in line and line.endswith(".md")
            continue
        if not in_blog_post or not line.startswith("+") or line.startswith("+++"):
            continue
        match = date_re.match(line[1:])
        if match:
            dates.append(dt.date.fromisoformat(match.group(1)))

base = max(dates) if dates else dt.date.today()
print((base + dt.timedelta(days=1)).isoformat())
PY
}

echo "🚀 Starting GEO Wiki Ralph Loop..."
echo "To pause, echo 'PAUSED' > $STATE_FILE"

tasks_completed=0

while [ $tasks_completed -lt $MAX_TASKS ]; do
    # 1. Check Kill Switch
    STATE=$(cat "$STATE_FILE" | xargs)
    if [ "$STATE" != "RUNNING" ]; then
        echo "🛑 Loop paused via state file ($STATE). Exiting."
        break
    fi

    # 2. Parse next task from GitHub Issues
    # Always reset to a clean main branch before starting a new task
    cd "$WIKI_DIR" || exit
    git checkout main
    git pull origin main

    export PATH="/home/claw/.local/bin:/home/linuxbrew/.linuxbrew/bin:$PATH"
    NEXT_TASK_ID=$(gh issue list --state open --json number --jq '.[0].number' 2>/dev/null)

    if [ -z "$NEXT_TASK_ID" ]; then
        echo "✅ No open GitHub Issues found. Ralph is going to sleep."
        break
    fi

    NEXT_TASK_DESC=$(gh issue view "$NEXT_TASK_ID" --json title --jq '.title' 2>/dev/null)
    NEXT_TASK_URL=$(gh issue view "$NEXT_TASK_ID" --json url --jq '.url' 2>/dev/null)
    NEXT_BLOG_DATE=$(next_blog_date)
    LOG_ENTRY_PATH="docs/logs/entries/$(date +%Y-%m-%d)-issue-$NEXT_TASK_ID.md"
    echo "🎯 Next objective: #$NEXT_TASK_ID - $NEXT_TASK_DESC"
    echo "🗓️ Next available blog date: $NEXT_BLOG_DATE"

    PROMPT=$(cat <<EOF
You are the GEO Wiki Orchestrator running inside a Ralph Loop.

ORIENT YOURSELF: Read $WIKI_DIR/strategy.md, $WIKI_DIR/SCHEMA.md, index.md, and log.md.
YOUR TASK: Resolve GitHub Issue #$NEXT_TASK_ID ($NEXT_TASK_URL).

RULES:
1. If the task requires deep coding, planning, or creative work, use delegate_task with acp_command='claude' and acp_args=['--acp', '--stdio', '--model', 'claude-opus-4-7'].
2. Content drafts: check out a new branch such as drafts/[name], write the file, and use gh CLI to close the issue.
3. Daily blog posts must go in docs/blog/posts/ and use date: $NEXT_BLOG_DATE. Do not use today's date unless it is already the day after the newest existing post date. This date was computed from both posts already on the site and dates introduced by open PRs.
4. Before creating a daily blog post, also inspect docs/blog/posts/ and open PRs yourself for existing daily-blog-day-N files. Use the next day number after the highest one you find across main and open PRs.
5. Do not add individual blog posts to mkdocs.yml navigation; the MkDocs blog plugin handles posts under docs/blog/posts/.
6. If the task is scraping, use your native web_search/web_extract tools and save to raw/.
7. If it is synthesis, save the result to the appropriate docs/ subdirectory.
8. Once completed, use the gh CLI to close issue #$NEXT_TASK_ID.
9. Create a new file at $LOG_ENTRY_PATH detailing your actions. Cross-reference pages using [[wikilinks]]. Do not edit any existing log files.
10. Manually stage only the files you created or modified using git add with explicit file paths. Do not use git add . or git add -A. Do not run git commit or git push; the loop script handles commit, push, and PR creation.

Execute now.
EOF
)

    # 3. Boot fresh agent instance
    echo "🧠 Booting fresh agent context..."
    hermes chat --yolo -Q -q "$PROMPT"

    # 4. Agent exits. Increment and cool down.

    # 4.5 Auto-Commit to GitHub
    echo "📦 Committing progress to Git..."
    cd "$WIKI_DIR" || exit

    git commit --author="Molty McClaw <molty@zero-shot.agency>" -m "Ralph Auto-Commit: Completed $NEXT_TASK_DESC" || true
    CURRENT_BRANCH=$(git branch --show-current)
    git push origin "$CURRENT_BRANCH"

    # Auto-create PR if we are on a new branch
    if [ "$CURRENT_BRANCH" != "main" ]; then
        echo "Closes #$NEXT_TASK_ID" > /tmp/pr_body.txt
        gh pr create --title "$NEXT_TASK_DESC" --body-file /tmp/pr_body.txt || true
    fi

    tasks_completed=$((tasks_completed + 1))

    if [ $tasks_completed -lt $MAX_TASKS ]; then
        echo "⏳ Cooling down for 60 seconds before next iteration..."
        sleep 60
    fi
done

echo "🏁 Ralph Loop shift finished. Completed $tasks_completed tasks."
