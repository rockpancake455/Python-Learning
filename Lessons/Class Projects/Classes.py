# ===================================================
# 
#   Classes Project
#   
#   Created By: Jacob Herndon & Taylor Herndon
# 
# ===================================================

# Jacob Ronald Herndon
# 796 Nethercott Lane
# Victor, ID 83455

# Taylor Bryan Herndon
# 2055 NE Skyview Drive
# Pullman, WA 99163

class Address:

    Owner = ""
    StreetName = ""
    ZipCode = ""
    State = ""
    City = ""

    def __init__(self, owner: str, streetName: str, city: str, state: str, zipCode: str):
        self.Owner = owner
        self.StreetName = streetName
        self.City = city
        self.State = state
        self.ZipCode = zipCode

    def PrintAddress(self):
        print(self.Owner) 
        print(self.StreetName)
        print(f"{self.City}, {self.State} {self.ZipCode}")
        
jacobAddress = Address("Jacob Ronald Herndon", "796 Nethercott Lane", "Victor", "Idaho", "83455")
taylorAddress = Address("Taylor Bryan Herndon", "2055 NE Skyview Dr", "Pullman", "Washington", "99163")

jacobAddress.PrintAddress()
print("")
taylorAddress.PrintAddress()