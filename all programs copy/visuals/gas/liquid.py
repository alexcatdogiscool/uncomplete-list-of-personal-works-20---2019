import math
import random
import pygame as pg
import numpy as np


def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5

def angle(sx,sy, ex,ey):
    return math.atan2((ey-sy), (ex-sx))





width = 1000
height = 300

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()



class particle:
    def __init__(self):
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)

        self.v = 1
        self.a = random.uniform(0, 2*math.pi)

        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        
    def draw(self):
        pg.draw.circle(screen, (self.r, self.g, self.b), (int(self.x), int(self.y)), 1)
    def step(self):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v



nodesize = 100
nodes = []
for i in range(nodesize):
    i = particle()
    nodes.append(i)


g = 0.01

frame = 0
running = True
while running:
    frame += 1
    width = 300
    width = (30*(math.sin(frame/20)+1))+300
    #width -= 0.2
    pg.draw.line(screen, red, (width,0),(width, height), 3)

    for n in nodes:
        if n.x > width:
            n.a = math.pi-n.a
            n.x = width - 1
            #n.step()
        if n.x < 0:
            n.a = ((math.pi-n.a))
            n.x = 1

        if n.y > height:
            n.a = ((math.pi/2)-n.a) - math.pi/2
        if n.y < 0:
            n.a = ((math.pi/2)-n.a) - math.pi/2
        n.step()
        n.draw()


    for n in nodes:
        dist = 50
        cols = 0
        for m in nodes:
            if abs(n.x - m.x) > 70:
                break
            if abs(n.y - m.y) > 70:
                break
            
            temp = pythag(n.x,n.y,m.x,m.y)
            if temp < dist and temp > 1:
                dist = temp
            
            if dist < 50:
                cols += 1
                a = angle(m.x,m.y, n.x, n.y)
                m.a = ((math.pi)-a)
                #m.v -= 0.1
                #break
        print(cols)
#
 #   for n in nodes:
  #      vy = math.sin(n.a)# + g
   #     vx = math.cos(n.a)
    #    n.a = math.atan(vy/vx)
     #   n.v = ((vx**2) + (vy**2))**0.5


    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False

