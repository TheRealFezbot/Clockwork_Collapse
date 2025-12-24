from tkinter import *
from scenes import SCENES

class GameUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root

        # -------- create widgets --------
        self.main_container = Frame(self.root, bg='black')
        self.content_frame = Frame(self.main_container, bg='black')
        
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
        
        self.title_label.pack(pady=10)
        
        self.text_frame.pack(pady=10)
        self.text_widget.pack(side=LEFT, expand=True, fill=BOTH)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.choices_frame.pack(pady=15)
    
    def render_scene(self, scene_id, state):
        scene = SCENES[scene_id]

        self.title_label.configure(text=scene["title"])
        
        self._set_text("")
        for block in scene["text_blocks"]:
            self._append_text(block["text"] + "\n\n")

        self._clear_choices()
        for choice in scene["choices"]:
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