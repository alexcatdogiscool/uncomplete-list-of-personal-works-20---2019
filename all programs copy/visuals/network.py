import pygame as pg
import numpy as np
import math
import random
import time


def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5



width = 1000
height = 800

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(white)
pg.display.flip()


class node:
    def __init__(self):
        self.x = random.uniform(0, width)
        self.y = random.uniform(0, height)

        self.a = random.uniform(0, 2*math.pi)

        self.id = 0

        self.ill = False

    def draw(self):
        if self.ill == False:
            pg.draw.circle(screen, white, (int(self.x), int(self.y)), 5)
        if self.ill == True:
            pg.draw.circle(screen, green, (int(self.x), int(self.y)), 5)

    def step(self):
        self.x += math.cos(self.a) * 1
        self.y += math.sin(self.a) * 1



nodes = []
nodesize = 100
for i in range(nodesize):
    num = i
    i = node()
    i.id = num
    nodes.append(i)

frame = 0
running = True
while running:
    frame += 1


    if frame == 200:
        for n in nodes:
            n.a = random.uniform(0, 2*math.pi)
        frame = 0


    for i in range(4):
        for n in nodes:
            
        
            for nt in nodes:
                dist = pythag(n.x, n.y,  nt.x, nt.y)
                if dist < 100 and dist > 0.1:
                
                    if n.ill == True:
                        nt.ill = True

                    if n.ill == False:
                        #pg.draw.line(screen, white, (int(n.x), int(n.y)), (int(nt.x), int(nt.y)),1)
                        pass
                    else:
                        pg.draw.line(screen, green, (int(n.x), int(n.y)), (int(nt.x), int(nt.y)),1)
        

            if n.id == 0:
                n.x, n.y = pg.mouse.get_pos()
                n.ill = True


            if n.id != 0:
                n.step()
                #pass

    for n in nodes:
        n.draw()
        n.ill = False
        if n.id == 0:
            n.ill = True
        

        if n.x > width:
            n.x = 0
        if n.x < 0:
            n.x = width

        if n.y > height:
            n.y = 0
        if n.y < 0:
            n.y = height
        
        

        








    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
