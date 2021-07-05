from view.picture import Picture
from world.lights import Light
from world.model import Model
from world.models import Cube
from world.shapes import *
from util.my_math import *
import numpy as np
from numpy import linalg as la

x = 1000
y = 800
s1 = Sphere(np.array([700, 0, 0]), 300, np.array([255, 0, 255]))
#c = TriangleObject(Cube().getTriangles(), np.array([255, 255, 255]))
#c.scale(200)
#c.move(np.array([800, 0, 0]))

shperes = [s1,]

l0 = Light(np.array([300, 350, 250]), np.array([255, 255, 255]), 1000)
l = [l0,]
m = Model(500, shperes, l, x, y)
r = m.calculatePoints()
print(len(r))

p = Picture(x, y)
for i in r:
    a, b , c = i
    p.drawPixel((a + (x/2)), y - (b + (y/2)), c)

p.showPicture()
p.save()

"""
c = TriangleObject(Cube().getTriangles(), np.array([255, 255, 255]))
c.scale(200)
c.move(np.array([800, 0, 0]))


print(c.pointOfIntersection(Line(np.array([0, 0, 0]),np.array([1, 0, 0]))))

"""