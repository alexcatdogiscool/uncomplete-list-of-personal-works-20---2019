import numpy as np
import math
import objects
import funcs
import cv2


balls = []
for i in range(1):
    i = objects.sphere()
    i.pos[0] = 1.5
    #i.pos[0] = 1
    #i.pos[2] = 0
    i.rad = 0.7
    i.pos[1] = 0.5
    balls.append(i)

width = 1000
height = 1000
fov = 90
rays = []
midx = (width-1)/2
midy = (height-1)/2
incx = fov/width
incy = fov/height
for y in range(height):
    for x in range(width):
        az = funcs.deg2rad((x*incx) - (midx*incx))
        el = funcs.deg2rad((y*incy) - (midy*incy)) + (math.pi/2)
        i = objects.ray()
        i.direction = (np.array([math.sin(el)*math.cos(az), math.sin(az)*math.sin(el), math.cos(el)]))
        i.imgx = x
        i.imgy = y
        rays.append(i)
        #print(i.direction, el)


for frame in range(10):



    for r in rays:
        dst = 10000
        for b in balls:
            d = funcs.spheredst(r.pos,b.pos,b.rad)
            if d < dst:
                dst = d
        pd = 100#funcs.planedst(r.pos, 2.5)
        if pd < dst:
            dst = pd
        r.step(dst,0.001)


img = np.zeros((height,width,3))
for r in rays:
    img[r.imgy,r.imgx,0] = r.colour[0]
    img[r.imgy,r.imgx,1] = r.colour[1]
    img[r.imgy,r.imgx,2] = r.colour[2]

cv2.imwrite('img.png', img)