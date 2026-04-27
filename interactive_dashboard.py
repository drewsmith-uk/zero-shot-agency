#!/usr/bin/env python3
import os
import time
import subprocess
from pathlib import Path
import re
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Button, RichLog
from textual.reactive import reactive

WIKI_DIR = Path(os.path.expanduser("~/workspace/zero-shot-agency"))
STATE_FILE = WIKI_DIR / "run-state.txt"
LOG_FILE = WIKI_DIR / "latest_agent.log"

def read_state():
    if STATE_FILE.exists():
        return STATE_FILE.read_text().strip()
    return "UNKNOWN"

def is_process_running():
    try:
        # Check if ralph_loop.sh is running using ps
        result = subprocess.run(['pgrep', '-f', 'ralph_loop.sh'], capture_output=True, text=True)
        return bool(result.stdout.strip())
    except Exception:
        return False

def get_tasks():
    try:
        import subprocess
        result = subprocess.run(
            ["gh", "issue", "list", "--state", "open", "--limit", "10"],
            cwd=str(WIKI_DIR), capture_output=True, text=True, check=True
        )
        if not result.stdout.strip():
            return "No open issues found."
        return result.stdout.strip()
    except Exception as e:
        return f"Error loading issues: {e}"

def get_logs():
    try:
        entries_dir = WIKI_DIR / "docs" / "logs" / "entries"
        if not entries_dir.exists():
            return "No logs found."
        
        # Grab the 3 most recently created log files
        files = sorted(entries_dir.glob("*.md"), reverse=True)[:3]
        if not files:
            return "No logs found."
            
        logs = []
        for f in files:
            # Add the filename as a mini-header
            header = f"[bold cyan]{f.stem}[/bold cyan]"
            logs.append(f"{header}
{f.read_text().strip()}")
            
        return "

".join(logs)
    except Exception as e:
        return f"Error loading logs: {e}"

def clean_ansi(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text).replace('\r', '')

class RalphDashboard(App):
    CSS = """
    Screen {
        layout: vertical;
    }
    #top-row {
        height: 45%;
        layout: horizontal;
    }
    #tasks-panel, #logs-panel {
        width: 50%;
        height: 100%;
        border: solid green;
        padding: 1;
    }
    #agent-panel {
        height: 40%;
        border: solid yellow;
        padding: 1;
    }
    #controls {
        height: 15%;
        border: solid blue;
        layout: horizontal;
        align: center middle;
    }
    Button {
        margin: 1 2;
    }
    #status-indicator {
        width: auto;
        margin: 1 2;
        content-align: center middle;
        padding: 1 2;
        border: solid white;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="top-row"):
            yield Static("Loading Tasks...", id="tasks-panel")
            yield Static("Loading Logs...", id="logs-panel")
        yield Static("Loading Agent Output...", id="agent-panel")
        with Horizontal(id="controls"):
            yield Button("Set RUNNING", id="btn_start", variant="success")
            yield Button("Set PAUSED", id="btn_pause", variant="warning")
            yield Button("▶ LAUNCH SCRIPT", id="btn_launch", variant="primary")
            yield Static("Loading Status...", id="status-indicator")
        yield Footer()

    def on_mount(self) -> None:
        self.update_content()
        self.set_interval(0.5, self.update_content)  # Fast refresh for responsiveness

    def update_content(self) -> None:
        # Update Tasks
        self.query_one("#tasks-panel", Static).update(f"[bold cyan]📋 Task Ledger[/bold cyan]\n\n{get_tasks()}")
        
        # Update Logs
        self.query_one("#logs-panel", Static).update(f"[bold green]📖 Recent Wiki Logs[/bold green]\n\n{get_logs()}")
        
        # Update Agent Output
        try:
            if LOG_FILE.exists() and LOG_FILE.stat().st_size > 0:
                with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    clean_text = clean_ansi("".join(lines[-20:]))
                    self.query_one("#agent-panel", Static).update(f"[bold yellow]⚡ Live Agent Output[/bold yellow]\n\n{clean_text}")
            else:
                self.query_one("#agent-panel", Static).update("[bold yellow]⚡ Live Agent Output[/bold yellow]\n\nWaiting for agent...")
        except Exception as e:
            pass

        # Update Combined Status Indicator
        state = read_state()
        is_running = is_process_running()
        
        state_fmt = f"[black on green] {state} [/]" if state == "RUNNING" else f"[white on red] {state} [/]"
        
        # Add intelligence to the process indicator
        try:
            log_content = ""
            if LOG_FILE.exists():
                with open(LOG_FILE, 'r') as f:
                    log_content = f.read()
                    
            if is_running:
                proc_fmt = "[bold lime]⚙ ACTIVE[/]"
            elif "Ralph is going to sleep" in log_content[-200:] or "shift finished" in log_content[-200:]:
                proc_fmt = "[bold cyan]⏹ STOPPED (READY TO LAUNCH)[/]"
            else:
                proc_fmt = "[bold red]💀 DEAD / CRASHED[/]"
        except:
             proc_fmt = "[bold red]💀 DEAD[/]" if not is_running else "[bold lime]⚙ ACTIVE[/]"
        
        self.query_one("#status-indicator", Static).update(f"File State: {state_fmt}  |  Loop: {proc_fmt}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_start":
            subprocess.run([f"{WIKI_DIR}/ralph-control.sh", "start"])
        elif event.button.id == "btn_pause":
            subprocess.run([f"{WIKI_DIR}/ralph-control.sh", "stop"])
        elif event.button.id == "btn_launch":
            # Clear the log file so we can see the fresh run
            with open(LOG_FILE, 'w') as f:
                f.write("System: Launching Ralph Loop...\n")
            
            # Launch the loop in the background, detached
            subprocess.Popen([f"{WIKI_DIR}/ralph_loop.sh"], cwd=WIKI_DIR, 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           start_new_session=True)
        self.update_content()

if __name__ == "__main__":
    app = RalphDashboard()
    app.run()
