import PythonUI

class ResourceNames:
    Coins = "Coin"
    Iron = "Iron"
    Wood = "Wood"
    Fabric = "Fabric"

class Reward:
    
    Name: ResourceNames
    Qty: int

    def __init__(self, name: ResourceNames, qty: int):
        self.Name = name
        self.Qty = qty
        
class Quest:

    Title: str
    Rewards: list[Reward]
    QuestLine: any
    
    def __init__(self, title: str, rewards: list[Reward], questLine: any):
        self.Title = title
        self.Rewards = rewards
        self.QuestLine = questLine

    def Play(self):
        self.QuestLine()

    def Payout(self):
        PythonUI.PrintBold("Your Rewards:")
        PythonUI.PrintTerm(self.Rewards)


AvailableQuests: list[Quest] = []

#=================================================
#                  Quests
#=================================================

# region Carvan Guard

def LeftPath():
    PythonUI.PrintTerm("You head down the left path, hoping to avoid any touble with bandits.")
    PythonUI.PrintTerm("After a few days you stop in a small clearing to setup camp.")
    PythonUI.PrintTerm("After everything has been setup for the night you take the first watch.")
    PythonUI.PrintTerm("Late into your watch you think you heard something moving in the brush behind you.")
    PythonUI.PressToContinue()
    PythonUI.ClearTerm()

    #checks if the player wins or looses
    combatResult: bool
    action = PythonUI.SelectFromList("What do you do?", ["Wake the caravan","It's probably nothing"])
    if action == "Wake the caravan":
        # === Start Combat ===
        combatResult = True
    elif action == "It's probably nothing":
        # === Start Combat ===
        combatResult = False
  
    if not combatResult:
        return False

    PythonUI.ClearTerm()
    PythonUI.PrintTerm("You valiantly defended the caravan from the wolf!")
    PythonUI.PrintTerm("Mr.Vanguard thanks you for your quick action in defending the caravan and rewards you with a healing potion.")
    PythonUI.PrintTerm("Once everything has died down you get to harvesting the wolf.")
    PythonUI.PrintBold("+1 Healing Potion, +1 Wolf Hide, +5 Meat")
    PythonUI.PressToContinue()
    PythonUI.ClearTerm()
    return True
    
def RightPath():
    PythonUI.PrintTerm("You head down the right path, you feel confident that we might not encounter any bandits.")
    PythonUI.PrintTerm("After a couple of days of easy travel you come to a dense part of the forest that doesn't feel right.")
    PythonUI.PrintTerm("All of the sudden three bandits walked out of nowhere demanding that you surrender one third of your carvan.")
    PythonUI.PressToContinue()
    PythonUI.ClearTerm()
    
    # checks users anwer to obeys or defy orders
    combatResult = bool
    action = PythonUI.SelectFromList("What do you do?",["Defy their orders","Obey their orders"])
    if action == "Obey their orders":
        PythonUI.PrintTerm("You obeyed their orders and gave one third of your caravan to the bandits.")
        PythonUI.PressToContinue()
        PythonUI.ClearTerm()
        return True
    elif action == "Defy their orders":
        # === Start Combat ===
        combatResult = PythonUI.SelectFromList("Win/Lose", [True, False])

    if not combatResult:
        return False
    
    PythonUI.ClearTerm()
    PythonUI.PrintTerm("You defended the caravan as hard you could!")
    PythonUI.PrintTerm("You successfully defeated the bandits, and you looted their bodies for resources.")
    PythonUI.PrintTerm("After the battle, Mr.Vanguard acknowledges your bravery and thanks you for your hard work by handing you a heath potion.")
    PythonUI.PrintBold("+1 healing potion, +3 swords, +1 bow, +30 coins")
    PythonUI.PressToContinue()
    PythonUI.ClearTerm()
    return True

def CaravanGuard():

    PythonUI.ClearTerm()
    PythonUI.PrintTerm("You accept the quest to guard Mr.Vanguard's caravan.\nOnce you arrive the caravan sets out for the city of Le'mans.")
    PythonUI.PressToContinue()
    PythonUI.ClearTerm()

    PythonUI.PrintTerm("After a days travel you reach a fork in the trail...")
    PythonUI.PrintTerm("You know these two paths, the left side is less traversed but the right path is known to have bandits.")
    PythonUI.PressToContinue()
    PythonUI.ClearTerm()
    # checks users anwser
    path = PythonUI.SelectFromList("What path do you take?", ["Left","Right"])
    
    results = bool
    
    # playes the Quest
    if path == "Left":
        results = LeftPath()
    elif path == "Right":
        results = RightPath()
    
    # check if player wins or not
    if results == False:
        PythonUI.ClearTerm()
        PythonUI.PrintTerm("Death Screen")
        return 
    
    PythonUI.ClearTerm()
    PythonUI.PrintTerm("Eventually the path came together and that path leaded up to Le'mans\n +300 Coins, +20 Food, +30 Representation, +10 Iron ")

# endregion Caravan Guard
