from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(root):
        super(Window, root).__init__()

        root.title("simple window")
        root.minsize(500, 400)


        root.button = ttk.Button(root, text="0")
        root.button.grid(column=0, row=0, padx=20, pady=20)

window = Window()
window.mainloop()
