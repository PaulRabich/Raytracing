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
        a = line.direction.x**2 + line.direction.y**2 + line.direction.z**2
        b = 2 * (line.origin.x * line.direction.x + line.origin.y * line.direction.y + line.origin.z * line.direction.z)
        c = line.origin.x**2 + line.origin.y**2 + line.origin.z**2 - self.radius**2
        if (b**2 - 4 * a * c < 0):
            return None
        t1:float = (-b + math.sqrt(b**2 - 4 * a * c))/ (2*a)
        t2:float = (-b - math.sqrt(b**2 - 4 * a * c))/ (2*a)
        #print(t1)
        #print(t2)
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
        return Vector(light.color[0] * c /255,light.color[1] * c /255, light.color[2] * c /255 )

    def getColor(self, c:float):
        return (int(self.color[0] * c.x), int(self.color[1] * c.y), int(self.color[2] * c.z))

    #Vector
    def isInSphere(self, vec:Vector):
        a = self.origin.add(vec.invert())
        return True if(a.length() <= self.radius) else False