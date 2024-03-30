import guicreatesrc as src

importBlock = src.importBlock

numberOfButtons = 0

numberOfButtonsIWant = 0

current = (input("what will your file name be dont forget the .py: "))
f = open(current, "a")

f.write(importBlock)
f.close()


def main():
  
    global current
   

    f = open(current, "a")
        
    





    doIWantAnotherButton = (input("make button y/n: "))


    while (doIWantAnotherButton != "no"):
        print("values default is None. If you want to leave a value out set value to None when prompted")
        buttonName =(input("insert button name: "))
        textValue=(input("insert button text : "))
        rowValue=(input("insert button row : "))
        columnValue=(input("insert button column : "))
        commandValue=(input("insert button command : "))
        padxValue=(input("insert button padx : "))
        padyValue=(input("insert button pady : "))
        colorValue=(input("insert button color : "))
        if (doIWantAnotherButton == "no"):
            f.close()
            exit()
        else:
            executionBlock = (buttonName + " = assignButton(" + textValue + ", " + rowValue + ", " + columnValue + ", " + commandValue + ", " +  padxValue + ", "  + padyValue + ", " + colorValue + ")\n")
            f.write(executionBlock)
        doIWantAnotherButton = (input("do you want another button y/n? "))
            

main()

