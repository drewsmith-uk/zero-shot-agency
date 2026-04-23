#!/bin/bash
# Ralph Loop Control Script

WORK_DIR="$HOME/workspace/zero-shot-agency"
STATE_FILE="$WORK_DIR/run-state.txt"

function show_help() {
    echo "Usage: ./ralph-control.sh [start|stop|status]"
    echo ""
    echo "Commands:"
    echo "  start   - Sets state to RUNNING to allow the Ralph loop to execute."
    echo "  stop    - Sets state to PAUSED to safely halt the Ralph loop."
    echo "  status  - Displays the current run state."
}

case "$1" in
    start|play|run)
        echo "RUNNING" > "$STATE_FILE"
        echo "✅ Ralph Loop state set to: RUNNING"
        ;;
    stop|pause|halt)
        echo "PAUSED" > "$STATE_FILE"
        echo "🛑 Ralph Loop state set to: PAUSED"
        ;;
    status)
        if [ -f "$STATE_FILE" ]; then
            STATE=$(cat "$STATE_FILE" | xargs)
            echo "Current Ralph Loop State: $STATE"
        else
            echo "State file not found at $STATE_FILE (defaulting to PAUSED)"
        fi
        ;;
    *)
        show_help
        ;;
esac
