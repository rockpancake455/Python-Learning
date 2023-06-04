#================================================
#   Password Generator
#   Made By: Jacob Herndon & Taylor Herndon
#   Date: 04/15/23
#================================================

# High Level 
# - Generate a password.
# - The passord must be secure.
#   - More characters.
#   - Doesn't follow patterns.
#   - Special Characters.
# - User gives perameters on how the password is generated.

# Pesudo Code
# 
# -- Program Start --
# Ask the user for perameters.
#  - How many characters do you want? / How long should the password be? (4 characters or 10 characters)
#  - How scambled do you want your password? [Low, Mid, High]
#  - Do you want to use special characters? [Y/N]
#  - Do you want the password segmented? [Y/N] [xxx-xxx-xxx-xxx]
#     
# Ask the computer to generate three possible passwords.
#  - Inputs: Length: int, How Scrambled: Enum, Special Characters: bool, Segmented: bool 
#  - Generate a string as long as the length input. 
#  - Output: str
#
# User chooses if they want to generate more.

class ScrambledLevels:
    Low = 0
    Mid = 1
    High = 2

# Input: userInput: String: Any input from the user
# Input: function: String: ["Length","Scrambled","Special Chars","Segmented"]
# Does: checks for response validity, 
# Returns: True: Good, False: Bad
def CheckUserInput(userInput: str, validResponses: list[str], convertToLower = False): 
    
    if convertToLower:
        userInput = userInput.lower()
        for i in range(0, len(validResponses)):
            validResponses[i] = validResponses[i].lower()

    if userInput in validResponses:
        return True

# region Main Program Start
print("-- Program Start --")

print("Hello User!\nHow long do you want your password?\n[6-12]")
response = input()
CheckUserInput(response, ["6","12"])

#How Scrambled?
CheckUserInput(response, ["High","Mid","Low"])

print("-- Program End --")
# endregion