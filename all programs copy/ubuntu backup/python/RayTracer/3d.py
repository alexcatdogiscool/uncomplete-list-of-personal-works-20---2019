import numpy as np
import math
import pygame as pg
import random
import cv2
import time
random.seed(1)



width, height = 800,800
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
birdCol = (217, 211, 50)
wallCol = (41, 194, 46)
sky = (60, 207, 240)

screen = pg.display.set_mode((width,height))
screen.fill(sky)
pg.display.flip()



class ray:
    def __init__(self):
        self.az = 0
        self.el = 0
        self.colour = (0,0,0)
        self.imgx = 0
        self.imgy = 0

class sphere:
    def __init__(self):
        self.pos = np.array([random.uniform(-5,5),random.uniform(-5,5),random.uniform(-5,5)])
        self.rad = 1
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))



def check(az,el,x,y,z,r):
    b = x
    n = y
    m = z
    a = az
    l = el

    desc = (-2*a*n - 2*b-2*l*m)**2 - 4*(a**2 + l**2 + 1)*(b**2+m**2+n**2-r**2)
    if desc > 0:
        return True
    return False


width = 100
height = 100
fov = 90
rays = []
midx = (width-1)/2
midy = (height-1)/2
incx = fov/width
incy = fov/height
for y in range(height):
    for x in range(width):
        az = math.tan(((x*incx) - (midx*incx)) * (math.pi/180))
        el = math.tan(((y*incy) - (midy*incy)) * (math.pi/180))
        i = ray()
        i.az = az
        i.el = el
        i.imgx = x
        i.imgy = y
        rays.append(i)

sphs = []
for i in range(1):
    i = sphere()
    sphs.append(i)





past = 0
frame = 0
running = True
while running:
    keys=pg.key.get_pressed()
    ###############################################################
    img = np.zeros([width,height,3])
    for r in rays:
        for s in sphs:
            coll = check(r.az,r.el,s.pos[0],s.pos[1],s.pos[2],s.rad)
            if coll == True:
                img[r.imgx,r.imgy,0] = s.colour[0]
                img[r.imgx,r.imgy,1] = s.colour[1]
                img[r.imgx,r.imgy,2] = s.colour[2]
                break
        if keys[pg.K_DOWN]:
            r.el += 0.1
        if keys[pg.K_UP]:
            r.el -= 0.1
        if keys[pg.K_LEFT]:
            r.az -= 0.1
        if keys[pg.K_RIGHT]:
            r.az += 0.1
    ###############################################################
    img = cv2.resize(img, (800,800), interpolation=cv2.INTER_AREA)
    s = pg.surfarray.make_surface(img)
    screen.blit(s, (0,0))

    if frame == 10:
        frame = -1
        t = time.time()
        framerate = 10/(t-past)
        past = t
        print(framerate)



    frame += 1
    pg.display.flip()
    for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        