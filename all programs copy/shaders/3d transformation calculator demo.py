import math
import numpy as np

def radtodeg(x):
    return x * 180/math.pi

def degtorad(x):
    return x * math.pi/180

point = np.array([0,0,2,1])

step = 10

hangle = degtorad(0)
vangle = degtorad(0)



def move(point, hangle, vangle, stepsize):
    
    ystep = stepsize * (math.sin(vangle))

    val = stepsize * math.cos(vangle)

    xstep = val * math.sin(hangle)

    zstep = val * math.cos(hangle)

    trans = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[xstep, ystep, zstep, 1]])

    return np.dot(point, trans)


print(move(point, hangle, vangle, step))
