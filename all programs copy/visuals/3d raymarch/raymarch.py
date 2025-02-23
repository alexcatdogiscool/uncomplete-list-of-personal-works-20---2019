import ray
import math
import circle
import cv2
import numpy as np


def pythag(sx,sy,sz, ex,ey,ez):
    return ((ex-sx)**2 + (ey-sy)**2 + (ez-sz)**2)**0.5


csize = 2
cs = []
for i in range(csize):
    num = i
    i = circle.circle()
    
    if num == 0:
        i.y = 15
        i.rad = 5
        i.x = 7
        i.reflective = True
        i.id = num
    
    if num == 1:
        i.y = 15
        i.rad = 5
        i.x = -7
        i.id = num
        #i.reflective = True
    
    cs.append(i)


res = 300
raysize = res**2
fov = math.pi/2
stepsize = fov/(res-1)

rays = []

el = fov/2
for y in range(res):
    az = -fov/2
    for x in range(res):
        x = ray.ray()
        x.az = az
        x.el = el
        rays.append(x)
        az += stepsize
    el -= stepsize


################################# PROGRAM ####################################
iters = 20
lazydst = 20
resdst = 1

img = []

for r in rays:
    for i in range(iters):
        dst = 100
        for c in cs:
            dx = abs(r.x-c.x)-c.rad
            dy = abs(r.y-c.y)-c.rad
            dz = abs(r.z-c.z)-c.rad
            
            if dx > lazydst or dy > lazydst or dz > lazydst:
                dst = lazydst
            else:
                temp = pythag(r.x,r.y,r.z, c.x,c.y,c.z) - c.rad
                if temp < dst:
                    dst = temp
                    cid = c.id
                
        
        if dst < resdst:
            if cs[cid].reflective == True:
                r.reflect(cs[cid].x,cs[cid].y,cs[cid].z,cs[cid].rad)
                r.step(resdst+1)
                r.r /= 1.3
                r.g /= 1.3
                r.b /= 1.3
            if cs[cid].reflective == False:
                r.r *= 1#cs[cid].r
                r.g /= 20#cs[cid].g
                r.b /= 20#cs[cid].b
                r.hit = True


        r.step(dst)

        

        
        ##### FLOOR #####
        if r.z < -10:
            r.r /= 20
            r.g /= 20
            r.b *= 1
            r.hit = True
        



    img.append(r.b)
    img.append(r.r)
    img.append(r.g)

img = np.array(img)
img = img.reshape(res,res,3)

cv2.imwrite('image.png', img)