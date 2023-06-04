from random import randint
import time
# Roll of The Many Dice
# 
# Purpose: Create a program that allows the user to roll 2D6 1-1000 times.
# 
# Step 1: Greet the user! 
# Step 2: Ask the user how many dice they want to roll.
# Step 3: Roll 2 D6 the number of times given by the user.
# Step 4: Give information and statstics on the dice rolls.
#   - Total of all rolls.
#   - How many times each result was rolled.
#       -  2: <->
#       -  3: <-->
#       -  4: <--->
#       -  5: <------>
#       -  6: <-------->
#       -  7: <----------->
#       -  8: <-------->
#       -  9: <------>
#       - 10: <--->
#       - 11: <-->
#       - 12: <->

def FindMax(myList: list[int]):
    biggestValue = 0
    for value in myList:
        if value > biggestValue:
            biggestValue = value
    return biggestValue
print("Hello, Welcome to the world greatest dice roller part two.")

while True:
    try:
        numberPicked = int(input("How many dice do you want to roll?\nType a number between 1 and 1000."))
        if (numberPicked >= 1 and numberPicked <= 1000):
            break
        else:
            print("Invalid input: Please try again.")
    except:
        print("Please provid a number.")

totalSum = 0
#count           0  0  0  1  0  1  1  2  0  1  0  0  0  
#unique numbers  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12
rollCount =      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for rollAgain in range(0, numberPicked):

    print("Rolling the dice!!")

    dice1 = randint(1,6)
    dice2 = randint(1,6)
    sum = dice1 + dice2
    totalSum = sum + totalSum

    rollCount[sum] += 1
    

    print(f"You rolled: {dice1} and {dice2} for a total of {sum}.")

print(f"Your total of {numberPicked} rolls is {totalSum}!!")
print(f"roll count{rollCount}\n")

print("display")
# it would go in torollcount fine 2 a print the count of 2 and to the same thing up to 12

# def MyRange(number1: int, number2: int): # number1 = int(1), number2 = int(7)
#     index = number1
#     outputList = [int]
#     while index != number2:
#         outputList.append(index)
#         index += 1
#     return outputList #[0, 1, 2, 3, 4, 5]

# range(0, 4) [0, 1, 2, 3]

# If max count = 13 then 13 will = 20 equal signs.
# Scale Factor = 20/13 
# Value = 13 * ScaleFactor (1.53846) => 20
#
# Value = 5 * ScaleFactor (1.53846) => 7.6923
#

# for index in range(2, 13): #range = [2, 3, 4, 5, 6, 7, 8, ...]
#     print("="*rollCount[index])

maxCount = FindMax(rollCount)

scaleFactor = 20 / maxCount
print(f"Max Count= {maxCount} & Scale Factor = {scaleFactor}!")
for index in range(2,13):
    print("{:>2}: |".format(index)+ "="*round(rollCount[index]*scaleFactor) + ">")

# Display something like the following:
#
#       -   2:  =
#       -   3:  ==
#       -   4:  ===
#       -   5:  =======
#       -   6:  ==========
#       -   7:  ============
#       -   8:  ==========      
#       -   9:  =======
#       -   10: === 
#       -   11: ==  
#       -   12: =
#       
#Display and "=" for every time a unique number was rolled.  
# 
# if 6 was rolled 4 times output: ====
# if 6 was rolled 6 times output: ======
# 
# Hint: "="*5 -> "====="
# 

print("\n\nEnd of Program")