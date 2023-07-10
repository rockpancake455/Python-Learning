def GetUserAnswer(message: str, validAnswers: list, castType: type):
    while True:
        try:
            userInput = castType(input(message))
            if (userInput in validAnswers):
                break
            else:
                print(f"Error: Invalid Answer!")
        except:
            print(f"Error: Invalid Answer!")
    return userInput

def GetUserRange(message: str, validRange: range, castType: type):
    while True:
        try:
            userInput = castType(input(message))
            if(userInput in validRange):
                break
            else:
                print(f"Error: Invalid Answer!")
        except:
                print(f"Error: Invalid Answer!")
    return userInput

def GetUserRangeWithExit(message: str, validRange: range, castType: type):
    while True:
        try:
            userInput = input(message)
            if(userInput == "e"):
                break
            userInput = castType(userInput)          
            if(userInput in validRange):
                break
            else:
                print(f"Error: Invalid Answer!")
        except:
                print(f"Error: Invalid Answer!")
    return userInput

# Input
# Test if "e"
# Cast
# Test number
