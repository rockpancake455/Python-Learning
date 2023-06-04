from random import randint

# My Loops

#for loop repeat at a certin amount of times 
#A while loop will repeat until a given statement is false

# region For Loops

# nameList = ["Taylor","Jacob","Mom","Dad","Riley","Bella"]

# #print(nameList[4])
# for name in nameList:
#     print(name)

# endregion
    
#regionwhileloop

#foo = 10
#while foo >= 10:
     #foo = randint(1, 20)
     #print(foo)
    
#print("End of Program :)")

#foo = ["ham","cheese","bread"]

#print (foo)
#for foo in foo:
    #print(foo)

#mylist = ["bread","bread","bread","bread","bread","cheese","ham"]
#print (mylist)

#while mylist.count("bread") > 1:
    #mylist.remove("bread")
    #print("I am removing an 'bread'from your plate")
    
#print(mylist)

# region buying drinks

print ("hello wellcome to the thirsty ghost inn where we serve drinks and food of all kinds." )
#the verities that the list has
liste= ["cocacola","pepsi","parkin","coffie","sushi","water"]
username = input()


if username == "cocacola":#if the item is in the list
    print("that is going to be $1.25")
elif username == "pepsi":#if the item is in the list
    print("that is going to be $1.50")
elif username == "parkin":#if the item is in the list
    print("that is going to be $3.50")
elif username == "water":#if the item is in the list
    print("that is going to be $1.00")
elif username == "sushi":#if the item is in the list
    print("that is going to be $3.59")
elif username == "coffie":#if the item is in the list
    print("that is going to be $2.59")
else:
     print("sorry we don't have that")   

usernameprice = input()

if usernameprice == "1.25":#the price of the item
    print("have a nice day")#a comment
elif usernameprice == "1.50":#the price of the item
    print("thanks for buying at the thirsty ghost inn")#a comment
elif usernameprice == "3.50":#the price of the item
    print("seya!")#a comment
elif usernameprice == "1.00":#the price of the item
    print("seems like you are thirsty have a nice day")#a comment
elif usernameprice == "3.59":#the price of the item
    print("munch munch")
elif usernameprice == "2.59":#the price of the item
    print("thanks for droping by")
else:
     print("you under esemated the price!") #a comment telling you that you less then what expected
      
print ("end of program")
# endregion