
#numberOfButtons = 0
#numberOfButtonsIWant =  0
#doIWantAnotherButton = (input("do i want another button y/n"))
#areYouSure = (input("are you sure you're finished? y/n"))
def buttonIteration():
    numberOfButtons = 0
    numberOfButtonsIWant =  10
    doIWantAnotherButton = str(input("do i want another button y/n"))
    #areYouSure = (input("are you sure you're finished? y/n"))

    
    while numberOfButtonsIWant >= numberOfButtons:
        if doIWantAnotherButton.upper() == "Y":
            numberOfButtons += 1
            print("added one button")
            print(numberOfButtons)
            
        

        elif doIWantAnotherButton == 'no':
            
            if areYouSure == 'no':
                continue
            else:
                exit 



       

        #print("creating new button")
    


test = buttonIteration()

print(test)
#elif areYouSure == 'y':
 #       print("terminating program")
        
    




#while numberOfButtonsIWant >= numberOfButtons:
 #   print(numberOfButtons)
  #  numberOfButtons += 1

#class buttonIteration():
 #   def __init__():
