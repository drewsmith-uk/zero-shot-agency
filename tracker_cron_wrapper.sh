#!/bin/bash
set -e

# Change to the workspace directory
WORKSPACE="/home/claw/workspace/zero-shot-agency"
cd "$WORKSPACE"

# Load environment variables if necessary (API keys)
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
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

# Execute leaderboard generation
echo "Running generate_leaderboard.py at $(date)"
python3 generate_leaderboard.py

# Ensure we are on the tracker data branch
git checkout -B data/tracker

# Auto-commit the results
git add raw/tracker_history/ citations.csv docs/leaderboard.md
git commit -m "chore(tracker): auto-commit tracker results and leaderboard for ${TIMESTAMP}"
git push origin data/tracker
echo "Tracker execution and commit completed successfully."
