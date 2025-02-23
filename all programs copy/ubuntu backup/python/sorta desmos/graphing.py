import pygame as pg
import numpy as np
import math


width, height = 800,800
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
sky = white

screen = pg.display.set_mode((width,height))
screen.fill(sky)
pg.display.flip()

def func(x, b):
    y = x**b
    return y * -1


class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.colour = black
        self.calced = False
    def draw(self, cent, view):
        pg.draw.circle(screen, self.colour, ((((width/2)/(view[0]/2))*self.x)+cent[0], (((height/2)/(view[1]/2))*self.y)+cent[1]), 3)

##### vars
resolution = 100 # points per unit
startx = -5
endx = 5
viewrange = (10,10) #widtj, height
viewcent = (400,400) #0,0 of graph mapped to x,y on viewcent


line = []
for i in range(int((endx-startx)*resolution)):
    num = i
    i = point()
    i.x = (num/resolution) + startx
    i.y = func(i.x,0)
    i.calced = True
    line.append(i)

frame = -1
running = True
while running:
    frame += 1

    i = -1
    for p in line:
        i += 1
        p.x = (i/resolution) + startx
        p.y = func(p.x, (1+(frame/300))).real
        #print(p.y)
        p.draw(viewcent, viewrange)





    pg.display.flip()
    screen.fill(sky)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    