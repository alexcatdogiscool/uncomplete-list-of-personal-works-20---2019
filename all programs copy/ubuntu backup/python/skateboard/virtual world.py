import math
import pygame as pg
import numpy as np
import time

width, height = 600,600
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
sky = (112, 232, 250)

screen = pg.display.set_mode((width,height))
screen.fill(sky)
pg.display.flip()


class board:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.a = 0
        self.v = 0.005
        self.rad = 100
        self.frontpx = self.x - self.rad
        self.frontpy = self.y
        self.endpx = self.x + self.rad
        self.endpy = self.y
    def rot(self):
        self.a += self.v
        self.frontpx = math.cos(self.a) * self.rad + self.x
        self.frontpy = math.sin(self.a) * self.rad + self.y

        self.endpx = math.cos(self.a) * -self.rad + self.x
        self.endpy = math.sin(self.a) * -self.rad + self.y
    def draw(self):
        pg.draw.line(screen, black, (self.x,self.y), (self.frontpx,self.frontpy), 3)
        pg.draw.line(screen, black, (self.x,self.y), (self.endpx,self.endpy), 3)





px1 = 0
px2 = 0
px3 = 0
py1 = 0
py2 = 0
py3 = 0

b = board()

frame = 0
running = True
while running:
    mx,my = pg.mouse.get_pos()
    if frame == 0:
        px3 = mx
        py3 = my
    if frame == 1:
        px2 = mx
        py2 = my
    if frame == 3:
        px1 = mx
        py1 = my
        frame = 0



    b.rot()
    b.draw()




    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(sky)

    #time.sleep(0.5)

