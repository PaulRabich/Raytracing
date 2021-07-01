import math
import numpy as np
"""
class Vector:
    #double, double, double
    def __init__(self, x:float, y:float, z:float): 
        self.vec = np.array([x, y, z], dtype=np.float64)

    def length(self):
        return math.sqrt(self.vec[0]**2 + self.vec[1]**2 + self.vec[2]**2)
    
    #Vector
    def add(self, vec):
       return self.vec + vec.vec

    #double
    def multiply(self, a:float):
        return Vector(self.vec[0] * a, self.vec[1] * a, self.vec[2] * a)

    def __str__(self):
        return(f"Vector:\n\tx:{self.vec[0]}\n\ty:{self.vec[1]}\n\tz:{self.vec[2]}\n")

    def invert(self):
        return Vector(-self.vec[0], -self.vec[1], -self.vec[2])

    def scalar(self, vec):
        return (self.vec[0] * vec.vec[0] + self.vec[1] * vec.vec[1] + self.vec[2] * vec.vec[2])

    def angle(self, vec):
        a = self.scalar(vec) / (self.length() * vec.length())
        if(a < -1):
            a = math.pi
        elif(a > 1):
            a = 0
        else:
            a = math.acos(a)
        
        alpha = (180/math.pi) * a
        return alpha

    def norm(self):
        return self.vec[0] + self.vec[1] + self.vec[2]
"""
class Line:
    def __init__(self, origin:np.array, direction:np.array):
        self.origin:np.array = origin
        self.direction:np.array = direction

    #double
    def insert(self, x:float):
        return self.origin + (self.direction * x)

    def __str__(self):
        return(f"Line:\n\tx:{self.origin.vec[0]}\t   x:{self.direction.vec[0]}\n\ty:{self.origin.vec[1]}\ts* y:{self.direction.vec[1]}\n\tz:{self.origin.vec[2]}\t   z:{self.direction.vec[2]}\n")

