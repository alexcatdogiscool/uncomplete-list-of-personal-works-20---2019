import gates
import gate as g
import math
import numpy as np
import pygame as pg
import time
import functions as func


width = 800
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (158, 228, 255)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()

ANDS = []
ORS = []
NANDS = []
NORS = []
XORS = []
XNORS = []
NOTS = []



m1p,m2p,m3p = 0,0,0

origin = (0,0)
running = True
while running:
    mx,my = pg.mouse.get_pos()
    m1,m2,m3 = pg.mouse.get_pressed()


    if m1 == 1 and m1p == 0:
        for i in range(1):
            i = g.gate()
            i.x = mx
            i.y = my
            ORS.append(i)


    for c in ANDS:
        c.think()
        c.draw()
    for c in NANDS:
        c.think()
        c.draw()
    for c in ORS:
        c.think()
        c.draw()
    for c in NORS:
        c.think()
        c.draw()
    for c in XORS:
        c.think()
        c.draw()
    for c in XNORS:
        c.think()
        c.draw()
    for c in NOTS:
        c.think()
        c.draw()
    




    m1p,m2p,m3p = m1,m2,m3
    pg.display.flip()
    screen.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False