from tkinter import ttk
from tkinter import *
from cats import assignButton
from cats import *

class assignEntry(Entry):
    #global e

    
    def __init__(self, text=None, row=None, col=None, padx=None, pady=None, borderwidth=None, command=None):
        self.text = text
        self.row = row
        self.column = col
        #self.padx = padx
        #self.pady = pady
        #self.width = width
        self.borderwidth = borderwidth
        self.command = command
        #self.color = color
        super().__init__()
        #self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self.grid(row = self.row, column = self.column)
        self['borderwidth'] = self.borderwidth
        

nameEntry = assignEntry("name1", 0, 1, 5, 5, 5)
rowEntry = assignEntry("name2", 0, 2, 5, 5, 5)
colEntry = assignEntry("name3", 0, 3, 5, 5, 5)
nameEntry1 = assignEntry("name4", 1, 1, 5, 5, 5)
nameEntry2 = assignEntry("name5", 1, 2, 5, 5, 5)
nameEntry3 = assignEntry("name6", 1, 3, 5, 5, 5)
nameEntry4 = assignEntry("name7", 2, 1, 5, 5, 5)
nameEntry5 = assignEntry("name8", 2, 2, 5, 5, 5)
nameEntry6 = assignEntry("name9", 2, 3, 5, 5, 5)
btn1= assignButton("1", 0, 0, lambda: buttonClick(1), 10, 10)
