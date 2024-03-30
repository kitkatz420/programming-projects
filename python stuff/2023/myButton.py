from tkinter import *
from tkinter import ttk

root =Tk()
root.title("simple calculator")

programDisplay = Entry(root, width=35, borderwidth=5)
#programDisplayGrid =
programDisplay.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

i==0
i+=1

def click(number):
    current = programDisplay.get()
    programDisplay.delete(0, END)
    programDisplay.insert(0, str(current) + str(number))


def myCommand(myCommandFunction):
    myCommandFunction = lambda : click(i)

#class myProgramGrid:
    #def __init__(self, Grid):



#class myProgramDisplay:
 #   def __init__(self, programDisplay, ):
        



#class myButtonText:
   # def __init__(self, text)
   #self.text = text



#class myButtonPadding:
   # def __init__(self, padx, pady):
   #     self.padx = padx
   #     self.pady = pady



#class myButtonCommand:
   # def __init__(self, myCommand):



#class myButton:
#    def __init__(self):
