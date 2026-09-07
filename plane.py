import asyncio
import dataclasses
import math
from cmath import sqrt
from math import cos
from math import sqrt
from dataclasses import dataclass

#Untuk Meng-Input Data dari GUI
@dataclass
class inputData:
    sweep_angle: float
    wings_area: float
    weight: float
    wings_length: float
    tip_length: float
    root_chord: float

#Untuk perhitungannya
class CalculatePlane():
    def __init__(self):
        asyncio.run(self.calculatePlane())

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

    async def calculatePlane(self, data: inputData):
        self.sweepAngle = data.sweep_angle
        self.wingsArea = data.wings_area
        self.weight = data.weight
        self.wingsLength = data.wings_length
        self.tipLength = data.tip_length
        self.rootChord = data.root_chord
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

        def __str__(self):
            return {
                "Stall Speed": f"{task1:.2f} m/s",
                "Aspect Ratio": f"{task2:.2f}",
                "Wing Loading": f"{task3:.2f} kg/m²",
                "Taper Ratio": f"{task4:.2f}",
                "Estimated Lift": f"{task5:.2f} N",
                "MAC": f"{task5:.2f} m"
            }











