# Hello User Application
# Function: Asks user for their name and then says "Hello (name)!"
# 
# Step 1: Greet the user and ask for their name.
# Step 2: Get the user's name
# Step 3: Say "Hello (name)!"
# 
#

def GetGreetings(firstname, lastname):
    print(f"hello, wellcom abord {firstname} {lastname}" )

def CheckUserInput(userInput: str, validAnswers: list[str]):

    if userInput in validAnswers:
        return True
    else:
        return False

print("hello wellcome to greetings\n question, what is your first name?")
GreetingFirstname = input()
print("and finally, what is your last name?\nif you dont want to put nothing.")
GreetingLastname = input()

GetGreetings(GreetingFirstname, GreetingLastname)

print("\nHow are you doing?\nYour options are: good, bad, fine or asian.")

userAnswers = input()
while not userAnswers in ["good", "bad", "fine", "asian"]:
    print("\nThat is an invalid answer\nYour options are: good, bad, fine or asian.")
    userAnswers = input()

if userAnswers== "good":
    print("I'm a computer so I dont care on how you feel ")
elif userAnswers== "bad":
    print("I'm a computer so I dont care on how you feel the curect answer was good")
elif userAnswers== "fine":
    print("I'm a computer so I dont care on how you feel")
elif userAnswers== "asian":
    print("goaway!")
else:
    print("")

print("end of program")

# print(f"hello {greetingfirstname} {greetinglastname}")