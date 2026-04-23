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
        content = (WIKI_DIR / "TASKS.md").read_text()
        lines = [line for line in content.split('\n') if line.strip().startswith('- [')]
        return "\n".join(lines)
    except:
        return "No tasks found."

def get_logs():
    try:
        content = (WIKI_DIR / "log.md").read_text()
        lines = [line for line in content.split('\n') if line.strip().startswith('##') or line.strip().startswith('-')]
        return "\n".join(lines[-15:])
    except:
        return "No logs found."

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
    .started { background: green; }
    .stopped { background: red; }
    .active-proc { color: lime; text-style: bold; }
    .dead-proc { color: red; text-style: bold; }
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
            yield Static("Status: UNKNOWN", id="status-indicator", classes="stopped")
            yield Static("PROCESS: CHECKING", id="process-indicator", classes="dead-proc")
        yield Footer()

    def on_mount(self) -> None:
        self.update_content()
        self.set_interval(1.0, self.update_content)

    def update_content(self) -> None:
        # Update Tasks
        self.query_one("#tasks-panel", Static).update(f"[bold cyan]📋 Task Ledger[/bold cyan]\n\n{get_tasks()}")
        
        # Update Logs
        self.query_one("#logs-panel", Static).update(f"[bold green]📖 Recent Wiki Logs[/bold green]\n\n{get_logs()}")
        
        # Update Agent Output
        try:
            log_file = WIKI_DIR / "latest_agent.log"
            if log_file.exists() and log_file.stat().st_size > 0:
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    clean_text = clean_ansi("".join(lines[-20:]))
                    self.query_one("#agent-panel", Static).update(f"[bold yellow]⚡ Live Agent Output[/bold yellow]\n\n{clean_text}")
            else:
                self.query_one("#agent-panel", Static).update("[bold yellow]⚡ Live Agent Output[/bold yellow]\n\nWaiting for agent...")
        except Exception as e:
            pass

        # Update State Text File Indicator
        state = read_state()
        status_widget = self.query_one("#status-indicator", Static)
        status_widget.update(f" State: {state} ")
        if state == "RUNNING":
            status_widget.classes = "started"
        else:
            status_widget.classes = "stopped"
            
        # Update Actual OS Process Indicator
        is_running = is_process_running()
        proc_widget = self.query_one("#process-indicator", Static)
        if is_running:
            proc_widget.update(" | ⚙ PROCESS: ALIVE")
            proc_widget.classes = "active-proc"
        else:
            proc_widget.update(" | 💀 PROCESS: DEAD")
            proc_widget.classes = "dead-proc"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_start":
            subprocess.run([f"{WIKI_DIR}/ralph-control.sh", "start"])
        elif event.button.id == "btn_pause":
            subprocess.run([f"{WIKI_DIR}/ralph-control.sh", "stop"])
        elif event.button.id == "btn_launch":
            # Launch the loop in the background, detached
            subprocess.Popen([f"{WIKI_DIR}/ralph_loop.sh"], cwd=WIKI_DIR, 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           start_new_session=True)
        self.update_content()

if __name__ == "__main__":
    app = RalphDashboard()
    app.run()
