import asyncio
import plane
from plane import CalculatePlane
global x
x = 0
class opening():

    def startServices(self):

        x = (input
             (""""What do u want?
             1. Configure plane values
             2. Calculate plane params
             """))
        try:
            valuex = int(x)
        except:
            print("invalid input")
            return opening().startServices()

        if 0<valuex<3:
            match valuex:
                case 1:
                    CalculatePlane().inputData()
                case 2:
                    ...

opening().startServices()




