import asyncio


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

        if 0 < valuex < 4:
            match valuex:
                case 1:
                    ...
                case 2:
                    ...
                case 3:
                    ...

        else:
            print("Invalid input")


class childClass(opening):
    def __init__(self, name, age, favCode):
        super().__init__(name, age)
        self.favCode = favCode


name = input("Enter your name: ")
favcode = input("Enter your favorite code: ")


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
    favcodestr = str(favcode)
    child = childClass(namestr, ageVal, favcodestr)
    print(child.name, child.age, child.favCode)


convert()
Person = childClass(namestr, ageVal, favcodestr)
print(f"Okay, {Person.name}, you are {Person.age} right? Lets get to the interesting part")
Person.startServices()


async def main():
    ...


asyncio.run(main())


