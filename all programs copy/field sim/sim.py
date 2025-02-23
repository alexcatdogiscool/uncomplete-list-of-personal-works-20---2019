import numpy as np
import math
import random
import pygame as pg



width = 600
height = 600

sky = (150,150,150)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()


def pythag(sx, ex, sy, ey):
    return math.sqrt((sx-ex)**2 + (sy-ey)**2)


class vector:
    def __init__(self):
        self.x = 300
        self.y = 300

        self.size = 100

        self.r = 0
        self.g = 0
        self.b = 0

        self.xmult = 0
        self.ymult = 0

        self.size = 1

    def draw(self):
        pg.draw.rect(screen, (self.r,self.g,self.b), (int(self.x),int(self.y), self.size,self.size))


class light:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)

        self.length = random.uniform(20,600)
        self.length2 = random.uniform(20,600)


vectors = []
vecsize = 100000

dim = int(math.sqrt(vecsize))

xcount = 0
ycount = 0

for i in range(vecsize):
    i = vector()
    
    i.x = (width/dim)*xcount
    i.y = (height/dim)*ycount
    i.size = width/(dim)+1
    xcount += 1
    if xcount == dim:
        xcount = 0
        ycount += 1
    vectors.append(i)


lights = []
lightsize = 3
for i in range(lightsize):
    i = light()
    i.xmult = random.uniform(0.5, 5)
    i.ymult = random.uniform(0.5, 5)
    lights.append(i)





num = 0
running = True
while running:
    num += 0.1
    mpos = (pg.mouse.get_pos())

    count = 0
    for l in lights:
        if count == 0:
            l.x, l.y = mpos
        else:
            l.x, l.y = math.sin(num*l.xmult)*l.length+300, math.cos(l.ymult*num)*l.length2+300
        count += 1
    
    for v in vectors:
        tempr = 0
        tempg = 0
        tempb = 0
        for l in lights:

            dist = pythag(v.x, l.x, v.y, l.y)
            
            tempr += 10/((dist+0.001))*l.r
            tempg += 10/((dist+0.001))*l.g
            tempb += 10/((dist+0.001))*l.b

        if tempr > 255:
            tempr = 255
        if tempg > 255:
            tempg = 255
        if tempb > 255:
            tempb = 255

    
        v.r = tempr
        v.g = tempg
        v.b = tempb

        v.draw()








    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
