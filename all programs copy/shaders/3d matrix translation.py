import math
import numpy as np

point = np.array([0,0,1])


def step(point, xstep, ystep):
    trans = np.array([[1,0,0],[0,1,0],[0,0,1]])
    trans[2,0] = xstep
    trans[2,1] = ystep

    return np.dot(point, trans)

npoint = step(point, 5,3)

print(npoint)
