from tkinter import *



#root = Tk()
#e = Entry(root, width=35, borderwidth=5)
#e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)


class assignButton(Button):
    def __init__(root, text=None, row=None, col=None, command="command: ", padx=None, pady=None, color=None, **kwargs):
        root.text = text
        root.row = row
        root.column = col
        root.command = command
        root.color = color
        root.padx = padx
        root.pady = pady
        super().__init__()
        root['bg'] = root.color
        root['text'] = root.text
        root['command'] = root.command
        root.grid(row = root.row, column = root.column)
        root['pady'] = root.pady
        root['padx'] = root.padx

        


#def buttonClick(number):
 #   current =e.get()
  #  e.delete(0, END)
   # e.insert(0, str(current) + str(number))


btn1 = assignButton("1", 2, 0, lambda:buttonClick(1), 20, 20, "green")

#windowGeometry = root.geometry('400x200')

#btn1 = assignButton()

#root.mainloop()
