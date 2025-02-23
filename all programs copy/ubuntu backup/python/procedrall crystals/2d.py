import math
import numpy as np
#import cv2
import pygame as pg
import random


width, height = 800,800
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
sky = (112, 232, 250)

screen = pg.display.set_mode((width,height))
screen.fill(sky)
pg.display.flip()

def pythag(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def angle(x1,y1,x2,y2):
    return (math.atan2((y2-y1),(x2-x1)))

def vectadd(a1,v1,a2,v2):
    v1x = math.cos(a1)*v1
    v1y = math.sin(a1)*v1
    v2x = math.cos(a2)*v2
    v2y = math.sin(a2)*v2
    vx = v1x + v2x
    vy = v1y + v2y
    a = math.atan2(vy,vx)
    v = (vx**2 + vy**2)**0.5
    return a,v

def force(x1,y1,x2,y2, G):
    d = pythag(x1,y1,x2,y2)
    return G*d**(-2)
    


class ion:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
        self.v = 0

        self.charge = 1
        self.rad = 20
    def run(self, temp):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v

        self.x += math.cos(random.uniform(0,2*math.pi)) * random.uniform(temp*0.2, temp)
        self.y += math.sin(random.uniform(0,2*math.pi)) * random.uniform(temp*0.2, temp)

    def draw(self):
        if self.charge == 1:
            pg.draw.circle(screen, red, (self.x,self.y), self.rad)
        else:
            pg.draw.circle(screen, blue, (self.x,self.y), self.rad)


ions = []
psize = 0
for i in range(psize):
    i = ion()
    i.x = random.uniform(250,650)
    i.y = random.uniform(250,650)
    i.a = random.uniform(0, math.pi*2)
    i.v = 0
    i.charge = random.choice([-1,1])
    if i.charge == 1:
        i.rad = 10
    ions.append(i)



G = 5
temp = 0.3

m1p = False
m2p = False

running = True
while running:
    m1,m3,m2 = pg.mouse.get_pressed()
    mx,my = pg.mouse.get_pos()
    if m1 == True and m1p == False:
        for i in range(1):
            i = ion()
            i.x = mx
            i.y = my
            i.charge = 1
            ions.append(i)
    if m2 == True and m2p == False:
        for i in range(1):
            i = ion()
            i.x = mx
            i.y = my
            i.charge = -1
            ions.append(i)
    


    for i in ions:
        for o in ions:
            d = pythag(i.x,i.y,o.x,o.y)
            if d != 0 and d > i.rad+o.rad+2:
                f = force(i.x,i.y,o.x,o.y,G)
                if o.charge == i.charge:
                    f *= -1
                a = angle(i.x,i.y,o.x,o.y)
                i.a, i.v = vectadd(i.a,i.v,a,f)
            if d < i.rad+o.rad and d > 0:
                d -= (i.rad+o.rad)
                a = angle(i.x,i.y,o.x,o.y)
                i.x += math.cos(a)*d
                i.y += math.sin(a)*d
                i.v *= 0.9
        i.run(temp)

        if i.x < 0:
            i.x = width
        if i.x > width:
            i.x = 0
        
        if i.y < 0:
            i.y = height
        if i.y > height:
            i.y = 0

        i.draw()
            





    m1p = m1
    m2p = m2
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(sky)