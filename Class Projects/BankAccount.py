from datetime import date

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

class Transaction:

    Ammount: float
    Date: date
    Vendor: str

    def __init__(self, ammount: float, date: date, vendor: str):
        self.Ammount = ammount
        self.Date = date
        self.Vendor = vendor

    @property
    def FormattedTransaction(self):
        formattedAmmount = "{:.2f}".format(self.Ammount)
        return f"${formattedAmmount.ljust(10)} {str(self.Date)} : {self.Vendor}"

class BankAccount:

    Owner: str = ""
    CoOwners: list[str] = []

    Balance: float = 0.0
    Deposits: list[Transaction] = []
    Withdrawals: list[Transaction] = []

    IntrestRate: float = 0.0

    def __init__(self, owner: str, coOwners: list[str] = [], firstDeposit: float = 0.0, intrestRate: float = 3.0):
        self.Owner = owner
        self.CoOwners = coOwners
        self.Balance = firstDeposit
        if firstDeposit != 0.0:
            trans = Transaction(ammount=firstDeposit,date=date.today(),vendor="Owner")
            self.Deposits.append(trans)
        self.IntrestRate = intrestRate

    def Deposit(self, thisDeposit: Transaction):
        self.Balance += thisDeposit.Ammount
        self.Deposits.append(thisDeposit)

    def Withdrawal(self, thisWithdrawal: Transaction):
        self.Balance -= thisWithdrawal.Ammount
        self.Withdrawals.append(thisWithdrawal)

    def AddCoOwner(self, coOwner: str):     
        self.CoOwners.append(coOwner)

    def RemoveCoOwner(self, coOwner: str):
        self.CoOwners.remove(coOwner)
 
    @property
    def FormattedBalance(self):
        return "${:.2f}".format(self.Balance)

# Start of Program
myAcc = BankAccount(owner="Jacob", firstDeposit=500.0)
 
myAcc.Deposit    (Transaction(50.0,  date.today(), "Owner"))
myAcc.Withdrawal (Transaction(121.0, date.today(), "Broliums"))
myAcc.Deposit    (Transaction(140.0, date.today(), "Owner"))
myAcc.Withdrawal (Transaction(20.0,  date.today(), "Ace Hardware"))
myAcc.Deposit    (Transaction(20.0,  date.today(), "Owner"))
myAcc.Deposit    (Transaction(130.0, date.today(), "Owner"))
 
print("Deposits:")
for transaction in myAcc.Deposits:
    print(transaction.FormattedTransaction)

print("Withdrawals:")
for transaction in myAcc.Withdrawals:
    print(transaction.FormattedTransaction)
