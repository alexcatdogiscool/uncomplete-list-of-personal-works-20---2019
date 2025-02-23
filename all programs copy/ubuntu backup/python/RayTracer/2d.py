import numpy as np
import math
import pygame as pg



width = 20
fov = 90
rays = []
mid = (width-1)/2
inc = fov/width
for y in range(1):
    for x in range(width):
        a = ((x*inc) - (mid*inc)) * (math.pi/180)
        m = math.tan(a)
        rays.append(m)


def circle(m, x,y,r):
    d = r**2 + m**2*r**2 + 2*m*y*x-m**2*x**2-y**2
    if d > 0:
        return True
    return False

img = np.zeros(width)
f = 0
for r in rays:
    img[f] = circle(rays[f], 2,0,1)



    f += 1

print(img)