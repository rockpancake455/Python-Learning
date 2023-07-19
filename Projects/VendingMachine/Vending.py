from random import randint
import time
print("Hello there this is the atomatic phone number generator\nyou will receve 5 numbers ")
rollagain="yes"

while rollagain.upper() in ["Y","YES"]:
    input("press[enter]to start")
    for ii in range(0,5):
        for i in range(0,3):
            time.sleep(1)
            print(".")
    
        number1=randint(100,999)
        number2=randint(100,999)

        print(f"(208){number1}-{number2}")

    rollagain = input("do you want a different set of phone numbers\n(yes or no) ")
print("end of program")