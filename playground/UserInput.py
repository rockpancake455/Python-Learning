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

def getUserRange(message: str, type2: type):
    while True:
        try:
            userInput = type2(input(message))
            if(userInput in range(1,101)):
                break
            else:
                print(f"Error: Invalid Answer!")

        except:
            print(f"Error: Invalid Answer!")
    return userInput