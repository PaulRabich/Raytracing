import math
from util.my_math import Line, Vector
from world.lights import Light

class Shape:
    def __init__(self, origin, color ):
        self.color = color
        self.origin = origin

    #def getColor(self, vec:Vector)

class Sphere(Shape) :

    #Vector, double
    def __init__(self, origin:Vector, r:float, color):
        super().__init__(origin, color)
        self.radius:float = r

    #Line
    def pointOfIntersection(self, line:Line):
        l = line
        line = Line(line.origin.add(self.origin.invert()), line.direction)
        a = line.direction.vec[0]**2 + line.direction.vec[1]**2 + line.direction.vec[2]**2
        b = 2 * (line.origin.vec[0] * line.direction.vec[0] + line.origin.vec[1] * line.direction.vec[1] + line.origin.vec[2] * line.direction.vec[2])
        c = line.origin.vec[0]**2 + line.origin.vec[1]**2 + line.origin.vec[2]**2 - self.radius**2
        #print(a, b, c)
        if (b**2 < 4 * a * c):
            return None
        t1:float = (-b + math.sqrt(b**2 - 4 * a * c))/ (2*a)
        t2:float = (-b - math.sqrt(b**2 - 4 * a * c))/ (2*a)
        #print(t1, t2)
        #exit()
        return (l.insert(t2), l.insert(t1))

    def getColorFactor(self, vec:Vector, light:Light):
        #print(light)
        c = 0
        v = vec.add(self.origin.invert())
        v1 = light.origin.add(vec.invert())
        angle = v1.angle(v)
        #print(angle)
        if (angle > 90):
            c = 0
        else:
            c = 255 - angle * 255/90
        c /= 255
        return Vector(light.color[0] * c /255,light.color[1] * c /255, light.color[2] * c /255)

    def getColor(self, c:float):
        return (int(self.color[0] * c.vec[0]), int(self.color[1] * c.vec[1]), int(self.color[2] * c.vec[2]))

    #Vector
    def isInSphere(self, vec:Vector):
        a = self.origin.add(vec.invert())
        return True if(a.length() <= self.radius) else False