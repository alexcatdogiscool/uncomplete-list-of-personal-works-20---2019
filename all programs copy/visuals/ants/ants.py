import random
import math
import pygame as pg
from matplotlib import pyplot as plt

width = 750
height = 750

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


def pythag(sx,ex, sy,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5

class ant:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0

        self.type = 0

        self.acount = 0
        self.bcount = 0
        self.ccount = 0
        self.dcount = 0
    
    def step(self):
        self.x += math.cos(self.a) * 3
        self.y += math.sin(self.a) * 3

    def draw(self):
        if self.type == 0:
            pg.draw.circle(screen, (255,0,0), (int(self.x), int(self.y)), 3)
        
        if self.type == 1:
            pg.draw.circle(screen, (0,255,0), (int(self.x), int(self.y)), 3)

        if self.type == 2:
            pg.draw.circle(screen, (0,0,255), (int(self.x), int(self.y)), 3)

        if self.type == 3:
            pg.draw.circle(screen, (255,0,255), (int(self.x), int(self.y)), 3)

    def change(self):
        total = self.acount + self.bcount + self.ccount + self.dcount + 1

        if self.acount / total < 0.2:
            self.type = 0

        if self.bcount / total < 0.2:
            self.type = 1

        if self.ccount / total < 0.2:
            self.type = 2

        if self.dcount / total < 0.2:
            self.type = 3



ants = []
antsize = 300
for i in range(antsize):
    i = ant()
    i.type = 0
    i.x = random.randint(0, width)
    i.y = random.randint(0, height)
    i.a = random.uniform(0, 2*math.pi)
    
    ants.append(i)


ac = 0
bc = 0
cc = 0
dc = 0

on = []
tw = []
th = []
fo = []


frame = 0
running = True
for epoch in range(1000):
    frame += 1


    for a in ants:
        for at in ants:
            dist = pythag(a.x,at.x, a.y,at.y)
            if dist < 100 and dist > 1:
                if at.type == 0:
                    a.acount += 1
                if at.type == 1:
                    a.bcount += 1
                if at.type == 2:
                    a.ccount += 1
                if at.type == 3:
                    a.dcount += 1

        
        a.draw()
        a.step()
        

    if frame == 100:
        for a in ants:
            a.a = random.uniform(0, 2*math.pi)
            a.change()

            if a.type == 0:
                ac += 1
            if a.type == 1:
                bc += 1
            if a.type == 2:
                cc += 1
            if a.type == 3:
                dc += 1
        print(ac, bc, cc, dc)
        on.append(ac)
        tw.append(bc)
        th.append(cc)
        fo.append(dc)

        ac = 0
        bc = 0
        cc = 0
        dc = 0
        frame = 0


    for a in ants:
        if a.x > width:
            a.x = 0
        if a.x < 0:
            a.x = width

        if a.y > height:
            a.y = 0
        if a.y < 0:
            a.y = height








    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False



plt.plot(on)
plt.plot(tw)
plt.plot(th)
plt.plot(fo)

plt.show()