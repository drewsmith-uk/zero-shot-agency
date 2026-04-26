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
    echo "🎯 Next objective: #$NEXT_TASK_ID - $NEXT_TASK_DESC"
    
    # 3. Boot fresh agent instance
    echo "🧠 Booting fresh agent context..."
    hermes chat --yolo -Q -q "You are the GEO Wiki Orchestrator running inside a Ralph Loop. \nORIENT YOURSELF: Read $WIKI_DIR/strategy.md, $WIKI_DIR/SCHEMA.md, index.md, and log.md.\nYOUR TASK: Resolve GitHub Issue #$NEXT_TASK_ID ($NEXT_TASK_URL).\nRULES:\n1. If the task requires deep coding/development, use delegate_task with acp_command='claude' (DO NOT USE legacy 3.5 models).\n2. Content Drafts: Checkout a new branch (e.g., drafts/[name]), write the file, update mkdocs.yml navigation, use gh CLI to close the issue, and then use gh pr create --fill to open a Pull Request.\n3. If the task is scraping, use your native web_search/web_extract tools and save to raw/.\n4. If it is synthesis, do it yourself and save to concepts/.\n5. Once completed, use the gh CLI to close the issue (#$NEXT_TASK_ID).\n6. Update log.md and cross-reference pages using standard [[wikilinks]] format (do NOT wrap them in backticks).\nExecute now."

    # 4. Agent exits. Increment and cool down.
    
    # 4.5 Auto-Commit to GitHub
    echo "📦 Committing progress to Git..."
    cd "$WIKI_DIR" || exit
    git add .
    git commit -m "Ralph Auto-Commit: Completed $TASK_DESC" || true
    CURRENT_BRANCH=$(git branch --show-current)
    git push origin "$CURRENT_BRANCH"
    
    tasks_completed=$((tasks_completed + 1))
    
    if [ $tasks_completed -lt $MAX_TASKS ]; then
        echo "⏳ Cooling down for 60 seconds before next iteration..."
        sleep 60
    fi
done

echo "🏁 Ralph Loop shift finished. Completed $tasks_completed tasks."
