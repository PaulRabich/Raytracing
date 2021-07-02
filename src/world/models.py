import pandas as pd

from util.my_math import Triangle
class Cube:

    def __init__(self):
        self.url = "src\models\cube_"
        self.triangles = None

    def getTriangles(self):
        if(self.triangles == None):
            self.generateTriangles()
        
        return self.triangles

    def generateTriangles(self):
        pass

