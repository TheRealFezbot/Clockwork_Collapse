from tkinter import *
from tkinter import simpledialog
from scenes import SCENES
from quests import QUESTS
from save_system import get_save_info, save_exists

class GameUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.typewriter_job = None
        self.is_typing = False

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
        self.quest_button = Button(
            self.top_menu_frame,
            text="Quest Log",
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            highlightthickness=0,
            command=controller.show_quest_log
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
        
        self.text_widget.bind("<Button-1>", self._skip_typewriter)

        self.scrollbar = Scrollbar(self.text_frame, bg='black', troughcolor='black')
        
        self.text_widget.configure(yscrollcommand=self.scrollbar.set, state=DISABLED)
        self.scrollbar.configure(command=self.text_widget.yview)

        self.choices_frame = Frame(self.content_frame, bg='black')
        
        
        # -------- pack widgets --------
        self.main_container.pack(expand=True, fill=BOTH)
        self.content_frame.pack(anchor=CENTER)
        
        self.top_menu_frame.pack(pady=8)
        self.menu_button.pack(side=LEFT, padx=8)
        self.quest_button.pack(side=LEFT, padx=8)
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
        
        full_text = ""
        for block in scene["text_blocks"]:
            text_to_show = self.get_text_for_block(block, state)
            if text_to_show:
                full_text += text_to_show + "\n\n"
        
        self._typewriter_text(full_text)

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
    
    def _typewriter_text(self, text, delay=20):
        if self.typewriter_job:
            self.root.after_cancel(self.typewriter_job)
        
        self.is_typing = True
        self.full_text = text
        self._set_text("")

        def type_char(index):
            if index < len(text):
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, text[index])
                self.text_widget.configure(state=DISABLED)
                self.text_widget.see(END)

                self.typewriter_job = self.root.after(delay, lambda: type_char(index + 1))
            else:
                self.is_typing = False
                self.typewriter_job = None
                self._enable_choice_buttons()
            
        type_char(0)
    
    def _skip_typewriter(self, event=None):
        if self.is_typing and self.typewriter_job:
            self.root.after_cancel(self.typewriter_job)
            self.is_typing = False
            self.typewriter_job = None
            self._set_text(self.full_text)
            self._enable_choice_buttons()


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
            command=lambda: self.controller.on_choice_selected(choice["id"]),
            state=DISABLED if self.is_typing else NORMAL
        )
        btn.pack(side=LEFT, padx=8)
    
    def _enable_choice_buttons(self):
        for btn in self.choices_frame.winfo_children():
            btn.configure(state=NORMAL)
    
    def show_top_menu(self):
        self.top_menu_frame.pack(pady=8, before=self.title_label)
    
    def hide_top_menu(self):
        self.top_menu_frame.pack_forget()
    
    def should_show_choice(self, choice, state):
        if "condition" not in choice:
            return True

        condition = choice["condition"]

        if "requires_flag" in condition:
            flags = condition["requires_flag"]
            if isinstance(flags, str):
                flags = [flags]
            for flag_name in flags:
                if state["flags"].get(flag_name, False) != True:
                    return False

        if "requires_flag_false" in condition:
            flags = condition["requires_flag_false"]
            if isinstance(flags, str):
                flags = [flags]
            for flag_name in flags:
                if state["flags"].get(flag_name, False) != False:
                    return False

        return True
    
    def get_text_for_block(self, block, state):
        if "condition" not in block:
            text = block["text"]
        else:
            condition = block["condition"]

            if "requires_flag" in condition:
                flags = condition["requires_flag"]
                if isinstance(flags, str):
                    flags = [flags]
                for flag_name in flags:
                    if not state["flags"].get(flag_name, False):
                        return ""

            if "requires_flag_false" in condition:
                flags = condition["requires_flag_false"]
                if isinstance(flags, str):
                    flags = [flags]
                for flag_name in flags:
                    if state["flags"].get(flag_name, False):
                        return ""

            text = block["text"]

        player_name = state["meta"].get("player_name", "Operator")
        text = text.replace("{player_name}", player_name)

        return text
    
    def show_save_slot_picker(self):
        selected_slot = None

        save_window = Toplevel(self.root)
        save_window.title("Save Game")
        save_window.geometry("600x400")
        save_window.config(bg="black")

        def on_slot_selected(slot_num):
            nonlocal selected_slot
            selected_slot = slot_num
            save_window.destroy()

        label = Label(save_window, text="Select a save slot:", bg="black", fg="white")
        label.pack(pady=20)

        for slot_number in range(1, 4):
            save_info = get_save_info(slot_number)

            if save_info:
                button_text = f"Slot {slot_number}: {save_info['scene_id']} ({save_info['timestamp']})"
            else:
                button_text = f"Slot {slot_number}: Empty"
        
            btn = Button(
                save_window,
                text=button_text,
                bg="black",
                fg="white",
                command=lambda num=slot_number: on_slot_selected(num)
            )
            btn.pack(pady=5)
        
        cancel_btn = Button(
            save_window,
            text="Cancel",
            bg="black",
            fg="white",
            command=save_window.destroy
        )
        cancel_btn.pack(pady=10)

        save_window.wait_window()

        return selected_slot
    
    def show_load_slot_picker(self, available_slots):
        selected_slot = None
        
        load_window = Toplevel(self.root)
        load_window.title("Load Game")
        load_window.geometry("600x400")
        load_window.config(bg="black")
        
        def on_slot_selected(slot_num):
            nonlocal selected_slot
            selected_slot = slot_num
            load_window.destroy()
        
        label = Label(load_window, text="Select a save to load:", bg="black", fg="white")
        label.pack(pady=20)
        
        from save_system import save_exists
        if save_exists(is_autosave=True):
            btn = Button(
                load_window,
                text="Autosave: [Latest]",
                bg="black",
                fg="white",
                command=lambda: on_slot_selected("autosave")
            )
            btn.pack(pady=5)
        
        for slot_number in available_slots:
            save_info = get_save_info(slot_number)
            button_text = f"Slot {slot_number}: {save_info['scene_id']} ({save_info['timestamp']})"
            
            btn = Button(
                load_window,
                text=button_text,
                bg="black",
                fg="white",
                command=lambda num=slot_number: on_slot_selected(num)
            )
            btn.pack(pady=5)
        
        cancel_btn = Button(
            load_window,
            text="Cancel",
            bg="black",
            fg="white",
            command=load_window.destroy 
        )
        cancel_btn.pack(pady=10)
        
        load_window.wait_window()
        
        return selected_slot

    def show_quest_log(self, state):
        quest_window = Toplevel(self.root)
        quest_window.title("Quest Log")
        quest_window.geometry("600x500")
        quest_window.config(bg="black")


        title = Label(
            quest_window,
            text="Quest Log",
            bg="black",
            fg="white",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        canvas_frame = Frame(quest_window, bg="black")
        canvas_frame.pack(fill=BOTH, expand=True, padx=20, pady=(0, 10))

        canvas = Canvas(canvas_frame, bg="black", highlightthickness=0)
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, bg="black", troughcolor="black")

        main_frame = Frame(canvas, bg="black")

        main_frame.bind(
            "<Configure>",
            lambda _: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=main_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        if state["quests"]["active"]:
            active_label = Label(
                main_frame,
                text="Active Quests:",
                bg="black",
                fg="yellow",
                font=("Arial", 12, "bold")
            )
            active_label.pack(anchor=W, pady=(10, 5))

            for quest_id in state["quests"]["active"]:
                quest = QUESTS[quest_id]

                quest_name = Label(
                    main_frame,
                    text=quest["name"],
                    bg="black",
                    fg="white",
                    font=("Arial", 11, "bold")
                )
                quest_name.pack(anchor=W, padx=10)

                quest_desc = Label(
                    main_frame,
                    text=quest["description"],
                    bg="black",
                    fg="gray70",
                    font=("Arial", 9)
                )
                quest_desc.pack(anchor=W, padx=20, pady=(0,5))

                first_incomplete_idx = None

                for idx, obj in enumerate(quest["objectives"]):
                    is_completed = state["quests"]["progress"][quest_id][obj["id"]]
                    if not is_completed:
                        first_incomplete_idx = idx
                        break


                for idx, obj in enumerate(quest["objectives"]):
                    if "condition" in obj:
                        condition_met = state["flags"].get(obj["condition"], False)
                        if not condition_met:
                            continue
                    
                    is_completed = state["quests"]["progress"][quest_id][obj["id"]]

                    
                    if is_completed or idx == first_incomplete_idx:
                        if is_completed:
                            obj_text = f"  ✓ {obj['description']}"
                            obj_color = "green"
                        else:
                            obj_text = f"  ○ {obj['description']}"
                            obj_color = "white"
                    
                        obj_label = Label(
                            main_frame,
                            text=obj_text,
                            bg="black",
                            fg=obj_color,
                            font=("Arial", 10)
                        )
                        obj_label.pack(anchor=W, padx=30)
                
                seperator = Label(main_frame, text="", bg="black")
                seperator.pack(pady=5)
        else:
            no_quests = Label(
                main_frame, 
                text="No active quests",
                bg="black",
                fg="gray",
                font=("Arial", 10)
            )
            no_quests.pack(pady=10)
        
        if state["quests"]["completed"]:
            completed_label = Label(
                main_frame,
                text="Completed Quests:",
                bg="black",
                fg="green",
                font=("Arial", 12, "bold")
            )
            completed_label.pack(anchor=W, pady=(10, 5))

            for quest_id in state["quests"]["completed"]:
                quest = QUESTS[quest_id]
                quest_name = Label(
                    main_frame,
                    text=f"✓ {quest['name']}",
                    bg="black",
                    fg="green",
                    font=("Arial", 10)
                )
                quest_name.pack(anchor=W, padx=10)
        
        close_btn = Button(
            quest_window,
            text="Close",
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            highlightthickness=0,
            command=quest_window.destroy
        )
        close_btn.pack(pady=10)
    
    def prompt_player_name(self):
        name = simpledialog.askstring(
            "Character Name",
            "Enter your name:",
            parent=self.root,
        )

        if name and name.strip():
            return name.strip()
        else:
            return "Cogsworth"