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

    Owner: str
    CoOwners: list[str]

    Balance: float
    Deposits: list[float]
    Withdrawals: list[float]

    IntrestRate: float

    def __init__(self, owner: str, coOwners: list[str] = [""], firstDeposit: float = 0.0, intrestRate: float = 3.0):
        self.Owner = owner
        self.CoOwners = coOwners
        self.Balance = firstDeposit
        if firstDeposit != 0.0:
            self.Deposits.append(firstDeposit)
        self.IntrestRate = intrestRate

    def Deposit(self,Diposit1):
        self.Balance += Diposit1
        if Diposit1 != 0.0:
            self.Deposits.append(Diposit1)
        
        
        

    def Withdrawal(self,Withdrawal1):
        self.Balance -= Withdrawal1
        if Withdrawal1 != 0.0:
            self.Withdrawals.append(Withdrawal1)

    def __add__(self,addCoOwner):
        
        pass

    def removeCoOwner(self,remCoOwner):
        
        pass
        
        
        

        
        

    # Function: Deposit
    #   - Change the account balance accordingly
    #   - Record the deposit in 'Deposits'
    #
    # Function: Withdrawal
    #   - Change the account balance accordingly
    #   - Record the withdrawal in 'Withdrawals'
    #
    # Function: Add CoOwner
    #   - Add the co-owner to 'CoOwners'
    #
    # Function: Remove CoOwner
    #   - Remove the co-owner from 'CoOwners'

myAccount = BankAccount(owner="Jacob",)

myAccount.Deposit(2500.0)
myAccount.Withdrawal(1500.0)
myAccount.Deposit(20.0)
myAccount.Withdrawal(15.0)
myAccount.AddCoOwner(["Taylor"])
myAccount.remove

print(f"Deposits:\n{myAccount.Deposits}\n\nWithdrawals:\n{myAccount.Withdrawals}\n\nBalance:\n{myAccount.Balance}")