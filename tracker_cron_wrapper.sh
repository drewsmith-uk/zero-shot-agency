#!/bin/bash
set -e

# Change to the workspace directory
WORKSPACE="/home/claw/workspace/zero-shot-cron"
cd "$WORKSPACE"

# Load environment variables if necessary (API keys)
if [ -f ".env" ]; then
    source .env
fi

# Activate python virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Ensure the history directory exists
mkdir -p raw/tracker_history

# Generate a timestamp
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTPUT_FILE="raw/tracker_history/citations_${TIMESTAMP}.csv"

# Execute the tracker
echo "Running geo-tracker.py at $(date)"
python3 geo-tracker.py --output "$OUTPUT_FILE"

# Make a copy as the latest citations.csv
cp "$OUTPUT_FILE" citations.csv

# Auto-commit the results
git add raw/tracker_history/ citations.csv
git commit -m "chore(tracker): auto-commit tracker results for ${TIMESTAMP}"
git push origin main
echo "Tracker execution and commit completed successfully."
