from tkinter import *
from PIL import ImageTk,Image

imtk = ImageTk


root=Tk()
root.title("image viewer")



my_img = imtk.PhotoImage(Image.open(""))
my_label = label("farts")
my_label.pack()


root.mainloop()
