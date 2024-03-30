from tkinter import *
from tkinter import ttk

root = Tk()


class assignEntry(Entry):
    def __init__(root, text=None, row=None, col=None, padx=None, pady=None, width=None, borderwidth=None, command=None, color=None):
        root.text = text
        root.row = row
        root.column = col
        root.padx = padx
        root.pady = pady
        root.width = width
        root.borderwidth = borderwidth
        root.command = command
        root.color = color
        super().__init__()
        root['bg'] = root.color
        root['text'] = root.text
        root['command'] = root.command
        root.grid(row = root.row, column = root.column)
        #root['pady'] = root.pady
        #root['padx'] = root.padx
        root['borderwidth'] = root.borderwidth
        root['width'] = root.width

        







nameEntry = assignEntry("name", 1, 0, 1, 1, 5, 5)
textEntry = assignEntry("text", 1, 1, 1, 1, 5, 5)
