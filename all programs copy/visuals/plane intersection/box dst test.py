import numpy as np
import pygame as pg
import math


def pythag(xy):
    x, y = xy
    return (x**2 + y**2)**0.5

def boxdst(p, c, size):
    pmc = tuple(abs(np.subtract(p, c)))
    offset = tuple(np.subtract(pmc, size))

    #print(pmcms)
    #min(max(q.x,max(q.y,q.z)),0.0)

    unsigned = pythag(max(offset, (0,0)))
    inside = max(min(offset, (0,0)))
    
    return inside + unsigned
    #return 100


width = 600
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (215,215,215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()




dist = 600
p = (0,0)

c = (300,300)
size = (40,60)

running = True
while running:

    dist = boxdst(p, c, size)

    p = pg.mouse.get_pos()
    pg.draw.circle(screen, black, (p[0], p[1]), int(abs(dist)))

    pg.draw.rect(screen, black, (c[0]-size[0], c[1]-size[1], size[0]*2, size[1]*2),3)


    #print(max())





    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False