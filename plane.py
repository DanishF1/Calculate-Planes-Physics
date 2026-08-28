import asyncio
import math
from cmath import sqrt
from math import cos
from math import sqrt

global airDensity
airDensity = 1.225
global stallSpeed
global coefficient

class CalculatePlane():
    def __init__(self):
        asyncio.run(self.calculatePlane())

    async def calculatePlane(self):
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
        try:
            wingsArea = float(self.wingsArea)
            weight = float(self.weight)
            wingsLength = float(self.wingsLength)
            tipLength = float(self.tipLength)
            rootChord = float(self.rootChord)
            tipLength = float(self.tipLength)
            sweepAngle = int(self.sweepAngle)
        except:
            print("Invalid input, restarting operation...")
            return self.calculatePlane()

        stallSpeed = sqrt((2 * 9.81 * weight)/(airDensity * wingsArea * 1.2))
        aspectRatio = (wingsLength)**2 / wingsArea
        wingRatio = weight/wingsArea
        taperRatio = tipLength/rootChord
        lift = 0.5 * (stallSpeed * cos(sweepAngle))**2 * wingsArea * coefficient
        MAC = 2/3 * rootChord * (1 + taperRatio + (taperRatio)**2)/(1 + taperRatio)




