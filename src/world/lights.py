from util.my_math import *

class Light:

    def __init__(self, origin:Vector, color):
        self.origin = origin
        self.color = color

    def __str__(self):
        return (f"Light:\n\tx:{self.origin.vec[0]}\n\ty:{self.origin.vec[1]}\n\tz:{self.origin.vec[2]}\n")
