from tkinter import *
from assignButton import assignButton
#from assignButton import buttonClick
#root = Tk()
#root.title("buttonMaker")

#e = Entry(root, width=35, borderwidth=5)
#e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

#def buttonClick(number):
 #   current =e.get()
 #   e.delete(0, END)
#    e.insert(0, str(current) + str(number))


#btn1= assignButton("1", 1, 0, lambda: buttonClick(1))
#btn2= assignButton("2", 1, 1, lambda: buttonClick(2))
#btn3= assignButton("3", 1, 2, lambda: buttonClick(3))










class assignButton:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

#choose button features    
    def __init__(self, text, row, col, command):
        print("2. Initialize the new instance of Point.")
        self.text = text
        self.row = row
        self.column = col
        self.command = command

        

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"




