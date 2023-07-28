import PythonUI, Player, MailBox, time

class UIItems:
    DIV = "="*60

class HomeActions:
    Craft = "Craft"
    Mail = "Check Mail"
    Quest = "Go on a Quest"
    Rest = "Rest"

#player has options to do in side the house
def Home():
    playerAction = PythonUI.SelectFromList(f"{UIItems.DIV}\nHealth: {Player.Instance.Health}\n{UIItems.DIV}\nWelcome Home!\nWhat do you want to do?\n{UIItems.DIV}",
                            [HomeActions.Craft, HomeActions.Mail, HomeActions.Quest, HomeActions.Rest])
    return playerAction

#You go to sleep and heal up
def Rest():
    PythonUI.ClearTerm()
    PythonUI.PrintBold("You fall asleep...")
    for i in range(0, 3):
        PythonUI.PrintTerm(".")
        time.sleep(1)
    Player.Instance.Heal_Max()
    PythonUI.PrintBold(f"You rested and now have {Player.Instance.Health} health!")
    PythonUI.PressToContinue()

#You open the mail to check quests
def Mail():
    letterHeaders: list[str] = []
    for i in range(0, len(MailBox.MailBox)):
        letterHeaders.append(MailBox.MailBox[i].GetHeader())
    # for item in MailBox.MailBox:
    #     letterHeaders.append(item.GetHeader())
    selection = PythonUI.SelectFromList("[Mail Box]", letterHeaders)
    PythonUI.PrintBold(f"You slected: {selection}")
    PythonUI.PressToContinue()

# CheckMail/Mailbox/Mail
    # Display all of the mail in mailbox
    # - Display the mail by the title of the mail item
    # Allow the user to pick a mail item to open
    # - Display them message and who it is from

# Make a mail class in a seperate file
    # - Mail message
    # - Title
    # - Sender