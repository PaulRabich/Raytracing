import math
import numpy as np
from util.my_math import Line, Triangle
from world.lights import Light
from numpy import linalg as la

from world.models import generateTriangles

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
        return np.array([int(self.color[0] * c[0]), int(self.color[1] * c[1]), int(self.color[2] * c[2])])

    #Vector
    def isInSphere(self, vec:np.array):
        a = self.origin.add(vec.invert())
        return True if(a.length() <= self.radius) else False

class TriangleObject(Shape):

    def __init__(self, name,  color):
        self.color = color
        
        #self.triagles = triagles

    def pointOfIntersection(self, line:Line):
        res0 = np.array([-np.inf, -np.inf, -np.inf])
        res1 = np.array([-np.inf, -np.inf, -np.inf])
        for t in self.triagles:
            i = t.pointOfIntersection(line)
            if(i[0] == -np.inf):
                continue
            else:
                if(res0 [0] == -np.inf):
                    res0 = i
                else:
                    res1 = i
        return np.array([res0, res1]) if(res0[0] == -np.inf) else np.array([-np.inf, -np.inf, -np.inf])

    def move(self, vec):
        for t in self.triagles:
            t.move(vec)

    def scale(self, x):
        for t in self.triagles:
            t.scale(x)

    def getColorFactor(self, vec:np.array, light:Light):

        return 1

    def getColor(self, c:float):
        #print(c, self.color)
        return np.array([0, 0, 0])#

    def generateTriangles(filename):
        f = open("src\models\\" + filename, 'r')
        points = []
        triangles = []
        for line in f:
            if(line[0] == "#"):
                continue
            elif(line[0] == "v"):
                line = line[2:]
                print(line)
                n = line.split(" ")
                points.append(np.array([n[0], n[1], n[2]], dtype="float64"))
            elif(line[0] == "f"):
                line = line[2:]
                print(line)
                n = line.split(" ")
                triangles.append(Triangle(points[int(n[0]) - 1], points[int(n[1]) - 1], points[int(n[2]) - 1]))

        f.close()
        return triangles