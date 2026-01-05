from tkinter import *
from scenes import SCENES

class GameUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root

        # -------- create widgets --------
        self.main_container = Frame(self.root, bg='black')
        self.content_frame = Frame(self.main_container, bg='black')
        
        self.top_menu_frame = Frame(self.content_frame, bg="black")

        self.menu_button = Button(
            self.top_menu_frame, 
            text="Main Menu", 
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            highlightthickness=0,
            command=controller.go_to_main_menu
        )
        self.save_button = Button(
            self.top_menu_frame, 
            text="Save Game", 
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            highlightthickness=0,
            command=controller.save_game
        )
        self.load_button = Button(
            self.top_menu_frame, 
            text="Load Game", 
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            highlightthickness=0,
            command=controller.load_game
        )
        self.quit_button = Button(
            self.top_menu_frame, 
            text="Quit Game", 
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            highlightthickness=0,
            command=self.quit_game
        )

        self.title_label = Label(self.content_frame, bg='black', fg='white')
        
        self.text_frame = Frame(self.content_frame, bg='black')
        
        self.text_widget = Text(
            self.text_frame, 
            bg='black', 
            fg='white', 
            insertbackground='white', 
            selectbackground='gray25', 
            relief='flat', 
            borderwidth=0, 
            width=80, 
            height=20, 
            wrap=WORD
        )
        
        self.scrollbar = Scrollbar(self.text_frame, bg='black', troughcolor='black')
        
        self.text_widget.configure(yscrollcommand=self.scrollbar.set, state=DISABLED)
        self.scrollbar.configure(command=self.text_widget.yview)

        self.choices_frame = Frame(self.content_frame, bg='black')
        
        
        # -------- pack widgets --------
        self.main_container.pack(expand=True, fill=BOTH)
        self.content_frame.pack(anchor=CENTER)
        
        self.top_menu_frame.pack(pady=8)
        self.menu_button.pack(side=LEFT, padx=8)
        self.save_button.pack(side=LEFT, padx=8)
        self.load_button.pack(side=LEFT, padx=8)
        self.quit_button.pack(side=LEFT, padx=8)

        self.title_label.pack(pady=10)
        
        self.text_frame.pack(pady=10)
        self.text_widget.pack(side=LEFT, expand=True, fill=BOTH)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.choices_frame.pack(pady=15)
    
    def render_scene(self, scene_id, state):
        if scene_id == "menu_main":
            self.hide_top_menu()
        else:
            self.show_top_menu()
        
        scene = SCENES[scene_id]

        self.title_label.configure(text=scene["title"])
        
        self._set_text("")
        for block in scene["text_blocks"]:
            text_to_show = self.get_text_for_block(block, state)
            self._append_text(text_to_show + "\n\n")

        self._clear_choices()
        for choice in scene["choices"]:
            if self.should_show_choice(choice, state):
                self._add_choice_button(choice)
    
    def quit_game(self):
        self.root.quit()


    # -------- UI helper methods --------

    def _set_text(self, text):
        self.text_widget.configure(state=NORMAL)
        self.text_widget.delete("1.0", END)
        self.text_widget.insert(END, text)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
    
    def _append_text(self, text):
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, text)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


    def _clear_choices(self):
        for button in self.choices_frame.winfo_children():
            button.destroy()

    def _add_choice_button(self, choice):
        btn = Button(
            self.choices_frame,
            text=choice["label"],
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            highlightthickness=0,
            command=lambda: self.controller.on_choice_selected(choice["id"])
        )
        btn.pack(side=LEFT, padx=8)
    
    def show_top_menu(self):
        self.top_menu_frame.pack(pady=8, before=self.title_label)
    
    def hide_top_menu(self):
        self.top_menu_frame.pack_forget()
    
    def should_show_choice(self, choice, state):
        if "condition" not in choice:
            return True
        
        condition = choice["condition"]

        if "requires_flag" in condition:
            flag_name = condition["requires_flag"]
            return state["flags"].get(flag_name, False) == True
        
        if "requires_flag_false" in condition:
            flag_name = condition["requires_flag_false"]
            return state["flags"].get(flag_name, False) == False
        
        return True
    
    def get_text_for_block(self, block, state):
        if "condition" not in block:
            return block["text"]
        
        condition = block["condition"]

        if "requires_flag" in condition:
            flag_name = condition["requires_flag"]
            has_flag = state["flags"].get(flag_name, False)

            if has_flag and "text_if_true" in block:
                return block["text_if_true"]
            elif not has_flag and "text_if_false" in block:
                return block["text_if_false"]
        
        return block["text"]