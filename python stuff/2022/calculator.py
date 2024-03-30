from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("calculator")
        self.minsize(500, 400)

#no. 0 button
        self.button = ttk.Button(self, text = "0")
        self.button.grid(column = 1, row = 4)

# no. 1 button
        self.button = ttk.Button(self, text = "1")
        self.button.grid(column = 1, row = 0)
#no. 2 button
        self.button = ttk.Button(self, text = "2")
        self.button.grid(column = 1, row = 1)

#no. 3 button
        self.button = ttk.Button(self, text = "3")
        self.button.grid(column = 2, row = 1)


#no. 4 button
        self.button = ttk.Button(self, text = "4")
        self.button.grid(column = 0, row = 2)


#no. 5 button
        self.button = ttk.Button(self, text = "5")
        self.button.grid(column = 1, row = 2)


#no. 6 button
        self.button = ttk.Button(self, text = "6")
        self.button.grid(column = 2, row = 2)


#no. 7 button
        self.button = ttk.Button(self, text = "7")
        self.button.grid(column = 0, row = 3)


#no. 8 button
        self.button = ttk.Button(self, text = "8")
        self.button.grid(column = 1, row = 3)


#no. 9 button
        self.button = ttk.Button(self, text = "9")
        self.button.grid(column = 2, row = 3)

#decimal button
        self.button = ttk.Button(self, text = ".")
        self.button.grid(column = 0, row = 4)


#equals button
        self.button = ttk.Button(self, text = "=")
        self.button.grid(column = 2, row = 4)

#divide button
        self.button = ttk.Button(self, text = "÷")
        self.button.grid(column = 3, row = 1)

#multiply button
        self.button = ttk.Button(self, text = "x")
        self.button.grid(column = 3, row = 2)

#subtract button
        self.button = ttk.Button(self, text = "-")
        self.button.grid(column = 3, row = 3)

        
#add button
        self.button = ttk.Button(self, text = "+")
        self.button.grid(column = 3, row = 4)


#backspace button
        self.button = ttk.Button(self, text = "<-")
        self.button.grid(column = 3, row = 0)
#clear button
        self.button = ttk.Button(self, text = "c")
        self.button.grid(column = 2, row = 0)
#right bracket
        self.button = ttk.Button(self, text = ")")
        self.button.grid(column = 1, row = 0)
#left bracket
        self.button = ttk.Button(self, text = "(")
        self.button.grid(column = 0, row = 0)
#textbox
        #self.textbox = 


window = Window()
window.mainloop()

#sample



