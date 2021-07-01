from view.picture import Picture
from world.lights import Light
from world.model import Model
from world.shapes import *
from util.my_math import *
import numpy as np
from numpy import linalg as la
"""
x = 1000
y = 800
s = Sphere(np.array([800, 0, 0]), 300, np.array([255, 255, 255]))

shperes = [s,]

l0 = Light(np.array([300, 350, 250]), np.array([255, 255, 255]), 1000)
l = [l0,]
m = Model(400, shperes, l, x, y)
r = m.calculatePoints()
print(len(r))

p = Picture(x, y)
for i in r:
    a, b , c = i
    p.drawPixel((a + (x/2)), y - (b + (y/2)), c)

p.showPicture()
p.save()

"""
t = Triangle(np.array([0, 0, 0]), np.array([10, 0, 0]), np.array([0, 10, 0]))
l = Line(np.array([0, 0, 0]), np.array([1, 0, 0]))
print(t.pointOfIntersection(l))

#p.pointOfInersection(l).print()

