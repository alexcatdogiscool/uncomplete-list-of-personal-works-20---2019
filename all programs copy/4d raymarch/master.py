import math
import ray
import shape
import cv2
import numpy as np

def pythag(sx,sy,sz, ex,ey,ez):
    return ((sx-ex)**2 + (sy-ey)**2 + (sz-ez)**2)**0.5


rays = []
raysize = 200**2
pov = 70
povstep = pov/(raysize**0.5)
posx = 0
posy = 1
for i in range(raysize):
    num = i
    i = ray.ray()
    i.el = (pov/2)
    #i.az = -(pov/2)
    i.az = (posx * povstep) - (pov/2)
    if posx == 35:
        i.el = (posy*povstep)
        posy += 1
        posx = -1
    posx += 1
    print(i.az, i.el)
    rays.append(i)

sphs = []
for i in range(1):
    i = shape.sphere()
    i.x = 10
    i.y = 0
    i.z = 0

    i.rad = 2

    i.r = 255
    i.g = 0
    i.b = 255
    sphs.append(i)


running = True
for epoch in range(5):


    for r in rays:
        dist = 1000
        for s in sphs:
            temp = pythag(r.x,r.y,r.z, s.x,s.y,s.z)
            if temp < dist:
                dist = temp
        r.step(dist, 0,0)

img = np.zeros((raysize, 3))
count = 0
for r in rays:
    colour = np.array([r.r, r.g, r.b])
    img[count,:] = colour

    count += 1

img = img.reshape(int(raysize**0.5), int(raysize**0.5), 3)


cv2.imwrite('test.png', img)