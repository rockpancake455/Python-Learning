from random import randint
import time
# Roll of the Dice
# 
# Purpose: Create a program that will allow the user to roll a dice.
# 
# Step 1: Greet the user.
# Step 2: Once the user presses enter roll a D6 dice.
# Step 3: Show the result to the user.
# 
# Possible Features:
# - Rolling other types of dice (D4, D8, D12, D20, D100)
# - Rolling more than one dice
def CheckUserInput(userInput: str, validAnswers: list[str]):
    if userInput in validAnswers:
        return True
    else:
        return False
    
#Greet the user
print("Hello, Welcome to the world greatest dice roller.")
rollAgain = "yes"

#Puting this entire dice roller in one big loop so that it can be done multiple times
while rollAgain.upper() in ["YES","Y"]:

    print("What kind of dice do you want to roll?\nYour Options: [D4:D6:D8:D10:D12:D20]")
    diceChoice = input("Your Choice: ").upper().replace("D","") 

    while not CheckUserInput(diceChoice, ["4","6","8","10","12","20"]):
        print("Invalid Input.\nYour Options: [D4:D6:D8:D10:D12:D20]")
        diceChoice = input("Your Choice: ").upper().replace("D","") 

    #Tell the user to press enter.
    input("\n\nPress [Enter] to roll.")
    print("Rolling Dice!")
    for i in range(0,3):
        time.sleep(1)
        print(".")

    #We have two dice and they will be rolled.
    dice1=randint(1, int(diceChoice))
    dice2=randint(1, int(diceChoice))
    print(f"You rolled a: {dice1} and a {dice2}!")
    
    #What if you are playing a game that requir's you to add up
    inTotal=dice1+dice2
    print(f"Sum = {inTotal}.")

    #To tell the user that they have a double.
    if dice1 == dice2:
        print("You have a double!")
    else:
        print("Hay!, Keep trying to get a double!")

    #Ask the user if they want to keep going or not.
    rollAgain = input("Do you want to roll again?\n(yes or no)")

print("End of Program")