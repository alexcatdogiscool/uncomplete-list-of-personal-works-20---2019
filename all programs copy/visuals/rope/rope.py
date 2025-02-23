import numpy as np
import random
import pygame as pg
import math



def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5


width = 800
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





class node:
    def __init__(self):
        self.x = 0
        self.y = height/2
        self.a = 0
        self.v = 0
        self.id = 0
    def step(self):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v
    def draw(self):
        pg.draw.circle(screen, red, (int(self.x), int(self.y)), 5)



ropelen = 400
elas = 1
nodesize = 10
qual = ropelen/nodesize
nodes = []
for i in range(nodesize):
    num = i
    i = node()
    i.id = num

    i.y += num*10

    i.x = qual * num
    if num > 0:
        i.x -= 10

    nodes.append(i)


g = 0.0

running = True
while running:




    for n in nodes:
        n.draw()
        n.step()
        if n.id != 0:
            xv = math.sin(n.a) * n.v
            yv = math.cos(n.a) * n.v
            yv += g
            n.v = (xv**2 + yv**2)**0.5
            n.a = math.atan(xv/yv+0.0001)

        
            


    for i in range(nodesize-1):
        dst = pythag(nodes[i].x,nodes[i].y, nodes[i+1].x,nodes[i+1].y)
        if dst > qual:
            #nodes[i+1].v *= -1
            nodes[i+1].v -= 0.1
            #nodes[i+1].step()
            """
            angle = math.atan2(nodes[i].y, nodes[i+1].x)
            yf = math.sin(angle) * (2*g)
            xf = math.cos(angle) * (2*g)

            xv = math.sin(nodes[i+1].a) * nodes[i+1].v
            yv = math.cos(nodes[i+1].a) * nodes[i+1].v
            
            xv -= xf
            yv -= yf

            n.v = (xv**2 + yv**2)**0.5
            n.a = math.atan(xv/yv+0.0001)
            """






    for i in range(nodesize-1):
        pg.draw.line(screen, red, (int(nodes[i].x), int(nodes[i].y)), (int(nodes[i+1].x), int(nodes[i+1].y)), 2)





    

    pg.display.flip()
    screen.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False