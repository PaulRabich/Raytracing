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
        o = np.array([0, 0, 0])
        for s in self.shapes:
            for a in range(-int(self.x/2), int(self.x/2), 1):
                for b in range(-int(self.y/2), int(self.y/2), 1):
                    v:np.array = np.array([self.distance, a, b], dtype='float64') 
                    l:Line = Line(o, v) 
                    i = s.pointOfIntersection(l)
                    #print(i)
                    if(i.size == 3):
                        continue
                    i = i[0] if (la.norm(i[0]) < la.norm(i[1])) else i[1]
                    #print(v)
                    c = np.array([0, 0, 0])
                    for l in self.lights:
                        c0 = s.getColorFactor(i, l)
                        c = c + c0
                    #c = c.multiply(1/len(self.lights))
                    #print(s.getColor(c))
                    res.append((a, b, s.getColor(c)))
        return res
    