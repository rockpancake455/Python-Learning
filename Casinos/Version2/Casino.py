from CasinoGames import *
from PythonUI import *
from blessed import Terminal
from time import sleep

wallet = 100

sleep(1)
ConfigureTerminal(Terminal()) #Sets up the Python UI library
PrintTerm("Hello! Welcome to Jacob's casino of doom 2.0")
PressToContinue()

while True:
    response = SelectFromList("Pick a game!", ["Slots","Chicken","Roulette","Exit"])
    PrintTerm(f"You selected {response}!")
    PressToContinue()
    
    # Play selected game
    if response == "Slots":
        wallet = Slots(wallet)
    elif response == "Chicken":
        wallet = Chicken(wallet)
    elif response == "Exit":
        break
    
PrintBold("Good bye!")
sleep(1)