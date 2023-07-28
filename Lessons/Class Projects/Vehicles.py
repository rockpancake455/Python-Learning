from time import sleep

# python folder1
#   - Class Projects
#       - Classes.py
#       - Vehicles.py
#   - Lessons
#   - Notes
#   - playground

def Limit(inputNumber: int, bottomLimit: int, topLimit: int):

    if inputNumber > topLimit:
        return topLimit
    elif inputNumber < bottomLimit:
        return bottomLimit
    
    return inputNumber

class Vehicle:

    # Properties
    Make = ""   # Ferrari
    Model = ""  # F40
    Year = ""   # 1980

    TopSpeed = 0
    Acceleration = 0
    BrakeForce = 0

    CurrentSpeed = 0

    def __init__(self, make: str, model: str, year: str):
        self.Make = make
        self.Model = model
        self.Year = year

    def ConfigureSpecs(self, topSpeed: int, acceleration: int, brakeForce: int):
        self.TopSpeed = topSpeed
        self.Acceleration = acceleration
        self.BrakeForce = brakeForce

    def Accelerate(self):
        self.CurrentSpeed += self.Acceleration
        self.CurrentSpeed = Limit(self.CurrentSpeed, 0, self.TopSpeed) 
        
        print(f"The {self.FullName} accelerates to {self.CurrentSpeed}!!")

    def Brake(self):
        self.CurrentSpeed -= self.BrakeForce
        self.CurrentSpeed = Limit(self.CurrentSpeed, 0, self.TopSpeed)

        print(f"The {self.FullName} brakes to {self.CurrentSpeed}!!")

    @property
    def FullName(self):
        return f"{self.Year} {self.Make} {self.Model}"
        
sleep(1)

myFerrari = Vehicle("Ferrari", "F40", "1980")
myFerrari.ConfigureSpecs(175, 15, 8)

myFord = Vehicle("Ford", "Focus", "2017")
myFord.ConfigureSpecs(120, 9, 8)

for i in range(0, 15):
    myFerrari.Accelerate()
    sleep(1)

for i in range(0,26):
    myFerrari.Brake()
    sleep(1)