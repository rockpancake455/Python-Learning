from CasinoGames import *
from PythonUI import *
from blessed import Terminal
from time import sleep
import os
#
# In the same directory as Casino.py
# Read from a text file -> Wallet.txt
# Convert the read text to a integer and assign it to wallet.txt = int 
#
# Check if the file exists before reading from it. (os.path.exists("FilePath"))
# try-catch when converting to integer.
#
walletDirectory = "C:\\Users\\teton\\python folder1\\Casinos\\Version2\\"
fileName = "Wallet.txt"
wallet: int = 0

if not os.path.exists(walletDirectory + fileName):
    file = open(walletDirectory + fileName, 'w')
    file.write("100.0")
    file.close()

file = open(walletDirectory + fileName, 'r')
walletText = file.read()
file.close()

if walletText == "":
    walletText = "100"

walletFloat = float(walletText)
wallet = int(walletFloat)

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
    elif response == "Roulette":
        wallet = Roulette(wallet)
    elif response == "Exit":
        break
    
PrintBold("Good bye!")
sleep(1)

wallet = str(wallet)

file = open(walletDirectory + fileName, 'w')
file.write(wallet)
file.close()

# In the same directory as Casino.py
# open the file, as a write -> Wallet.txt
# write the current wallet as a string to the file