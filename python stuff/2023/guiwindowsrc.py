from tkinter import *
from tkinter import ttk
from assignButton import *
import calcfunctions
from calcfunctions import *
from assignEntry import *


#root = Tk()

#e = Entry(root, width=35, borderwidth=5)

def buttonClick(number):
    current =e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

nameEntry = assignEntry("name", 0, 1, 5, 5, 5, 5)
btn1= assignButton("1", 0, 0, lambda: buttonClick(1), 10, 10)
