import json
from pathlib import Path

SAVE_DIR = Path("saves")
SAVE_FILE = SAVE_DIR / "save.json"


def save_state(state):
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    with SAVE_FILE.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def load_state():
    with SAVE_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_exists():
    return SAVE_FILE.exists()

    