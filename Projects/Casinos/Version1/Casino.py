from random import randint
import CasinoGames
import UserInput
from time import sleep
sleep(1)

wallet = 100 #coins
play = "Yes"

while play.upper() in ["YES","Y"]:
    
    msg = "Hello!\nWelcome to Jacob's Casino of DOOM!\nWhat do you want to play?\n[1]: Slots\n[2]: Chicken\n"
    gameSelection = UserInput.GetUserAnswer(msg, [1,2], int)

    if gameSelection == 1: #Slots
        wallet = CasinoGames.Slots(wallet)
    elif gameSelection == 2: #Chicken
        wallet = CasinoGames.Chicken(wallet)
    # cards like War?

    play = UserInput.GetUserAnswer("Do you want to play another game?\n[Yes,No]", ["Yes","yes","Y","y","No","no","N","n"], str)

print("End of Program")