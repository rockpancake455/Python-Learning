from time import *

print("Start of Program")

print("While loop method...")
# For loop made with a while loop
index = 0   
while index in [0, 1, 2]:
    sleep(1)
    print(index)
    index = index + 1

print("For loop method...")
# For loop doing the same thing
for i in range(0,3):
    sleep(1)
    print(i)

print("End of Program")