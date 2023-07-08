from blessed import Terminal
from time import sleep
import string

def ConfigureTerminal(t: Terminal):
    """
    Passes the terminal reference to the PythonUI library.\n
    Required to use the PythonUI library.
    """
    global term
    term = t
    print(term.green)

def ClearTerm():
    """
    Clears the terminal.
    """
    print(term.home + term.clear)

def PrintCenter(message: str):
    """
    Will print a given string centered-aligned in the terminal.
    """
    splitMessage = str.split(message, '\n')
    for msg in splitMessage:
        print(term.green + term.center(msg))

def PrintHeader(headerMessage: str):
    ClearTerm()
    headerMessageLines = str.split(headerMessage, '\n')
    print("")
    for line in headerMessageLines:
        print(term.green + term.bold(term.center(line)))
    print("")

def SelectFromList(queryMessage: str, inputOptions: list[str]):
    """
    Will print the query message and each of the input options with a coresponding number.\n
    The user will must enter the number coresponding to their desired selection.\n
    Returns the selected option.
    """
    with term.cbreak(), term.hidden_cursor():
        while True:
            #Printing query message and input options
            PrintHeader(queryMessage)
            for i in range(0, len(inputOptions)):
                print(term.green + term.center((f"[{i}] {inputOptions[i]}")))

            #Taking user input
            try:
                response = int(term.inkey())
            except:
                continue
            if response in range(0, len(inputOptions)):
                return inputOptions[response]
        
def QueryNumber(queryMessage: str, minInput: int, maxInput: int, intOnly: bool = False): 
    """
    Will print the query message and will take a number as an input from the user.
    The user can only input numbers and a single decimal point.
    User input can be restricted by validRange. The input number must be in this range.
    User input can be restricted by intOnly. If true, the user must give an whole number.
    """
    validInputs = ["0","1","2","3","4","5","6","7","8","9","."]

    runningInput = ""
    with term.cbreak(), term.hidden_cursor():
        while True:
            #Print out query message
            PrintHeader(queryMessage)
            print(term.green + term.center(f"[{runningInput}]"))

            #Take input from user
            nextInput = term.inkey()

            #If input is [Enter] key, test if the running input is valid
            if nextInput.name == "KEY_ENTER":
                castInput = None
                if intOnly:
                    castInput = int(runningInput)
                else:
                    castInput = float(runningInput)

                if castInput > minInput and castInput < maxInput:
                    return castInput
                runningInput = ""

            #If backspace key, remove the last character that was input
            if nextInput.name == "KEY_BACKSPACE":
                if runningInput == "":
                    continue
                runningInput = runningInput[:-1]
                continue
            
            #If input is not [Enter], check if it is a valid input
            if not nextInput in validInputs:
                continue
            if nextInput == "." and runningInput.count(".") != 0 or nextInput == "." and intOnly:
                continue
            runningInput += nextInput

def QueryWord(queryMessage: str):
    """
    Will print the query message and will take a single word as an input.
    """
    validInputs = string.ascii_letters

    runningInput = ""
    with term.cbreak(), term.hidden_cursor():
        while True:
            #Print out query message
            PrintHeader(queryMessage)
            print(term.green + term.center(f"[{runningInput}]"))

            #Take input from user
            nextInput = term.inkey()

            #If input is [Enter] key, test if the running input is valid
            if nextInput.name == "KEY_ENTER" and runningInput != "":
                return runningInput
            
            #If backspace key, remove the last character that was input
            if nextInput.name == "KEY_BACKSPACE":
                if runningInput == "":
                    continue
                runningInput = runningInput[:-1]
                continue

            #If input is not [Enter], check if it is a valid input
            if not nextInput in validInputs:
                continue
            runningInput += nextInput