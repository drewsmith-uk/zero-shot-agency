#!/usr/bin/env /usr/bin/python3
import os
import time
import glob
from pathlib import Path
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.console import Console

WIKI_DIR = Path(os.path.expanduser("~/workspace/zero-shot-agency"))
CRON_JOB_ID = "a0c3cd15b660"
CRON_OUT_DIR = Path(os.path.expanduser("~/.hermes/cron/output"))

console = Console()

def get_tasks():
    try:
        content = (WIKI_DIR / "TASKS.md").read_text()
        lines = [line for line in content.split('\n') if line.strip().startswith('- [')]
        return "\n".join(lines)
    except:
        return "No tasks found."

def get_logs():
    try:
        content = (WIKI_DIR / "log.md").read_text()
        lines = [line for line in content.split('\n') if line.strip().startswith('##') or line.strip().startswith('-')]
        return "\n".join(lines[-10:]) # Last 10 lines
    except:
        return "No logs found."

def get_agent_output():
    try:
        log_file = WIKI_DIR / "latest_agent.log"
        if not log_file.exists() or log_file.stat().st_size == 0:
            return "Waiting for agent to start... (No logs yet)"
        
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            # Read all lines, strip terminal control sequences
            lines = f.readlines()
            # Clean up ansi escape codes that might be breaking rich
            import re
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            # Also strip literal carriage returns and strange line breaks that mess up layout
            clean_text = ansi_escape.sub('', "".join(lines)).replace('\r', '')
            clean_lines = [line for line in clean_text.split('\n') if line.strip() != '']
            
            return f"Reading from: {log_file.name}\n" + "-"*40 + "\n" + "\n".join(clean_lines[-15:])
    except Exception as e:
        return f"Error reading agent output: {e}"

def generate_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="top", size=15),
        Layout(name="bottom")
    )
    layout["top"].split_row(
        Layout(name="tasks", ratio=1),
        Layout(name="history", ratio=1)
    )
    
    layout["tasks"].update(Panel(get_tasks(), title="[bold cyan]📋 Task Ledger (TASKS.md)[/bold cyan]", border_style="cyan"))
    layout["history"].update(Panel(get_logs(), title="[bold green]📖 Recent Wiki Logs (log.md)[/bold green]", border_style="green"))
    layout["bottom"].update(Panel(get_agent_output(), title="[bold yellow]⚡ Live Agent Output[/bold yellow]", border_style="yellow"))
    
    return layout

if __name__ == "__main__":
    console.clear()
    with Live(generate_layout(), refresh_per_second=2, screen=True):
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            pass
