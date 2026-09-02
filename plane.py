import asyncio
import math
from cmath import sqrt
from math import cos
from math import sqrt

class CalculatePlane():

    async def stallsp(self, weight, wingsArea):
        stallSpeed = sqrt((2 * 9.81 * weight) / (1.225 * wingsArea * 1.2))
        return stallSpeed

    async def aspectr(self, wingsLength, wingsArea):
        aspectRatio = (wingsLength) ** 2 / wingsArea
        return aspectRatio

    async def wingr(self, weight, wingsArea):
        wingRatio = weight / wingsArea
        return wingRatio

    async def taperr(self, tipLength, rootChord):
        taperRatio = tipLength / rootChord
        return taperRatio

    async def lift(self, sweepAngle, wingsArea, stallSpeed):
        sweep_radian = math.radians(sweepAngle)
        lift = 0.5 * 1.225 * (stallSpeed * math.cos(sweep_radian))**2 * wingsArea * 0.4
        return lift

    async def mac(self, rootChord, taperRatio):
        MAC = 2 / 3 * rootChord * (1 + taperRatio + (taperRatio) ** 2) / (1 + taperRatio)
        return MAC

    async def calculatePlane(self):
        x = input("Plane have sweep? [Y/N]")
        if x == "Y" or x == "y":
            self.sweepAngle = input("Angle on LE Sweep? (decimal)")
        elif x == "N" or x == "n":
            self.sweepAngle = 0
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
            rootChord = float(self.rootChord)
            tipLength = float(self.tipLength)
            sweepAngle = float(self.sweepAngle)
        except:
            print("Invalid input, restarting operation...")
            return await self.calculatePlane()

        task1 = await asyncio.create_task(self.stallsp(weight, wingsArea))
        task2 = await asyncio.create_task(self.aspectr(wingsLength, wingsArea))
        task3 = await asyncio.create_task(self.wingr(weight, wingsArea))
        task4 = await asyncio.create_task(self.taperr(tipLength, rootChord))
        task5 = await asyncio.create_task(self.lift(sweepAngle, wingsArea, task1))
        task6 = await asyncio.create_task(self.mac(rootChord, task4))

        print(f"Stall Speed: {task1}")
        print(f"Aspect Ratio: {task2}")
        print(f"Wing Ratio: {task3}")
        print(f"Taper Ratio: {task4}")
        print(f"Lift: {task5}")
        print(f"MAC: {task6}")












