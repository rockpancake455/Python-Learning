from random import randint
from PythonUI import *
from time import sleep

# 
# Make a list of symbols (BAR, cherry, lollypop, etc...)
# Make the game cost 10 coins to play.
# If the user doesn't have 10 coins they can't play!
# Pick a symbol at random for all three slots
# if all three slots match up you win the jackpot of 200 coins!
# if two symbols match you win the mini pot of 20 coins!
# if get a BAR then you automatically lose.
# 
def Slots(wallet: int):
    symbols = ["Orange","Cherry","BAR","Star","Bell","Soda","tucker hat","game controller"]
    winnings = 0 
    
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
        
        # Checks for win/loose conditions
        if slots[0] == "BAR" or slots[1] == "BAR" or slots[2] == "BAR":
            PrintTerm("Oh No! BAR! Try again!")
        elif slots[0] == slots[1] == slots[2]:
            winnings = 200
            PrintTerm("Yahoo!! You gat a triple and won 200 coins!")
        elif slots[0] == slots[1] or slots[0] == slots[2] or slots[1] == slots[2]: #Check for two slots matching
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

# 
# Chicken:  The computer will generate a random number from 1-100.
#           The user will enter a number that they want to bet.
#           If the user's number is <= the random number they win and double the money they bet.
#           If the user's number is > the random number they lose and lose the money they bet.
#           
# Other Goals:
#           Use the wallet and keep track of how much money the players has.
#           Don't allow the user to bet more than they have.
#           Don't allow the user to bet more than 100 coins and less than 1 coin.
#           Check user input for garbage. -> Use GetUserAnswer() method.
#           Kick the user out when the user bets "1-4" three times in a row.
#           Kick the user out when the user bets "1-4" more than 1/3 (33%) of the time.
#           Allow the user to exit by entering "E" into the terminal.
#
def Chicken(wallet: int):
    # Variables used to detect when the user is cheating.
    totalGuesses: int = 0
    totalLowGuesses: int = 0
    repeatLowBetCount: int = 0

    while wallet > 0:
        # Gets the user's bet and generates the house's bet.
        msg = (f"Please enter a bet from 1 to {wallet}.")
        userBet = QueryNumber(msg, 0, wallet, False)
        houseBet = randint(1,100)
        if userBet == "e":
            break
        
        # Logging user's bet to detect cheating.
        totalGuesses += 1                    
        if userBet in range(1,5):
            totalLowGuesses += 1
            repeatLowBetCount += 1
        else:
            repeatLowBetCount = 0
        # Cheat detection, kicks out user.
        if repeatLowBetCount >= 3 or (totalLowGuesses / totalGuesses) > 0.33 and totalGuesses > 10:
            PrintBold("Hey!\nYou're cheating!\nGet out of here!!")
            break

        PrintBold(f"Your Bet: {userBet}")
        sleep(1)
        PrintBold(f"House Bet: {houseBet}")
        sleep(1)

        # Checks if the user wins or looses
        if userBet <= houseBet:                                               
            PrintTerm("\nYou Win!\nCongratulations!!!")                     
            wallet += userBet + userBet                                     
        elif userBet > houseBet:                                               
            PrintTerm("\noops!\nYou lost your bet!\nBetter luck next time!")  
            wallet -= userBet                                                   
                    
        PrintTerm(f"You now have {wallet} coins in your wallet!")              
        PressToContinue()  

        if SelectFromList("Do you want to leave Chicken?", ["Yes","No"]) == "Yes":
            break                                      

    PrintTerm("End of Chicken")
    return wallet

# 
# Roulette:
# Player bets on either red or black and gives a bet ammount.
# The wheel is spun.
# There is a 50/50 chance for either red or black to win.
# If the user bet on the right color they win and double their bet.
# Allow the user to exit either on the red/black pick or at the end.
# 
def Roulette(wallet: int):

    wheelcolor = ["Red","Black"]
    
    while wallet > 0:
        
        #Gets the user's guess and bet and wheels color
        usercolor = SelectFromList("What color will it land on?",["Red","Black"])
        wheelspin = (wheelcolor[randint(0,1)])
        msg = (f"And how mutch will you bet on from 10-{wallet}?")
        userbet = QueryNumber(msg, 10, wallet, True)
    
        #Spins the wheel
        PrintTerm("The dealer is spinning the wheel!")
        for i in range(1,5):
            sleep(1)
            PrintTerm(".")
    
        PrintTerm(f"The ball landed on {wheelspin}!")
        PressToContinue()

        #Checks if you win or loose
        if usercolor == wheelspin:
            PrintBold("Hooray, you guessed correctly!")
            wallet += userbet
        else:
            PrintBold("Oops!,better luck next time.")
            wallet -= userbet

        PrintTerm(f"You now have {wallet} in your wallet.")
        PressToContinue()

        if SelectFromList("Do you want to leave Roulette?", ["Yes","No"]) == "Yes":
            break                                      

    PrintTerm("End of Roulette")
    return wallet