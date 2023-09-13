
# Dictionary
# Essentially a translator
# A way to convert one value to another

# myDict = {
#     "AppleJuice": True,
#     "OrangeJuice": 2,
#     "GrapeJuice": "Yuk",
#     "LemonJuice": [5.01, 10.02, 15.03]
# }

# print(myDict["AppleJuice"])
# print(myDict["OrangeJuice"])
# print(myDict["GrapeJuice"])
# print(myDict["LemonJuice"])

# For Loop
# A loop that is used to repeat an action a specific/known number of times.

# Simple repeat code x times

# x = 5
# for index in range(0, x):
#     print("*"*index)

# 
# *
# **
# ***
# ****

# Itterate through a group of values (list)

myStrings = ["A", "B", "C", "D", "E"]

x = len(myStrings)
for index in range(0, x):
    currentItem = myStrings[index]
    print(currentItem)

for currentItem in myStrings:
    print(currentItem)