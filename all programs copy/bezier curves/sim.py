import math
import numpy as np
import pygame as pg
import objects as objs
import funcs
import time




width = 800
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = black

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


curve = objs.curve([np.array([200,300]), np.array([200, 200]), np.array([600,200]), np.array([600,400])])

curves = []
curves.append(curve)

addP = 0
addPP = False
m1pre = False
running = True
while running:
    mx, my = pg.mouse.get_pos()
    m1,m3,m2 = pg.mouse.get_pressed()
    addP = 0

    for c in curves:
        c.draw(screen, 0.05, red, red)
        addP += c.dragPoint(mx,my,m1)
    for i in range(len(curves)-1):
        curves[i+1].points[1] = (curves[i].points[-1]-curves[i].points[-2])+curves[i].points[-1]
    if addP == 0 and m1 and not m1pre:
        P = (curves[-1].points[-1]-curves[-1].points[-2])+curves[-1].points[-1]
        i = objs.curve(np.array([curves[-1].points[-1], P, curves[-1].points[-1] + 0.75*(np.array([mx,my])), np.array([mx,my])]))
        curves.append(i)



    m1pre = m1
    addPP = addP
    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False