from random import randint

drinks = ["Cola","Pepsi","Fanta","Water","DR.Peper"]
drinkscost = {"Cola":1.00,"Pepsi":1.25,"Fanta":2.00,"Water":0.50,"DR.Peper":2.00}

print("Hello, welcome to the vending machine \n")
for drink in drinks:
    formatedprices = "{:.2f}".format(drinkscost[drink])
    print(f"[{drinks.index(drink)}] {drink.ljust(15)} ${formatedprices}")
print("")
userinput = int(input(f"what type of dring do you want to buy"))

product = drinks[userinput]


print(f"you bought a {product}")


