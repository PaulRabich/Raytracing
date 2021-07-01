from util.my_math import *

class Light:

    def __init__(self, origin:Vector, color):
        self.origin = origin
        self.color = color

    def __str__(self):
        return (f"Light:\n\tx:{self.origin.x}\n\ty:{self.origin.y}\n\tz:{self.origin.z}\n")
