import numpy as np
import math
import pygame as pg
import shape
import random



def pythag(sx,sy,sz, ex,ey,ez):
    return ((sx-ex)**2 + (sy-ey)**2 + (sz-ez)**2)**0.5



width = 600
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (215,215,215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.lit = False
        self.r = 0
        self.g = 0
        self.b = 0
    def draw(self):
        if self.r > 255:
            self.r = 255
        if self.g > 255:
            self.g = 255
        if self.b > 255:
            self.b = 255

        if self.r < 0:
            self.r = 0
        if self.g < 0:
            self.g = 0
        if self.b < 0:
            self.b = 0

        if self.lit == True:
            pg.draw.rect(screen, (self.r, self.g, self.b), (int(self.x), int(self.y), int(self.size), int(self.size)))
        else:
            pg.draw.rect(screen, (200,200,200), (int(self.x), int(self.y), int(self.size), int(self.size)))

pointsize = 10000
points = []
pstep = width/(pointsize**0.5)
xstep = 0
ystep = 0
print(pstep)
for i in range(pointsize):
    num = i
    i = point()
    i.size = pstep+1
    i.x = xstep * pstep
    i.y = ystep * pstep
    if xstep == int(pointsize**0.5)-1:
        xstep = -1
        ystep += 1

    xstep += 1

    points.append(i)

sphs = []
for i in range(2):
    num = i
    i = shape.sphere()
    i.id = num
    i.x = random.randint(0,width)
    i.y = random.randint(0,height)
    #i.z = 100
    i.r = random.randint(0,255)
    i.g = random.randint(0,255)
    i.b = random.randint(0,255)
    i.rad = 100
    sphs.append(i)

running = True
while running:

    for s in sphs:
        if s.id == 0:
            s.x, s.y = pg.mouse.get_pos()
        #s.z -= 0.5

    for p in points:
        p.lit = False
        distold = 1000
        count = 1
        for s in sphs:
            dist = pythag(p.x,p.y,0, s.x,s.y,s.z) - s.rad

            #if dist < 0 and distold < 0:
             #   p.lit = True 
              #  p.r = s.r
               # p.g = s.g
                #p.b = s.b
                
            if dist < 0:
                p.lit = True
                p.r = s.r
                p.g = s.g
                p.b = s.b

            if dist * distold < 300:
                p.lit = True
                #p.r = (sphs[0].r * (2*dist)/(dist+distold+0.01) + (sphs[1].r * 1-((2*dist)/(dist+distold+0.01))))
                #p.g = (sphs[0].g * (2*dist)/(dist+distold+0.01) + (sphs[1].g * 1-((2*dist)/(dist+distold+0.01))))
                #p.b = (sphs[0].b * (2*dist)/(dist+distold+0.01) + (sphs[1].b * 1-((2*dist)/(dist+distold+0.01))))
                ratio = dist/(distold+0.001)
                p.r = (ratio*sphs[0].r) + (1-(ratio*sphs[1].r))
                p.g = (ratio*sphs[0].g) + (1-(ratio*sphs[1].g))
                p.b = (ratio*sphs[0].b) + (1-(ratio*sphs[1].b))

            distold = dist
            count += 1

        p.draw()
        




    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False