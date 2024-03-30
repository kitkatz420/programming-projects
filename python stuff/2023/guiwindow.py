from tkinter import *
from tkinter import ttk

root = Tk()



e = Entry(root, width=5, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)


class assignEntry(Entry):
    def __init__(root, text=None, row=None, col=None, command="command: ",borderwidth, width, padx=None, pady=None, color=None, **kwargs):
        self.text = text
        self.row = row
        self.column = col
        self.command = command
        self.color = color
        self.padx = padx
        self.pady = pady
        self.borderwith = borderwidth
        self.width = width
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self.grid(row = self.row, column = self.column)
        self['pady'] = self.pady
        self['padx'] = self.padx
        self['borderwidth'] = self.borderwidth
        self['width'] = self.width


nameEntry = assignEntry("name", 1, 0, None, 5, 5, 10, 20, None) 
