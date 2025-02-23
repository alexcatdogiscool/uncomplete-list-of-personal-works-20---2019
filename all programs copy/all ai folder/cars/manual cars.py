import numpy as np
import pygame as pg
import math
import time
import random

def acc(vel):
    return 0.7*(math.log(20) * 20**(-vel + 3))/((1+20**(-vel + 3))**2)

def intercept(oa,ox,oy,olen, ta,tx,ty,tlen):
    m1 = math.tan(oa)
    m2 = math.tan(ta)
    h1 = ox
    k1 = oy
    h2 = tx
    k2 = ty
    ##### ONE #####
    h1 *= m1
    j1 = h1 + k1
    a1 = m1
    ##### TWO #####    
    h2 *= m2
    j2 = h2 + k2
    a2 = m2
    ##### SOLVE #####
    j1 -= j2
    a2 -= a1
    j1 /= a2+0.0001
    x = j1
    y = m1*(x-ox) + oy
    x *= -1
    #x -= tx
    #x *= -1
    #x += tx
    ltex = math.cos(ta) * tlen + tx
    ltey = math.sin(ta) * tlen + ty
    loex = math.cos(oa) * olen + ox
    loey = math.sin(oa) * olen + oy
    if x < ox or x > loex or y > tx or y < ltex:
        return x,y#None, None
    else:
        return x, y


width = 900
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


class car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = math.pi/4
        self.v = 0
        self.hit = False
    def step(self):
        self.v /= 1.001
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v
    def draw(self):
        if self.hit == False:
            pg.draw.circle(screen, black, (int(self.x), int(self.y)), 20, 3)
            pg.draw.line(screen, black, (int(self.x), int(self.y)), ((int(self.x + math.cos(self.a)*20)), (int(self.y + math.sin(self.a)*20))) )
        if self.hit == True:
            pg.draw.circle(screen, red, (int(self.x), int(self.y)), 20, 3)
            pg.draw.line(screen, red, (int(self.x), int(self.y)), ((int(self.x + math.cos(self.a)*20)), (int(self.y + math.sin(self.a)*20))) )


class line:
    def __init__(self):
        self.x = 70
        self.y = 50
        self.a = math.pi/4
        self.len = 300

        self.ex = math.cos(self.a) * self.len
        self.ey = math.sin(self.a) * self.len
    def draw(self):
        pg.draw.line(screen, black, (int(self.x), int(self.y)), (int(self.ex), int(self.ey)), 2)

lines = []
for i in range(1):
    i = line()
    lines.append(i)



cars = []
for i in range(1):
    i = car()
    cars.append(i)

frame = 0
running = True
while running:


    for l in lines:
        l.draw()

    for c in cars:
        c.step()
        c.draw()

        ########## CONTROLLER ##########
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            c.v += acc(c.v)
            if c.v > 0.8:
                c.v = 0.8
        if keys[pg.K_DOWN]:
            c.v /= 1.001
        if keys[pg.K_RIGHT]:
            c.a += 0.005
        if keys[pg.K_LEFT]:
            c.a -= 0.005


        ######### COLLISION #######

        for l in lines:
            ix, iy = intercept(c.a,c.x,c.y,100, l.a,l.x,l.y,l.len)
            print(ix,iy)
            if type(ix) == float:
                c.hit = True
                pg.draw.circle(screen, red, (int(ix), int(iy)), 5)
            else:
                c.hit = False



    pg.display.flip()
    screen.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
