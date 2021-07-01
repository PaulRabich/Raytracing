import math
import numpy as np

class Vector:
    #double, double, double
    def __init__(self, x:float, y:float, z:float): 
        self.x:float = x
        self.y:float = y
        self.z:float = z

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    #Vector
    def add(self, vec):
       return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    #double
    def multiply(self, a:float):
        return Vector(self.x * a, self.y * a, self.z * a)

    def __str__(self):
        return(f"Vector:\n\tx:{self.x}\n\ty:{self.y}\n\tz:{self.z}\n")

    def invert(self):
        return Vector(-self.x, -self.y, -self.z)

    def scalar(self, vec):
        return (self.x * vec.x + self.y * vec.y + self.z * vec.z)

    def angle(self, vec):
        a = self.scalar(vec) / (self.length() * vec.length())
        if(a < -1):
            a = math.pi
        elif(a > 1):
            a = 0
        else:
            a = math.acos(a)
        
        alpha = (180/math.pi) * a
        #print(alpha)
        return alpha

    def norm(self):
        return self.x + self.y + self.z

class Line:
    def __init__(self, origin:Vector, direction:Vector):
        self.origin:Vector = origin
        self.direction:Vector = direction

    #double
    def insert(self, x:float):
        return self.origin.add(self.direction.multiply(x))

    def __str__(self):
        return(f"Line:\n\tx:{self.origin.x}\t   x:{self.direction.x}\n\ty:{self.origin.y}\ts* y:{self.direction.y}\n\tz:{self.origin.z}\t   z:{self.direction.z}\n")

class NormalPlain:
    def __init__(self, origin: Vector, normal:Vector):
        self.normal = normal
        self.origin = origin

    def __str__(self):
        return(f"Plain:\n\t(x   {self.origin.x})\t   ({self.normal.x})\n\t(y - {self.origin.y})\t * ({self.normal.y})\n\t(z   {self.origin.z})\t   ({self.normal.z})\n")

    def pointOfInersection(self, line:Line):
        a = self.normal.x * (self.origin.x - line.origin.x) + self.normal.y * (self.origin.y - line.origin.y) + self.normal.z * (self.origin.z - line.origin.z)
        b = line.direction.x * self.normal.x + line.direction.y * self.normal.y + line.direction.z * self.normal.z
        if(b==0):
            return None 
        s:float = (a)/(b)
        return line.insert(s)
