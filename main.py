from tkinter import *
from gamecontroller import GameController
from gameui import GameUI



def main():
    # create main window
    root = Tk()
    root.title("Clockwork Collapse")
    root.geometry("800x600")
    root.minsize(600, 400)
    root.config(bg='black')
    
    controller = GameController()
    ui = GameUI(root, controller)
    controller.attach_ui(ui)

    controller.start()
    root.mainloop()


if __name__ == "__main__":
    main()
