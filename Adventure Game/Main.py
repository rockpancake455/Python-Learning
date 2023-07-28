from random import randint
import PythonUI, blessed, GameMenus, Player, MailBox, time, os
# from Player import Instance
PythonUI.ConfigureTerminal(blessed.Terminal())
time.sleep(1)
"""
Game system
Want to be able to go on quests/encounters/contracts
Fight enemies
Use different weapons - Sword, Daggers, Bows, 
Player inventory
Turn based combat
Chance based attacks
Player skills
"""
MailBox.MailBox.append(MailBox.Letter("Guardians of the Caravan","Hello good sir I would like you to join our caravan to transport\n some goods to the noble king and if you acssept ill gift you 50 coin for your protispation", "Lord Cedric Ironhelm"))
MailBox.MailBox.append(MailBox.Letter("The Golden Griffin", "Hello adventurer!\nHave you heard of the lost golden Griffin?", "Jacob Herndon"))
MailBox.MailBox.append(MailBox.Letter("The Golden Griffin", "Hello adventurer!\nHave you heard of the lost golden Griffin?", "Jacob Herndon"))

while True: 
    playerAction = GameMenus.Home()

    # Craft
    # Check Mail
    # Go on Quest
    # Rest - Done3

    # if player action is Check mail
    # - Check the mailbox -> GameMenus menu
    if playerAction == GameMenus.HomeActions.Rest:
        GameMenus.Rest()
    if playerAction == GameMenus.HomeActions.Mail:
        GameMenus.Mail()

        
        


PythonUI.PrintBold("[END OF GAME]")
PythonUI.PressToContinue()