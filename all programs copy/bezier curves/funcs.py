import math
import numpy as np





def norm(a, b):
    return math.sqrt(a*a + b*b)


def colourLerp(start,end,t):
    r = (1-t)*start[0] + t*end[0]
    g = (1-t)*start[1] + t*end[1]
    b = (1-t)*start[2] + t*end[2]
    return (r,g,b)


def normalize(p, length):
    l = norm(p[0], p[1]) / length
    return np.array([p[0]/l, p[1]/l])