import PythonUI, Player, MailBox, Questing, time

class UIItems:
    DIV = "="*60

class HomeActions:
    Craft = "Craft"
    Mail = "Check Mail"
    Quest = "Go on a Quest"
    Rest = "Rest"

#Displays the home menu
def HomeMenu():
    playerAction = PythonUI.SelectFromList(f"{UIItems.DIV}\nHealth: {Player.Instance.Health}\n{UIItems.DIV}\nWelcome Home!\nWhat do you want to do?\n{UIItems.DIV}",
                            [HomeActions.Craft, HomeActions.Mail, HomeActions.Quest, HomeActions.Rest])
    return playerAction

#You go to sleep and heal up
def RestMenu():
    PythonUI.ClearTerm()
    PythonUI.PrintBold("You fall asleep...")
    for i in range(0, 3):
        PythonUI.PrintTerm(".")
        time.sleep(1)
    Player.Instance.Heal_Max()
    PythonUI.PrintBold(f"You rested and now have {Player.Instance.Health} health!")
    PythonUI.PressToContinue()

# You open the mail to check quests or exit
def MailMenu():
    # Builds a list of headers + an exit option to select from
    letterHeaders: list[str] = []
    for item in MailBox.MailBox:
        letterHeaders.append(item.GetHeader())
    letterHeaders.append("Exit")

    # Displays all of the letterheaders  
    selection = PythonUI.SelectFromList("[Mail Box]", letterHeaders)
    if selection == "Exit":
        return
    
    # Back trace the selected letter 
    mailIndex = letterHeaders.index(selection)
    selectedLetter = MailBox.MailBox[mailIndex]

    MailBox.MailBox.remove(selectedLetter) 
    Questing.AvailableQuests.append(selectedLetter.LinkedQuest)

    PythonUI.PrintTerm(selectedLetter.GetMessage())
    PythonUI.PressToContinue()

# AvailableQuests               questTitles
#  [0] Quest                     [0] Caravan
#  [1] Quest <------------------ [1] Guard
#  [2] Quest                     [2] Pest Control

# Pick a quest to play or exit
def QuestMenu():
    # Builds a list of quest titles
    questTitles: list[str]= []
    for q in Questing.AvailableQuests:
        questTitles.append(q.Title)
    questTitles.append("Exit")  

    # Pick from the list of quests
    selection = PythonUI.SelectFromList("What adventure do you want to go on?", questTitles)
    if selection == "Exit":
        return
    
    # Back trace to selected quest
    selectionIndex = questTitles.index(selection)
    questToPlay: Questing.Quest = Questing.AvailableQuests[selectionIndex]

    questToPlay.Play()
    PythonUI.PressToContinue()