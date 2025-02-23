import math
import random
import pygame as pg
import numpy as np


def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5

def angle(sx,sy, ex,ey):
    return math.atan2((ey-sy), (ex-sx))





width = 1000
height = 800

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
    def draw(self):
        pg.draw.circle(screen, white, (int(self.x), int(self.y)), 5)
    def step(self):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v



nodesize = 300
nodes = []
for i in range(nodesize):
    i = particle()
    nodes.append(i)

frame = 0
running = True
while running:
    frame += 1
    width = (30*(math.sin(frame/20)+1))+300
    width -= 0.2
    pg.draw.line(screen, red, (width,0),(width, height), 3)

    for n in nodes:
        if n.x > width:
            n.a = ((math.pi/2)-n.a) + math.pi/2
            n.x = width-1
            n.step()
        if n.x < 0:
            n.a = ((math.pi/2)-n.a) + math.pi/2
            n.x = 1

        if n.y > height:
            n.a = ((math.pi/2)-n.a) - math.pi/2
        if n.y < 0:
            n.a = ((math.pi/2)-n.a) - math.pi/2
        n.step()
        n.draw()


    for n in nodes:
        dist = 1000
        for m in nodes:
            temp = pythag(n.x,n.y,m.x,m.y)
            if temp < dist and temp > 1:
                dist = temp

            if dist < 5:
                a = angle(m.x,m.y, n.x, n.y)
                m.a = ((math.pi/2)-m.a) - math.pi/2
                break



    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False

