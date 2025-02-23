import math
import numpy as np
import random

def norm(a,b):
    return (a*a + b*b)**0.5

def sigmoid(x):
    return (2/(1 + np.exp(-x)))-1

def angleto(x1,y1,x2,y2):
    return math.atan2(y1-y2, x1-x2)

def growth(x):
    return (-1.5*(x-0.5)**2+0.5)/500