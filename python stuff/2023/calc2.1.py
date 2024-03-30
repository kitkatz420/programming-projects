from tkinter import *
from tkinter import ttk
from assignButton import *
import calcfunctions
from calcfunctions import *



root.title("calc 2.1")


e = calcfunctions.e





btn1= assignButton("1", 2, 0, lambda: buttonClick(1), 20, 20)
btn2= assignButton("2", 2, 1, lambda: buttonClick(2), 20, 20)
btn3= assignButton("3", 2, 2, lambda: buttonClick(3), 20, 20)
btn4= assignButton("4", 3, 0, lambda: buttonClick(4), 20, 20)
btn5= assignButton("5", 3, 1, lambda: buttonClick(5), 20, 20)
btn6= assignButton("6", 3, 2, lambda: buttonClick(6), 20, 20)
btn7= assignButton("7", 4, 0, lambda: buttonClick(7), 20, 20)
btn8= assignButton("8", 4, 1, lambda: buttonClick(8), 20, 20)
btn9= assignButton("9", 4, 2, lambda: buttonClick(9), 20, 20)
btn0= assignButton("0", 5, 1, lambda: buttonClick(0), 20, 20)
btndecimal= assignButton(".", 5, 0, lambda: button_click("."), 20, 20)
btnequals= assignButton("=", 5, 2, button_equals, 20, 20)
btnadd= assignButton("+", 4, 3, button_add, 20, 20)
btnsubtract= assignButton("-", 5, 3, button_subtract, 20, 20)
btnleftbracket= assignButton("(", 1, 0, lambda: buttonClick("("), 20, 20)
btnrightbracket= assignButton(")", 1, 1, lambda: buttonClick(")"), 20, 20)
btnclear= assignButton("c", 1, 2, button_clear, 20, 20)
btnbackspace= assignButton("<-", 1, 3, button_backspace, 20, 20)
btndivide= assignButton("÷", 3, 3, button_divide, 20, 20)
btnmnultiply= assignButton("x", 2, 3, button_multiply, 20, 20)



