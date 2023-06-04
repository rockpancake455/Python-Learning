# Project: Bank account class
# 
# Needed properties:
#   - Balance
#   - Owner
#   - Co-Owner(s)
#   - Deposits
#   - Withdrawals
#   - Intrest Rate
#
# Functions:
#   - Deposit money
#   - Withdrawal money
#   - Add/remove co-owner
#   - Earn Intrest

class BankAccount:

    Owner: str = ""
    CoOwners: list[str] = []

    Balance: float = 0.0
    Deposits: list[float] = []
    Withdrawals: list[float] = []

    IntrestRate: float = 0.0

    def __init__(self, owner: str, coOwners: list[str] = [], firstDeposit: float = 0.0, intrestRate: float = 3.0):
        self.Owner = owner
        self.CoOwners = coOwners
        self.Balance = firstDeposit
        if firstDeposit != 0.0:
            self.Deposits.append(firstDeposit)
        self.IntrestRate = intrestRate

    def Deposit(self, thisDeposit: float):
        self.Balance += thisDeposit
        self.Deposits.append(thisDeposit)

    def Withdrawal(self, thisWithdrawal: float):
        self.Balance -= thisWithdrawal
        self.Withdrawals.append(thisWithdrawal)

    def AddCoOwner(self, coOwner: str):     
        self.CoOwners.append(coOwner)

    def RemoveCoOwner(self, coOwner: str):
        self.CoOwners.remove(coOwner)