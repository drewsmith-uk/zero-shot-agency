#!/usr/bin/env python3
import os
import time
import subprocess
from pathlib import Path
import re
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Header, Footer, Static, Button, RichLog
from textual.reactive import reactive
from textual.events import Resize

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
    #main-scroll {
        width: 100%;
        height: 1fr;
    }
    #top-row {
        height: auto;
        layout: horizontal;
    }
    #tasks-panel, #logs-panel {
        width: 50%;
        height: auto;
        min-height: 12;
        border: solid green;
        padding: 1;
    }
    #agent-panel {
        height: auto;
        min-height: 12;
        border: solid yellow;
        padding: 1;
    }
    #controls {
        height: auto;
        border: solid blue;
        layout: horizontal;
        align: center middle;
        padding: 1;
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

    /* Mobile / Narrow Screen Overrides */
    Screen.narrow #top-row {
        layout: vertical;
    }
    Screen.narrow #tasks-panel, Screen.narrow #logs-panel {
        width: 100%;
        height: auto;
        min-height: 10;
    }
    Screen.narrow #controls {
        layout: vertical;
        align: center middle;
    }
    Screen.narrow Button {
        width: 100%;
        margin: 1 0;
        padding: 1 0;
    }
    Screen.narrow #status-indicator {
        width: 100%;
        margin: 1 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="main-scroll"):
            with Horizontal(id="top-row"):
                yield Static("Loading Tasks...", id="tasks-panel")
                yield Static("Loading Logs...", id="logs-panel")
            yield Static("Loading Agent Output...", id="agent-panel")
            with Horizontal(id="controls"):
                yield Static("Loading Status...", id="status-indicator")
                yield Button("Set RUNNING", id="btn_start", variant="success")
                yield Button("Set PAUSED", id="btn_pause", variant="warning")
                yield Button("▶ LAUNCH SCRIPT", id="btn_launch", variant="primary")
        yield Footer()

    def on_mount(self) -> None:
        self.update_content()
        self.set_interval(0.5, self.update_content)

    def on_resize(self, event: Resize) -> None:
        if event.size.width < 75:
            self.screen.add_class("narrow")
        else:
            self.screen.remove_class("narrow")

    def update_content(self) -> None:
        self.query_one("#tasks-panel", Static).update(f"[bold cyan]📋 Task Ledger[/bold cyan]\n\n{get_tasks()}")
        self.query_one("#logs-panel", Static).update(f"[bold green]📖 Recent Wiki Logs[/bold green]\n\n{get_logs()}")
        
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

        state = read_state()
        is_running = is_process_running()
        state_fmt = f"[black on green] {state} [/]" if state == "RUNNING" else f"[white on red] {state} [/]"
        
        try:
            log_content = ""
            if LOG_FILE.exists():
                with open(LOG_FILE, 'r') as f:
                    log_content = f.read()
                    
            if is_running:
                proc_fmt = "[bold lime]⚙ ACTIVE[/]"
            elif "Ralph is going to sleep" in log_content[-200:]:
                proc_fmt = "[bold yellow]💤 SLEEPING[/]"
            elif "shift finished" in log_content[-200:]:
                proc_fmt = "[bold cyan]🏁 FINISHED[/]"
            else:
                proc_fmt = "[bold red]💀 DEAD / CRASHED[/]"
        except:
             proc_fmt = "[bold red]💀 DEAD[/]" if not is_running else "[bold lime]⚙ ACTIVE[/]"
        
        self.query_one("#status-indicator", Static).update(f"State: {state_fmt} | Loop: {proc_fmt}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_start":
            subprocess.run([f"{WIKI_DIR}/ralph-control.sh", "start"])
        elif event.button.id == "btn_pause":
            subprocess.run([f"{WIKI_DIR}/ralph-control.sh", "stop"])
        elif event.button.id == "btn_launch":
            with open(LOG_FILE, 'w') as f:
                f.write("System: Launching Ralph Loop...\n")
            subprocess.Popen([f"{WIKI_DIR}/ralph_loop.sh"], cwd=WIKI_DIR, 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           start_new_session=True)
        self.update_content()

if __name__ == "__main__":
    app = RalphDashboard()
    app.run()
