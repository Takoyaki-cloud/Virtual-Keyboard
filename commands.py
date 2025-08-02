import json
import os

COMMANDS_FILE = "commands.json"

def load_commands():
    try:
        with open(COMMANDS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        # Si fichier absent ou corrompu, renvoyer liste vide
        return []

def save_commands(commands):
    with open(COMMANDS_FILE, "w") as f:
        json.dump(commands, f, indent=2)

def add_command(new_command):
    commands = load_commands()
    commands.append(new_command)
    save_commands(commands)

def delete_command(index):
    commands = load_commands()
    if 0 <= index < len(commands):
        commands.pop(index)
        save_commands(commands)
