from tkinter import *
from tkinter import ttk

#root = Tk()

#e = Entry(root, width=35, borderwidth=5)
#e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)


#def button_Click(number):
#    current =e.get()
#    e.delete(0, END)
#    e.insert(0, str(current) + str(number))

#def buttonClick(number):
 #   current =e.get()
  #  e.delete(0, END)
   # e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)
    return

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)



def button_equals():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))


    if math == "subtraction":
        e.insert(0, f_num - int(second_number))


    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))



    
def button_backspace():
    e.delete(END, END)
    return

