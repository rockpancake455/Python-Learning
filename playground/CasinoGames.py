from random import randint
from time import sleep
import UserInput

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
    symbols = ["Orange","Cherry","BAR","Star","Bell","Soda"]
    winnings = 0 
    
    # Accessing Lists
    # variable = symbols[0]
    # symbols[0] = variable
    
    while wallet > 10:
        userInput = input("Press [Enter] to spin the slots!\nOr enter [E] to exit!")
        if userInput.upper() == "E":         
            break
            
        print("You inserted 10 coins!")
        wallet -= 10
        
        slots = []
        for index in range(0,3):
            sleep(1)
            slots.append(symbols[randint(0,5)])
            print(f"[{slots[index]}]")

        if slots[0] == "BAR" or slots[1] == "BAR" or slots[2] == "BAR":
            print("Oh No! BAR! Try again!")
        elif slots[0] == slots[1] == slots[2]:
            winnings = 200
            print("Yahoo!! You gat a triple and won 200 coins!")
        elif slots[0] == slots[1] or slots[0] == slots[2] or slots[1] == slots[2]:
            winnings = 20
            print("You got a double! You won 20 coins!")
        else:
            print("No Match! Try again!")

        wallet += winnings
        winnings = 0
        print(f"You now have {wallet} coins!\n")
    
    print("End of Slots!")
    return wallet
    
# 
# Chicken:  The computer will generate a random number from 1-100.
#           The user will enter a number that they want to bet.
#           If the user's number is <= the random number they win and double the money they bet.
#           If the user's number is > the random number they lose and lose the money they bet.
#           
# Other Goals:
#           Use the wallet and keep track of how much money the players has.
#           Don't allow the user to bet more than they have. <To-Do>
#           Don't allow the user to bet more than 100 coins and less than 1 coin.
#           Check user input for garbage. -> Use GetUserAnswer() method.
#           Kick the user out when the user bets "1-4" three times in a row.
#           Kick the user out when the user bets "1-4" more than 1/3 (33%) of the time.
#           Allow the user to exit by entering "E" into the terminal. <To-Do>
#

def Chicken(wallet: int):
    
    repeatLowBetCount: int = 0
    totalGuesses: int = 0
    totalLowGuesses: int = 0

    while wallet > 0:
    
        msg = "Please enter a bet from 1 to 100.\nor you can leave by entering [E]"
        userBet = UserInput.GetUserRange(msg, range(1,101), int)
        randomBet = randint(1,100)
        totalGuesses += 1

        if userBet in range(1,5):
            totalLowGuesses += 1
            repeatLowBetCount += 1
        else:
            repeatLowBetCount = 0

        if repeatLowBetCount >= 3 or (totalLowGuesses / totalGuesses) > 0.33 and totalGuesses > 10:
            print("Hey!\nYour cheating!\nGet out of here!!")
            break

        print(f"Your Bet: {userBet}")
        sleep(1)
        print(f"House Bet: {randomBet}")
        sleep(1)
            
        if userBet <= randomBet:
            print("\nYou Win!\nCongratulations!!!")
            wallet += userBet + userBet
        elif userBet > randomBet:
            print("\noops!\nYou lost your bet!\nBetter luck next time!")
            wallet -= userBet
            
        print(f"You now have {wallet} coins in your wallet!")

    print("End of Chicken")
    return wallet