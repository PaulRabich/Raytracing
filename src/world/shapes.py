import math
import numpy as np
from util.my_math import Line
from world.lights import Light
from numpy import linalg as la

class Shape:
    def __init__(self, origin, color ):
        self.color = color
        self.origin = origin

    #def getColor(self, vec:Vector)

class Sphere(Shape) :

    #Vector, double
    def __init__(self, origin:np.array, r:float, color):
        super().__init__(origin, color)
        self.radius:float = r
        print(self.color)

    #Line
    def pointOfIntersection(self, line:Line):
        l = line
        line = Line(line.origin + (-1 * self.origin), line.direction)
        a = line.direction[0]**2 + line.direction[1]**2 + line.direction[2]**2
        b = 2 * (line.origin[0] * line.direction[0] + line.origin[1] * line.direction[1] + line.origin[2] * line.direction[2])
        c = line.origin[0]**2 + line.origin[1]**2 + line.origin[2]**2 - self.radius**2
        #print(a, b, c)
        if (b**2 < 4 * a * c):
            return np.array([-np.inf, -np.inf, -np.inf])
        t1:float = (-b + math.sqrt(b**2 - 4 * a * c))/ (2*a)
        t2:float = (-b - math.sqrt(b**2 - 4 * a * c))/ (2*a)
        #print(t1, t2)
        #exit()
        return np.array([l.insert(t1), l.insert(t2)])

    def getColorFactor(self, vec:np.array, light:Light):
        #print(light)
        c = 0
        v = vec + -1* self.origin
        v1 = light.origin + -1* vec
        #print(v, v1)
        
        angle = np.degrees(np.arccos(np.dot(v, v1) / (la.norm(v) * la.norm(v1))))
        #print(angle)
        if (angle > 90):
            c = 0
        else:
            c = 255 - angle * 255/90
        c  = (c/255**2) * light.intensity/1000
        #print(c)
        return self.color * c

    def getColor(self, c:float):
        #print(c, self.color)
        return (int(self.color[0] * c[0]), int(self.color[1] * c[1]), int(self.color[2] * c[2]))

    #Vector
    def isInSphere(self, vec:np.array):
        a = self.origin.add(vec.invert())
        return True if(a.length() <= self.radius) else False