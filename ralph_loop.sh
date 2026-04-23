#!/bin/bash
# The Ralph Loop for the GEO Wiki

WIKI_DIR="$HOME/workspace/zero-shot-agency"
TASKS_FILE="$WIKI_DIR/TASKS.md"
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

    # 2. Parse next task
    NEXT_TASK=$(grep -m 1 "^- \[ \]" "$TASKS_FILE")
    
    if [ -z "$NEXT_TASK" ]; then
        echo "✅ No more tasks in the backlog. Ralph is going to sleep."
        break
    fi
    
    # Clean up the string to pass to the agent
    TASK_DESC=$(echo "$NEXT_TASK" | sed 's/^- \[ \] //')
    echo "🎯 Next objective: $TASK_DESC"
    
    # 3. Boot fresh agent instance
    echo "🧠 Booting fresh agent context..."
    hermes chat --yolo -Q -q "You are the GEO Wiki Orchestrator running inside a Ralph Loop. \nORIENT YOURSELF: Read $WIKI_DIR/strategy.md, $WIKI_DIR/SCHEMA.md, index.md, and log.md.\nYOUR TASK: $TASK_DESC\nRULES:\n1. If the task requires deep coding/development, use delegate_task with acp_command='claude' (DO NOT USE legacy 3.5 models).\n2. Content Drafts: Checkout a new branch (e.g., drafts/[name]), write the file, update TASKS.md, and then use /home/linuxbrew/.linuxbrew/bin/gh pr create --fill to open a Pull Request.\n3. If the task is scraping, use your native web_search/web_extract tools and save to raw/.\n4. If it is synthesis, do it yourself and save to concepts/.\n5. Once completed, edit $TASKS_FILE to move the task from the Backlog to Completed.\n6. Update log.md and cross-reference with [[wikilinks]].\nExecute now."

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
