import math
import numpy as np
import matplotlib.pyplot as plt

def calc(a,b):
    num = (complex(a,b))**2
    length = (num.real**2 + num.imag**2)**0.5
    return num.real, num.imag, length

size = 10,10
origen = 0,0
startx = origen[0] - size[0]/2
starty = origen[1] - size[1]/2


values = []

for y in range(size[1]):
    for x in range(size[0]):
        a,b,length = calc(startx+x, starty+y)
        values.append(a)
        values.append(b)
        values.append(length)

values = np.array(values)
values = values.reshape(size[0]*size[1], 3)

print(values)
