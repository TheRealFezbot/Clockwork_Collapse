from scenes import SCENES

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
        
        if choice_id == "menu_quit":
            self.ui.quit_game()
        
        current_scene = SCENES[self.state["meta"]["current_scene_id"]]
        
        for choice in current_scene["choices"]:
            if choice["id"] == choice_id:
                self.state["meta"]["current_scene_id"] = choice["next"]
                break
        # apply effects // apply_choice_effects(choice_id, self.state)
        # update pulse if needed // advance_pulse(self.state)
        # next scene // self.state["meta"]["current_scene_id"]v=vroute_next_scene(self.state)
        # autosave // self.save_game("autosave")
        self.render_current_scene()
    
    def save_game(self):
        # serialize self.state to json file
        pass 

    def load_game(self):
        #self.state = load state from json
        # self.render_current_scene()
        pass 

    def create_initial_state(self):
        return {
            "meta": {"current_scene_id": "menu_main"},
            "pulse_stage": 0,
            "flags": {},
            "counters": {},
            "stances": {},
        }