import math
import pygame as pg
import numpy as np
import time
import random

width = 800
height = 800

white = (255,255,255)
black = (0,0,0)
red = (209, 71, 71)
green = (0,255,0)
sky = (50, 168, 82)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


class board:
    def __init__(self):
        self.r = 1
    def draw(self):
        pg.draw.circle(screen, red, (int(width/2), int(width/2)), int((self.r/2) * scale))


db = []
for i in range(1):
    i = board()
    db.append(i)

dx = 0
dy = 0

scale = width

score = 0
scores = []
avg = 0
m1p = 0
running = True
while running:
    m1,m2,m3 = pg.mouse.get_pressed()
    mx,my = pg.mouse.get_pos()

    #if m1 == 1 and m1p == 0:
    dx = random.uniform(0,1) * scale
    dy = random.uniform(0,1) * scale



    for b in db:
        dst = (((400-dx)**2 + (400-dy)**2)**0.5)/400
        if dst < b.r:# and (m1-m1p) == 1:
            score += 1
            b.r = (b.r**2 - dst**2)**0.5
            #print(dst)
        else:#if m1-m1p == 1 and dst > b.r:
            scores.append(score)
            score = 0
            b.r =1
            avg = sum(scores)/len(scores)
            print(avg)

        b.draw()
        pg.draw.circle(screen, white, (int(dx),int(dy)), 5)










    pg.display.flip()
    screen.fill(sky)
    m1p,m2p,m3p = m1,m2,m3
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False