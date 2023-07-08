from casinoplays2 import *
from PythonUI import *
from blessed import Terminal
from time import sleep

sleep(1)
ConfigureTerminal(Terminal())
wallet = 100
PrintTerm("Hello! Welcome to Jacob's casino of doom 2.0")



#response = SelectFromList("Your options are 1 for chicken 2 for slots", [1,2])
response = SelectFromList("Pick a game!", ["Slots","Chicken"])
PrintTerm(f"You selected {response}!")
PressToContinue()

if response == "Slots":
    wallet = Slots(wallet)
elif response == "Chicken":
    wallet = Chicken(wallet)