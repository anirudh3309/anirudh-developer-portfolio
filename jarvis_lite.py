"""JARVIS Lite: a local notes and tasks helper; no microphone or API required."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("jarvis_data.json")

def load():
    if DATA.exists():
        try:
            with DATA.open(encoding="utf-8") as f:
                d = json.load(f)
            if isinstance(d, dict):
                return {"notes": d.get("notes", []), "tasks": d.get("tasks", [])}
        except (OSError, json.JSONDecodeError):
            print("Could not read saved data; starting fresh.")
    return {"notes": [], "tasks": []}

def save(data):
    with DATA.open("w", encoding="utf-8") as f: json.dump(data, f, indent=2)

def main():
    data = load()
    print("JARVIS LITE ONLINE — type help for commands")
    while True:
        cmd = input("\nJARVIS> ").strip().lower()
        if cmd == "help":
            print("Commands: note, task, notes, tasks, done, exit")
        elif cmd == "note":
            value = input("Note: ").strip()
            if value: data["notes"].append(value); save(data); print("Note saved.")
        elif cmd == "task":
            value = input("Task: ").strip()
            if value: data["tasks"].append({"text": value, "done": False}); save(data); print("Task added.")
        elif cmd == "notes":
            if not data["notes"]: print("No notes saved.")
            for i, note in enumerate(data["notes"], 1): print(f"{i}. {note}")
        elif cmd == "tasks":
            if not data["tasks"]: print("No tasks saved.")
            for i, task in enumerate(data["tasks"], 1):
                print(f"{i}. [{'x' if task['done'] else ' '}] {task['text']}")
        elif cmd == "done":
            try:
                n = int(input("Task number: "))
                if 1 <= n <= len(data["tasks"]):
                    data["tasks"][n-1]["done"] = True; save(data); print("Task completed.")
                else: print("Task number not found.")
            except ValueError: print("Enter a valid number.")
        elif cmd in {"exit", "quit"}:
            print("JARVIS signing off."); break
        else: print("Unknown command. Type help.")

if __name__ == "__main__":
    main()
