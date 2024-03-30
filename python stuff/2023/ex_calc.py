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


class MyButton:
    def __init__(self, text, padx, pady, command, root):
      self.text = text
      self.padx = padx
      self.pady = pady
      self.root = Tk(e)
     # self.grid 
    def click(number):
     current =e.get()
     e.delete(0, END)
     e.insert(0, str(current) + str(number))

    
MB = MyButton

button_1.grid = MyButton("1", 20, 20,  click(1), root)


#button_1.Grid = button_1
#button_1.grid[(2,0)] = button_1

