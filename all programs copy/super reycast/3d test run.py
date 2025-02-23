import math
import numpy as np
import random
import cv2
import pygame as pg




width = 600
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(white)
pg.display.flip()





class ray:
    def __init__(self):
        
        self.ha = 0
        self.va = 0

        self.r = 0
        self.g = 0
        self.b = 0

class sphere:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.rad = 1

        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)

rays = []

xdim = 100
ydim = 100

raysize = xdim * ydim

xstep = (math.pi/2)/(xdim-1)
ystep = (math.pi/2)/(ydim-1)

count = -math.pi/4
count2 = -math.pi/4

frame = 0
for r in range(raysize):
    r = ray()
    
    if frame == xdim:
        count = -math.pi/4
        count2 += ystep
        frame = 0
    
    r.ha = (math.sin(count))/(math.cos(count))
    r.va = (math.sin(count2))/(math.cos(count2))
    count += xstep

    frame += 1

    rays.append(r)



sphs = []
sphsize = 1
for s in range(sphsize):
    s = sphere()
    
    s.x = 0
    s.y = 0
    s.z = 0

    sphs.append(s)


#################################
tick = 0

running = True
while running:
    tick += 0.01
    s.x = math.sin(tick)*5
    s.y = math.cos(tick)*5

    mouse = pg.mouse.get_pos()


    count = ((mouse[0]-300)*0.01)-math.pi/4
    count2 = ((mouse[1]-300)*0.01)-math.pi/4

    frame = 0
    for r in rays:
    
        if frame == xdim:
            count = ((mouse[0]-300)*0.01)-math.pi/4
            count2 += ystep
            frame = 0
    
        r.ha = (math.sin(count))/(math.cos(count))
        r.va = (math.sin(count2))/(math.cos(count2))
        count += xstep

        frame += 1

    
    ############################################
    
    for r in rays:
        for s in sphs:
            x = (-2*s.y-2*s.x*r.ha-2*s.z*r.va)/(2 * (1 + r.ha**2 + r.va**2))
            y = (1 + r.ha**2 + r.va**2)*(x)**2 - (-2*s.y-2*s.x*r.ha-2*s.z*r.va)*(x) + (s.y**2 + s.x**2 + s.z**2)

            if y < 1:
                r.r = s.r
                r.g = s.g
                r.b = s.b

    ############################################

    img = []
    for r in rays:
        img.append(r.r)
        img.append(r.g)
        img.append(r.b)

        r.r = 0
        r.g = 0
        r.b = 0

    img = np.array(img)
    img = img.reshape(xdim, ydim, 3)

    

    cv2.imwrite('img.png', img)
    img = cv2.imread('img.png')
    img = cv2.resize(img,None,fx=width/xdim, fy=height/ydim, interpolation = cv2.INTER_AREA)
    cv2.imwrite('img.png', img)

    img = pg.image.load('img.png')
    
    screen.blit(img, (0,0))
    
    ###########
    
    pg.display.flip()
    screen.fill(black)
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False

#################################









