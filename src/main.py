from view.picture import Picture
from world.lights import Light
from world.model import Model
from world.models import Cube
from world.shapes import *
from util.my_math import *
import numpy as np
from numpy import linalg as la, zeros

x = 1000
y = 800
s1 = Sphere(np.array([700, 0, 0]), 300, np.array([255, 0, 255]))

shperes = [s1,]

l0 = Light(np.array([300, -350, 250]), np.array([255, 255, 255]), 1000)
l = [l0,]

m = Model(500, shperes, l, x, y)
m.calculatePoints()
r = m.getPixels()

p = Picture(x, y)
for i in range(x):
    for j in range(y):
        p.drawPixel(i, j, (r[i][j][0], r[i][j][1], r[i][j][2]))

p.showPicture()
p.save()

"""
a = np.full([10, 10], np.array([255, 255, 255]), dtype="object")
for i in range(10):
    for j in range(10):
        a[i][j] = np.array([255, 255, 255])
print(a)
"""
