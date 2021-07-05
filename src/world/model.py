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
        self.pixels = np.full([x, y, 3], 255)


    def calculatePoints(self):
        o = np.array([0, 0, 0])
        for s in self.shapes:
            for a in range(self.x):
                for b in range(self.y):
                    v:np.array = np.array([self.distance, -self.x/2 + a, -self.y/2 + b], dtype='float64') 
                    #print(a, b)
                    l:Line = Line(o, v) 
                    i = s.pointOfIntersection(l)
                    #print(i)
                    if(i.size == 3):
                        continue
                    i = i[0] if (la.norm(i[0]) < la.norm(i[1])) else i[1]
                    c = np.array([0, 0, 0])
                    for l in self.lights:
                        c0 = s.getColorFactor(i, l)
                        c = c + c0
                    self.pixels[a][b] =  s.getColor(c)
                    #self.pixels[a][b][0] = c[0]
                    #self.pixels[a][b][1] = c[1]
                    #self.pixels[a][b][2] = c[2]
    
    def getPixels(self):
        return self.pixels