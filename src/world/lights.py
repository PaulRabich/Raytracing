from util.my_math import *

class Light:


    #Lightintensity int between 0 - 1000
    def __init__(self, origin:np.array, color:np.array, intensity:int):
        self.origin = origin
        self.color = color
        self.intensity = intensity

    def __str__(self):
        return (f"Light:\n\tx:{self.origin.vec[0]}\n\ty:{self.origin.vec[1]}\n\tz:{self.origin.vec[2]}\n")
