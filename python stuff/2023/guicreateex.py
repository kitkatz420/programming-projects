#add all necessary imports
importBlock = (
"from tkinter import *\n"
      
"from tkinter import ttk\n"

"from assignButton import assignButton\n"
      
"import calcfunctions\n"
      
"from calcfunctions import *\n"
)



#btn1= assignButton("1", 2, 0, lambda: buttonClick(1), 20, 20)
print("values default is None. If you want to leave a value out set value to None when prompted")
buttonName =(input("insert button name: "))
textValue=(input("insert button text : "))
rowValue=(input("insert button row : "))
columnValue=(input("insert button column : "))
commandValue=(input("insert button command : "))
padxValue=(input("insert button padx : "))
padyValue=(input("insert button pady : "))
colorValue=(input("insert button color : "))


executionBlock = (buttonName + ' = assignButton(' + textValue + ', ' + rowValue + ', ' + columnValue + ', ' + commandValue + ', ' +  padxValue + ', '  + padyValue + ', ' + colorValue + ')')


#print(importBlock)
print(executionBlock)
