from util.my_math import *
from world.lights import Light
from world.shapes import *


class Model:

    def __init__(self, distance:float, shapes:Sphere, lights:Light,  x:int = 500, y:int = 300):
        self.x = x
        self.y = y
        self.lights = lights
        self.distance = distance
        self.shapes = shapes

    def calculatePoints(self):
        res = []
        o = Vector(0, 0, 0)
        for s in self.shapes:
            for a in range(-int(self.x/2), int(self.x/2), 1):
                for b in range(-int(self.y/2), int(self.y/2), 1):
                    v:Vector = Vector(self.distance, a, b) 
                    l:Line = Line(o, v) 
                    i = s.pointOfIntersection(l)
                    if(i == None):
                        continue
                    i = i[0] if (i[0].length() < i[1].length()) else i[1]
                    #print(v)
                    c = Vector(0, 0, 0)
                    for l in self.lights:
                        c0 = s.getColorFactor(i, l)
                        c = c.add(c0)
                    #c = c.multiply(1/len(self.lights))
                    res.append((a, b, s.getColor(c)))
        return res
    