from random import randint
import PythonUI, blessed, GameMenus, Player, MailBox, time, Questing, os
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


caravanQuest = Questing.Quest("Guardians of the Caravan", [Questing.Reward(Questing.ResourceNames.Coins, 300)], Questing.CaravanGuard)
MailBox.MailBox.append(MailBox.Letter("Guardians of the Caravan", "Hello good sir, I would like you to join our caravan to transport\n some goods to the noble king. If you join us,\n you will be gifted 300 coins for your protection.", "Mr.Vanguard", caravanQuest))

while True: 
    playerAction = GameMenus.HomeMenu()

    # Craft
    # Check Mail
    # Go on Quest
    # Rest - Done3

    #plays any action the player wants to run
    if playerAction == GameMenus.HomeActions.Rest:
        GameMenus.RestMenu()
    if playerAction == GameMenus.HomeActions.Mail:
        GameMenus.MailMenu()
    if playerAction == GameMenus.HomeActions.Quest:
        GameMenus.QuestMenu()

PythonUI.PrintBold("[END OF GAME]")
PythonUI.PressToContinue()