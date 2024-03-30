from tkinter import *
from tkinter import ttk


self = Tk()


e = Entry(self, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

def buttonClick(number):
    current =e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))




class assignButton(Button):
    buttonCount = 0
    #text = input("text: "),
    #row = input("row: "),
    #col = input("column: "),
    #command = input("command: "),
    #padx = input("pad x: "),
    #pady = input("pady: "),
   # color = input("color: "),
    def __init__(self, text = input("text: "), row = input("row: "), col = input("column: "), command = input("command: "), padx = input("pad x: "), pady = input("pady: "), color = input("color: "),  **kwargs):
        

        self.text = text
        self.row = row #input("what row")
        self.column = col #input("col")
        self.command = command #input("command")
        self.color = color #input("color")
        self.padx = padx #input("padx")
        self.pady = pady #input("pady")
        assignButton.buttonCount += 1
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self.grid(row = self.row, column = self.column)
        self['pady'] = self.pady
        self['padx'] = self.padx

btn1= assignButton(assignButton.text, assignButton.row, assignButton.col, assignButton.command, assignButton.padx, assignButton.pady, assignButton.color)        
#btn1= assignButton()      



