import json
import os
import datetime
from pathlib import Path

SAVE_DIR = Path("saves")
AUTOSAVE_FILE = SAVE_DIR / "autosave.json"

def get_save_file_path(slot_number):
    return SAVE_DIR / f"save_slot_{slot_number}.json"

def save_state(state, slot_number=None, is_autosave=False):
    if is_autosave:
        file_path = AUTOSAVE_FILE
    else:
        if slot_number is None:
            raise Exception("Must provide slot_number for manual save")
        file_path = get_save_file_path(slot_number)
    
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def load_state(slot_number=None, is_autosave=False):
    if is_autosave:
        file_path = AUTOSAVE_FILE
    else:
        if slot_number is None:
            raise Exception("Must provide slot_number for load")
        file_path = get_save_file_path(slot_number)
    
    if not save_exists(slot_number, is_autosave):
        return None

    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_exists(slot_number=None, is_autosave=False):
    if is_autosave:
        return AUTOSAVE_FILE.exists()
    else:
        return get_save_file_path(slot_number).exists()

def list_all_saves():
    slots = []
    for slot_number in range(1, 4):
        if save_exists(slot_number):
            slots.append(slot_number)
    return slots

def get_save_info(slot_number):
    if not save_exists(slot_number):
        return None
    
    state = load_state(slot_number)
    file_path = get_save_file_path(slot_number)
    m_time = os.path.getmtime(file_path)
    dt_m = datetime.datetime.fromtimestamp(m_time)
    
    return {
        "slot": slot_number,
        "scene_id": state["meta"]["current_scene_id"],
        "timestamp": dt_m.strftime("%d-%m-%Y %H:%M")
    }

    