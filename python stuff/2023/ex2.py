
numberOfButtons = 0
numberOfButtonsIWant = 1
doIWantAnotherButton = ()
def buttonIteration():
    doIWantAnotherButton = str(input("do i want another button y/n"))
    areYouSure = (input("are you sure you're finished? y/n"))


while numberOfButtonsIWant >= numberOfButtons:
      if doIWantAnotherButton.upper() == "Y":
            numberOfButtons += 1
            print(numberOfButtons)

            
            
