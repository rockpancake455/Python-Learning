import os, time

time.sleep(1)

class Driver:

    Name: str
    Make: str
    Model: str
    Year: str
    Color: str

file = open(f"{os.path.dirname(__file__)}\\DriverData.txt", 'r')
inputString = file.read()
file.close()

driverLines = str.split(inputString, "\n")
drivers: list[Driver] = []

for line in driverLines:
    driverData = str.split(line, ",")
    # [John Smith,Toyota,Supra,2019,Blue]
    thisDriver = Driver()
    thisDriver.Name = driverData[0]
    thisDriver.Make = driverData[1]
    thisDriver.Model = driverData[2]
    thisDriver.Year = driverData[3]
    thisDriver.Color = driverData[4]
    drivers.append(thisDriver)

for driver in drivers:
    print(f"{driver.Make} {driver.Model} {driver.Year}")


