import asyncio

global airDensity
airDensity = 1.225
global stallSpeed
global coefficient

class CalculatePlane():

    def inputData(self):
        x = input("Plane have sweep? [Y/N]")
        if x == "Y" or x == "y":
            self.sweepAngle = 0
        elif x == "N" or x == "n":
            self.sweepAngle = input("Angle on LE Sweep? (decimal)")
        else:
            print("Invalid input")
            return
        self.wingsArea = input("Wings Area [m²]")
        self.weight = input("Weight [kg]")
        self.wingsLength = input("Wings Length [m]")
        self.tipLength = input("Tip Length [m]")
        self.rootChord = input("Root Chord [m]")

    async def calculatePlane(self):
        wingRatio = self.weight/self.wingsArea
        taperRatio = self.tipLength/self.rootChord


