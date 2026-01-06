from scenes import SCENES
from quests import QUESTS
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

                if "start_quest" in choice:
                    self.start_quest(choice["start_quest"])

                self.state["meta"]["current_scene_id"] = choice["next"]
                break
            
        # update pulse if needed // advance_pulse(self.state)
        
        self.update_all_quests()

        self.autosave()
        self.render_current_scene()
    
    def save_game(self, slot_number=None):
        if slot_number is None:
            slot_number = self.ui.show_save_slot_picker()
            if slot_number is None:
                return
            
        try:
            save_state(self.state, slot_number=slot_number)
            self.state["meta"]["current_slot"] = slot_number
            messagebox.showinfo("Saved", "Game saved.")
        except Exception as e:
            messagebox.showerror("Save Failed", str(e))

    def load_game(self):
        available_slots = list_all_saves()
        
        if not available_slots:
            messagebox.showwarning("No Saves", "No save files found.")
            return
        
        slot_number = self.ui.show_load_slot_picker(available_slots)
        if slot_number is None:
            return


        try:
            if slot_number == "autosave":
                self.state = load_state(is_autosave=True)
                self.state["meta"]["current_slot"] = slot_number
            else:
                self.state = load_state(slot_number=slot_number)
                self.state["meta"]["current_slot"] = slot_number
                
            self.render_current_scene()
            messagebox.showinfo("Loaded", f"Game loaded from slot {slot_number}.")
        except Exception as e:
            messagebox.showerror("Load Failed", str(e))
    
    def autosave(self):
        try:
            save_state(self.state, is_autosave=True)
        except Exception as e:
            print(f"Autosaved failed: {e}")

    def go_to_main_menu(self):
        self.state["meta"]["current_scene_id"] = "menu_main"
        self.render_current_scene()
    
    def create_initial_state(self):
        return {
            "meta": {
                "current_scene_id": "menu_main",
                "version": 1,
                "current_slot": None,
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

    
    # ----------- Quest Functions -----------

    def start_quest(self, quest_id):
        if quest_id in self.state["quests"]["active"]:
            return
        
        if quest_id in self.state["quests"]["completed"]:
            return
        
        self.state["quests"]["active"].append(quest_id)

        quest = QUESTS[quest_id]
        self.state["quests"]["progress"][quest_id] = {}

        for obj in quest["objectives"]:
            self.state["quests"]["progress"][quest_id][obj["id"]] = False
        
        messagebox.showinfo("Quest Started", f"New Quest: {quest['name']}")
    
    def check_quest_progress(self, quest_id):
        if quest_id not in self.state["quests"]["active"]:
            return
        
        quest = QUESTS[quest_id]
        all_completed = True

        for obj in quest["objectives"]:
            if obj["type"] == "flag":
                flag_name = obj["requirement"]
                if flag_name in self.state["flags"] and self.state["flags"][flag_name]:
                    self.state["quests"]["progress"][quest_id][obj["id"]] = True
                else:
                    all_completed = False

            elif obj["type"] == "counter":
                counter_name = obj["requirement"]
                target = obj["target"]
                current = self.state["counters"].get(counter_name, 0)

                if current >= target:
                    self.state["quests"]["progress"][quest_id][obj["id"]] = True
                else:
                    all_completed = False
            
        if all_completed:
            self.complete_quest(quest_id)
    
    def complete_quest(self, quest_id):
        self.state["quests"]["active"].remove(quest_id)
        self.state["quests"]["completed"].append(quest_id)

        #self.apply_quest_rewards(quest_id) // apply quest rewards 

        quest = QUESTS[quest_id]
        messagebox.showinfo("Quest Completed", f"Quest Completed: {quest['name']}")
    
    def update_all_quests(self):
        for quest_id in self.state["quests"]["active"]:
            self.check_quest_progress(quest_id)
    
    def show_quest_log(self):
        self.ui.show_quest_log(self.state)