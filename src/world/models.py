import numpy as np

from util.my_math import Triangle
class Cube:

    def __init__(self):
        self.triangles = None

    def getTriangles(self):
        if(self.triangles == None):
            self.triangles = generateTriangles("Cube.obj")
        
        return self.triangles


def generateTriangles( filename):
        f = open("src\models\\" + filename, 'r')
        points = []
        triangles = []
        for line in f:
            if(line[0] == "#"):
                continue
            elif(line[0] == "v"):
                line = line[2:]
                print(line)
                n = line.split(" ")
                points.append(np.array([n[0], n[1], n[2]], dtype="float64"))
            elif(line[0] == "f"):
                line = line[2:]
                print(line)
                n = line.split(" ")
                triangles.append(Triangle(points[int(n[0]) - 1], points[int(n[1]) - 1], points[int(n[2]) - 1]))

        f.close()
        return triangles

