from time import sleep
from PythonUI import *
import blessed

ConfigureTerminal(blessed.Terminal())

PrintCenter("Welcome to PythonUI Demo!")
sleep(2)

response = SelectFromList("Select an option", ["Option A","Option B"])
PrintCenter(f"You selected {response}!")
sleep(2)

response = QueryNumber("Input a number\nOnly a number", 0, 100, False)
PrintCenter(f"Your number is {response}!")
sleep(2)

response = QueryWord("Input a word\nOnly a word!")
PrintCenter(f"Your word is {response}")
sleep(2)

print("<EOP>")