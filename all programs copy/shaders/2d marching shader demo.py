import pygame as pg
import math
import random
import numpy as np

random.seed(1)
np.random.seed(1)


sky = (0,0,0)

width = 800
height = 700

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()


mousey = 0

objx = int(width/2)
objy = int(height/2)

dist = 2

angle = 1.74

pointx = 0
pointy = 420


running = True
while True:
    mousex, mousey = pg.mouse.get_pos()



    pg.draw.circle(screen, (255,255,255), (objx, objy), 50, 1)

    for i in range(10):


        dist = (math.sqrt((pointx - objx)**2 + (pointy - objy)**2)) - 50

        pg.draw.circle(screen, (255,255,255), (pointx, pointy), int(dist+1), 1)
        pg.draw.line(screen, (255,255,255), (pointx, pointy), (dist, pointy), 1)

        pointx += int(dist)
        pointy += int(math.sin(angle))
        
        pg.display.flip()

        



    pointx = 0
    pointy = mousey



    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
