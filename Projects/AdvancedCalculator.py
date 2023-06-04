# Purpose: To make a calculator using a class.
#
# Make a Class called "Calculator"
#   - Properties
#       - First Number
#       - Second Number
#       - Result
#   - Functions:
#       - Add 
#       - Subtract
#       - Multiply
#       - Divide

# Suedo Code
#
# myCalc.Number1 = 10
# myCalc.Number2 = 5
# myCalc.Add()
# print(myCalc.Result) -> [Terminal: 15]
#
# myCalc.Number1 = 10
# myCalc.Number2 = 5
# myCalc.Subtract()
# print(myCalc.Result) -> [Terminal: 5]

# Program Steps:
#   - Step 1: Get Num1 from the user
#   - Step 2: Get Num2 from the user
#   - Step 3: Get a function from the user
#   - Step 4: Show the user the result

class calculator:

    FirstNumber =  ""
    SecondNumber = ""
    Function = ""

    Total = ""

    def __init__(self,firstnumber: int,secondnumber: int,function: str):
        self.FirstNumber = firstnumber
        self.SecondNumber = secondnumber
        self.Function = function
        
        if self.Function == "+":
            self.Total = self.FirstNumber + self.SecondNumber
        elif self.Function == "-":
            self.Total = self.FirstNumber - self.SecondNumber
        elif self.Function.upper() in ["X","*"]:
            self.Total = self.FirstNumber * self.SecondNumber
        elif self.Function == "/":
            self.Total = self.FirstNumber / self.SecondNumber
        
        print(f"your anser is {self.Total}\nend of program")

    
        
equation = calculator(firstnumber=int(input("what is your first number?:")), secondnumber = int(input("what is your second number?:")), function = str(input("what is your function? ex:+ - x * and / :")))

#
# myCalc = Calculator()
# myCalc.FirstNumber = input("")
# myCalc.SecondNumber = input("")
# myCalc.Function = input("")
# 
# if myCalc.Function == "+"
#   myCalc.Add()
# elif myCalc.Function == "-"
#   myCalc.Subtract()
#