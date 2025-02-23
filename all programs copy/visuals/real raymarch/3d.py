import math
import numpy as np
import cv2
import random

def norm(a,b,c):
    return (a*a + b*b + c*c)**0.5

def des(x,y,z, cx,cy,cz,cr):
    return norm(x-cx, y-cy, z-cz) - cr

def deb(x,y,z, bx,by,bz,br):
    br /= 2
    xm = max(abs(x-bx)-br,0)
    ym = max(abs(y-by)-br,0)
    zm = max(abs(z-bz)-br,0)
    return norm(xm,ym,zm)



class sphere:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.r = 3

class cube:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.r = 3

class light:
    def __init__(self):
        self.x = 300
        self.y = 120
        self.z = 0
        self.r = 10


class ray:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.az = 0
        self.el = 0

        self.r = 0
        self.g = 0
        self.b = 0

        self.closest = 0
        self.reflects = 0
        self.light = False
        self.hit = False
        self.ltest = False
        self.ldst = 100
    def step(self, dist):
        if self.hit != True:
            self.z += math.sin(self.el) * dist
            xyd = math.cos(self.el) * dist
            self.x += math.cos(self.az) * xyd
            self.y += math.sin(self.az) * xyd

    def cast(self, shapes, lights):
        # shapes key:   spheres(0), boxes(1), planes(2), cylinders(3)
        
        toll = 0.5
        dist = 100
        
        ##### sphere ####
        for s in shapes[0]:
            dist = min(dist, des(self.x,self.y,self.z, s.x,s.y,s.z,s.r))
        ### box ####
        for s in shapes[1]:
            dist = min(dist, deb(self.x,self.y,self.z, s.x,s.y,s.z,s.r))
        ### plane ###
        for s in shapes[2]:
            dist = min(dist, des(self.x,self.y,self.z, s.x,s.y,s.z,s.r))
        ### cylinder ###
        for s in shapes[3]:
            dist = min(dist, des(self.x,self.y,self.z, s.x,s.y,s.z,s.r))
        if dist < toll:
            if self.ltest == False:
                self.step(-toll)
            self.hit = True
            if self.ltest == False:
                for i in range(1):
                    i = ray()
                    i.ltest = True

                    i.az = 0
                    i.el = math.pi/2
                    
                    i.x = self.x
                    i.y = self.y
                    i.z = self.z
                    for e in range(30):
                        i.cast(shapes, lights)
                    if i.z > 200:
                        self.r = 255
                        self.g = 255
                        self.b = 255
                    else:
                        self.r = 50
                        self.g = 50
                        self.b = 50
        self.step(dist)

shapes = []
sphs = []
boxes = []
planes = []
cylinders = []
lights = []
for i in range(2):
    num = i
    i = sphere()
    i.x = 300
    i.z = -30
    i.r = 80
    if num == 1:
        i.x = 225
        i.r = 20
        i.y = 0
        i.z = 60
    sphs.append(i)
for i in range(1):
    i = cube()
    i.r = 500
    i.x = 300
    i.z = -450
    boxes.append(i)
for i in range(1):
    i = light()
    lights.append(i)

shapes.append(sphs)
shapes.append(boxes)
shapes.append(planes)
shapes.append(cylinders)


width = 500
res = width**2
fov = math.radians(70)
astep = fov/(width-1)
lookingaz = 0
lookingel = math.radians(-15)

rays = []
for e in range(width):
    
    for a in range(width):
        numa = a
        a = ray()
        a.az = ((-fov/2) + (astep * numa)) + lookingaz
        a.el = ((fov/2) - (astep * e)) + lookingel
        rays.append(a)

for r in rays:
    for i in range(50):
        r.cast(shapes, lights)


img = []
for r in rays:
    img.append(r.r)
    img.append(r.g)
    img.append(r.b)

img = np.array(img)
img = img.reshape(width,width,3)
cv2.imwrite('3d.png', img)