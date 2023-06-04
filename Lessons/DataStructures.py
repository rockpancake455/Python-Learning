# Data Structures

# Dictionaries
# Lists
# Classes

# region Dictionaries

# myDictionary = {0: "Yes", 1: "Maybe", 2: "No", 55212: "Mabery"}
# myDictionary2 = {"Cookies": 0, "Toast": 1, "Waffles": 2}
# myDictionary3 = {1: 1.5, 2: 2.89, 3: 3.88}

# print(myDictionary2["Toast"])

# endregion

# region List

myVowls = ["a","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","i","o","u",]

# myVowls.append()
# myVowls.remove()
# myVowls.clear()
# myVowls.count()

# Does "myVowls" have 1 letter e? = False 
# Does "myVowls" not have 1 e? = True ["a", "i", "o", "u",]
# Does "myVowls" have greater or equal to 1 e? 

print (myVowls)

while myVowls.count("e") > 1:
    myVowls.remove("e")
    print("I am removing an 'e'")
    
print(myVowls)

 # u o i e a
# endregion

print("End of program :)")
