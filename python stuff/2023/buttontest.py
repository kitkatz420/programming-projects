from tkinter import *
from tkinter import ttk
from assignButton import assignButton
import calcfunctions
from calcfunctions import *
btn1 = assignButton(1, 2, 0, lambda: buttonClick(1), 20, 20, "green")
btn2 = assignButton(2, 2, 1, lambda: buttonClick(2), 20, 20, "green")
