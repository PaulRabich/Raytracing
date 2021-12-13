from multiprocessing import Process
from util.my_math import *
from world.lights import Light
from models.shape import *


class Model:

    def __init__(self, distance:float, shapes:Shape, lights:Light,  x:int = 500, y:int = 300, numberOfThreads = 4):
        self.x = x
        self.y = y
        self.lights = lights
        self.distance = distance
        self.shapes = shapes
        self.pixels = np.full([x, y, 3], 255)
        self.numberOfThreads = numberOfThreads

    def calculatePoints(self, name):
        print(name)
        process = []
        for i in range(self.numberOfThreads):
            x = Process(target = self.calculatePointsThread, args=(i,))
            process.append(x)
            #print(i)
            x.start()

        for t in process:
            t.join()

    
    def calculatePointsThread(self, t):
        
        o = np.array([0, 0, 0])
        p = int(self.x/self.numberOfThreads)
        res = np.full([p, self.y, 3], 255)
        for s in self.shapes:
            for a in range(p):
                for b in range(self.y):
                    v:np.array = np.array([self.distance, (-self.x/2 + (t*p)) + a, -self.y/2 + b], dtype='float64') 
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
                    self.pixels[(t*p) + a][b] =  s.getColor(c)

        
    
    def getPixels(self):
        return self.pixels