import asyncio
import plane
from plane import CalculatePlane

class opening():

    def startAsync(self):
        if __name__ == "__main__":
            asyncio.run(CalculatePlane().calculatePlane())
    def startServices(self):

        x = (input
             (""""What do u want?
             1. Calculate plane params
             """))
        try:
            valuex = int(x)
        except:
            print("invalid input")
            return opening().startServices()

        if 0<valuex<3:
            match valuex:
                case 1:
                    self.startAsync()
                case 2:
                    ...

opening().startServices()




