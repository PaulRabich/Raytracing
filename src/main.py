from view.picture import Picture
from world.lights import Light
from world.model import Model
from world.shapes import *
from util.my_math import *
"""
x = 1000
y = 800
s = Sphere(Vector(800, 0, 0), 300, (255, 255, 255))

shperes = [s,]

l0 = Light(Vector(300, 350, 250), (255, 0, 255))
#l1 = Light(Vector(400, -300, -200), (255, 255, 255))
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
v = Vector(1, 23, 4)
v1 = Vector(2, 4, 1)
print(v.vec + v1.vec)
print(v)
print(v1)
#p.pointOfInersection(l).print()

