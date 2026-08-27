import asyncio
from InitPlane import CalculatePlane

class opening():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def startServices(self):
        x = (input
             (""""What do u want?
             1. Configure plane values
             2. Calculate plane params
             3. Configure drone values
             4. Calculate drone params 
             """))
        valuex = int(x)

        if 0 < valuex < 5:
            match valuex:
                case 1:
                    ...
                case 2:
                    ...
                case 3:
                    ...
                case 4:
                    ...

        else:
            print("Invalid input")

name = input("Enter your name: ")

def checkage():
    age = input("Enter your age: ")
    global ageVal
    if type(age) != int:
        try:
            ageint = int(age)
        except:
            print("Invalid input")
            return checkage()
    else:
        ...
    ageVal = ageint


def convert():
    checkage()
    global namestr, agestr, favcodestr
    namestr = str(name)

convert()
Person = opening(namestr, ageVal, favcodestr)
print(f"Okay, {Person.name}, you are {Person.age} right? Lets get to the interesting part")
Person.startServices()



