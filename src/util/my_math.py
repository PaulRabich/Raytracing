import math
import numpy as np
from numpy import linalg as la

class Line:
    def __init__(self, origin:np.array, direction:np.array):
        self.origin:np.array = origin
        self.direction:np.array = direction

    #double
    def insert(self, x:float):
        return self.origin + (self.direction * x)

    def __str__(self):
        return(f"Line:\n\tx:{self.origin.vec[0]}\t   x:{self.direction.vec[0]}\n\ty:{self.origin.vec[1]}\ts* y:{self.direction.vec[1]}\n\tz:{self.origin.vec[2]}\t   z:{self.direction.vec[2]}\n")

class Triangle:
    #a, b, c as Points
    def __init__(self, a:np.array, b:np.array, c:np.array):
        self.a = a
        self.b = b - a
        self.c = c - a
        self.cross = np.cross(self.b, self.c)

    def pointOfIntersection(self, line:Line):
        A = np.array([self.b, self.c, -1* line.direction])
        if(la.det(A) == 0):
            return np.array([-np.inf, -np.inf, -np.inf])
        B = (-1* self.a + line.origin)
        solution = la.solve(A, B)
        #print(solution)
        if(solution[0] == np.inf or solution[1] == np.inf or solution[2] == np.inf):
            return np.array([-np.inf, -np.inf, -np.inf])
        elif(solution[0] < 0 or solution[1] < 0 or solution[0] > 1 or solution[1] > 1 or solution[0] + solution[1] > 1):
            return np.array([-np.inf, -np.inf, -np.inf])
        else:
            return line.insert(solution[2])
        

