from random import randint
from PythonUI import *
from time import sleep


def Slots(wallet: int):
    symbols = ["Orange","Cherry","BAR","Star","Bell","Soda"]
    winnings = 0 
    
    # Accessing Lists
    # variable = symbols[0]
    # symbols[0] = variable
    
    while wallet > 10:        
        # Gets user input and will exit if selected
        userInput = SelectFromList("What do you want to do?", ["Spin!","Exit"])
        if userInput == "Exit":
            break

        # Charges the user to play, and informs the user
        wallet -= 10
        PrintTerm("You inserted 10 coins!")
        
        # Spinning the slots, generates three symbols and displays them
        slots = []
        for index in range(0,3):
            sleep(1)
            slots.append(symbols[randint(0,5)]) # Generates a random number to get a symbol
            PrintBold(f"[{slots[index]}]") # Displays the symbol that was just generated
        
        # Checks 
        if slots[0] == "BAR" or slots[1] == "BAR" or slots[2] == "BAR":
            PrintTerm("Oh No! BAR! Try again!")
        elif slots[0] == slots[1] == slots[2]:
            winnings = 200
            PrintTerm("Yahoo!! You gat a triple and won 200 coins!")
        elif slots[0] == slots[1] or slots[0] == slots[2] or slots[1] == slots[2]:
            winnings = 20
            PrintTerm("You got a double! You won 20 coins!")
        else:
            PrintTerm("No Match! Try again!")
       
        wallet += winnings
        winnings = 0
        PrintTerm(f"You now have {wallet} coins!\n")
        PressToContinue()
    
    PrintBold("End of Slots!")
    return wallet


def Chicken(wallet):
   
    repeatLowBetCount: int = 0
    totalGuesses: int = 0
    totalLowGuesses: int = 0

    while wallet > 0:
    
        msg = "Please enter a bet from 1 to 100.\nor you can leave by entering [E]"
        userBet = QueryNumber(msg,0,wallet,False)
        randomBet = randint(1,100)
        totalGuesses += 1

        if userBet in range(1,5):
            totalLowGuesses += 1
            repeatLowBetCount += 1
        elif userBet == "e":
            break
        else:
            repeatLowBetCount = 0

        if repeatLowBetCount >= 3 or (totalLowGuesses / totalGuesses) > 0.33 and totalGuesses > 10:
            PrintBold("Hey!\nYour cheating!\nGet out of here!!")
            break

        PrintBold(f"Your Bet: {userBet}")
        sleep(1)
        PrintBold(f"House Bet: {randomBet}")
        sleep(1)
        
        if userBet <= randomBet:
            PrintTerm("\nYou Win!\nCongratulations!!!")
            wallet += userBet + userBet
        elif userBet > randomBet:
            PrintTerm("\noops!\nYou lost your bet!\nBetter luck next time!")
            wallet -= userBet
            
        PrintTerm(f"You now have {wallet} coins in your wallet!")
        PressToContinue()

    PrintTerm("End of Chicken")
    return wallet