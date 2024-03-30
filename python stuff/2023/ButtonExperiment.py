from tkinter import *
from tkinter import ttk

root =Tk()
root.title("simple calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)



def click(number):
    current =e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


#class myButtonGrid:
# def __init__(self, row = row, grid.column = column)):


class myButton(e):
 def __init__(self, text, padx, pady, Grid, Button):
     self.text = text
     self.padx = padx
     self.pady = pady
     self.Grid = Grid
     #self.Row = Row
     #self.Column =Column


button_1 = myButton( "1", 20, 20, 2 Button(root, command = lambda : click(1)))




