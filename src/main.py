from view.picture import Picture
from world.lights import Light
from world.rendering import Model
from util.my_math import *
from models.sphere import *
import numpy as np



if __name__ == "__main__":
    x = 1000
    y = 800
    s1 = Sphere(np.array([700, 0, 0]), 300, np.array([255, 0, 255]))

    shperes = [s1,]

    l0 = Light(np.array([300, -350, 250]), np.array([255, 255, 255]), 1000)
    lights = [l0,]

    m = Model(500, shperes, lights, x, y, 8)
    m.calculatePoints("main")
    r = m.getPixels()

    picture = Picture(x, y)
    for i in range(x):
        for j in range(y):
            picture.drawPixel(i, j, (r[i][j][0], r[i][j][1], r[i][j][2]))

    picture.showPicture()
    picture.save()
