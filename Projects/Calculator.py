# Purpose: Make a simple program to do simple mathematical fucntions.
#
# Step 1: Greet the user.
# Step 2: Ask for the first number. 
# Step 3: Ask for the second number.
# Step 4: Ask for the function. [+, -, x, /]
# Step 5: Give the result back to the user.
#   a. number1 [function] number2, ex. number1 + number2


def GetUserAnwser(message: str, validAnswers: list, castType: type):
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

# we first greet the user
print ("hello wellcome to caculicious calculator")
calculateAgain = "YES"
#This entire code is inside a big o loop and it checks if calculateAgain is in the list if not it will stop and print end of program
while calculateAgain.upper() in ["YES","Y"]:
    #Get the first number from the user
    firstNumber = int(GetUserAnwser("What is your first number? [+100k to -100k]", range(-100000, 100000), int))
    #Get the second number from the user
    secondNumber = int(GetUserAnwser("What is your second number? [+100k to -100k]", range(-100000, 100000), int))
    #Get the function from the user
    function = str(GetUserAnwser("What Function? [+, -, x, *, /]", ["+","-","x","*","/"], str))
    
    # Calcuate the answer
    if function == "+":
        total = firstNumber + secondNumber
    elif function == "-":
        total = firstNumber - secondNumber
    elif function.upper() in ["X","*"]:
        total = firstNumber * secondNumber     
    elif function == "/":
        total = firstNumber / secondNumber

    #Then it will print out total
    print(f"Your answer is {total}!")
    #Finaly it will ask the user if they want to do another equation 
    calculateAgain = input("Do you want to calculate another equation? [Yes or No]")

print("End of Program")