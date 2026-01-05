from scenes import SCENES
from tkinter import messagebox
from save_system import *

class GameController:
    def __init__(self):
        self.state = self.create_initial_state()
        self.ui = None
    

    def attach_ui(self, ui):
        self.ui = ui

    def start(self):
        self.create_initial_state()
        self.render_current_scene()

    def start_new_game(self):
        self.state["meta"]["current_scene_id"] = "test_01"
        self.render_current_scene()
    
    def render_current_scene(self):
        scene_id = self.state["meta"]["current_scene_id"]
        self.ui.render_scene(scene_id, self.state)

    def on_choice_selected(self, choice_id):
        if choice_id == "menu_new_game":
            self.start_new_game()
            return
        
        if choice_id == "load_game":
            self.load_game()
            return
        
        if choice_id == "menu_quit":
            self.ui.quit_game()
            return
        
        try:
            current_scene = SCENES[self.state["meta"]["current_scene_id"]]
        except KeyError: 
            messagebox.showerror("Error", f"Could not find scene: {self.state['meta']['current_scene_id']}")
            return
        
        for choice in current_scene["choices"]:
            if choice["id"] == choice_id:
                self.apply_choice_effects(choice, self.state)
                self.state["meta"]["current_scene_id"] = choice["next"]
                break
            
        # update pulse if needed // advance_pulse(self.state)
        # next scene // self.state["meta"]["current_scene_id"] = route_next_scene(self.state)
        # autosave // self.save_game(self.state)
        self.render_current_scene()
    
    def save_game(self):
        try:
            save_state(self.state)
            messagebox.showinfo("Saved", "Game saved.")
        except Exception as e:
            messagebox.showerror("Save Failed", str(e))

    def load_game(self):
        if not save_exists():
            messagebox.showwarning("No Save", "No save file found.")
            return
        
        try:
            self.state = load_state()
            self.render_current_scene()
            messagebox.showinfo("Loaded", "Game loaded.")
        except Exception as e:
            messagebox.showerror("Load Failed", str(e))

    def go_to_main_menu(self):
        self.state["meta"]["current_scene_id"] = "menu_main"
        self.render_current_scene()
    
    def create_initial_state(self):
        return {
            "meta": {
                "current_scene_id": "menu_main",
                "version": 1
            },
            "pulse_stage": 0,
            "flags": {}, # booleans i.e. "talked_to_worker": True
            "counters": {}, # ints i.e. "checked_logs": 3
            "quests": {
                "active": [],
                "completed": [],
                "progress": {},
            },

        }

    def apply_choice_effects(self, choice, state):
        if "effects" not in choice:
            return
        
        effects = choice["effects"]

        if "flags" in effects:
            for flag_name, flag_value in effects["flags"].items():
                state["flags"][flag_name] = flag_value
        
        if "counters" in effects:
            for counter_name, change in effects["counters"].items():
                if counter_name not in state["counters"]:
                    state["counters"][counter_name] = 0
                state["counters"][counter_name] += change