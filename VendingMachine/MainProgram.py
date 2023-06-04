# ===============================================================
# 
#   Vending Machine
#   By: Jacob Herndon
#
#   Desc:
#
# ===============================================================

# Wanted Features
# - Variety of products.
# - A way to put in money & a wallet to take money from.
# - Check user input.
# - A way to order multiple times.
# - Calculate change & give money back to the user.

# region Program Constants and Variables

wallet = 10.00
products = ["Pepsi", "Coke", "Root Beer", "Mtn Dew", "V8", "Hot Pockets", "Chocolate", "Chips"]
prices = {"Pepsi": 1.25, "Coke": 1.25, "Root Beer": 1.50, "Mtn Dew": 1.75, "V8": 1.50, "Hot Pockets": 2.00, "Chocolate": 1.75, "Chips": 1.00}

# endregion

# region Program Functions

def CheckUserItem(userInput: str):
    isValid = False

    # Check if user response 0 to 7
    # Check if user response is a number
    if not userInput.isdigit(): # Check if customer response is not a digit.
        print("Error: Input is not a number.")
    elif not int(userInput) in range(0,8): # Check if customer reponse is in range 0 to 7.
        print("Error: Input is not in range 0 to 7.")
    else: 
        print(f"You have selected {products[int(userInput)]}")
        isValid = True

    return isValid

def CheckUserPrice(userPrice: str, productPrice: float):
    isValid = False

    if not userPrice.replace('.', '').isnumeric():
        print("Error: Input is not a decimal.")
    elif not float(userPrice) >= productPrice:
        print("Error: The input is less then the price.")
    elif not wallet >= float(userPrice):
        print("Error: Your wallet doesn't have that much money!")
    elif float(userPrice) > productPrice + 2.00:
        print("Error: You put in too much money!")
    else:
        change = float(userPrice) - productPrice
        print(f"You put in ${userPrice}, the cost was ${productPrice}, your change is ${change}.")    
        isValid = True
    
    return isValid

def CheckExit(userInput :str):
    isValid = False
    if userInput == "Y":
        isValid = True
    elif userInput == "N":
        isValid = True
    
    return isValid

# endregion

# region Main Loop

exitTransaction = False
while exitTransaction == False:

    print("Hello, welcome to THE THRISTY GHOST!\nWhat product do you want?")
    for product in products:
        formattedPrice = "{:.2f}".format(prices[product])
        print(f"[{products.index(product)}] {product.ljust(15)}  ${formattedPrice}")
    print(f"You currently have ${wallet}")

    itemInput = ""
    responseIsValid = False
    while responseIsValid == False:
        itemInput = input()#Example Input: 0, 2, 5, 7
        responseIsValid = CheckUserItem(itemInput)

    print("\nPlease insert money.")
    responseIsValid = False
    productName = products[int(itemInput)]   # Get product name from index
    productPrice = prices[str(productName)]     # Get product price from product name

    while responseIsValid == False:
        priceInput = input()
        responseIsValid = CheckUserPrice(priceInput, productPrice)

    print(f"\nVending {productName}...")
    print ("Do you want to keep on buying more stuff?\n[Y] = Yes  [N] = No")
    
    responseIsValid = False
    while responseIsValid == False:
        exitInput = input().upper()
        responseIsValid = CheckExit(exitInput)
    
    if exitInput == "Y":
        exitTransaction = False
    elif exitInput == "N":
        exitTransaction = True

# endregion

print("thinks for visiting THE THRISTY GHOST\n\n End Of Program")

# the custumer puts in the products price
# the custumer has a wallet like $10.00 or $5.00
#subtract the products price to  the wallet
#give the item to the custumer
#and repeat