import pygame as pg
import math
import random
import time



def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5



width = 800
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



s1 = (int(width/2 + 50), 700)
s2 = (int(width/2 - 50), 700)

p = (0,0)



running = True
while running:
    mx,my = pg.mouse.get_pos()
    p = mx,my

    pg.draw.circle(screen, black, (mx,my), 5)

    pg.draw.circle(screen, red, (s1[0],s1[1]), 10)
    pg.draw.circle(screen, red, (s2[0],s2[1]), 10)

    d2 = pythag(s1[0],s1[1], p[0],p[1])
    d1 = pythag(s2[0],s2[1], p[0],p[1])
    
    w = -(d2**2 - d1**2 + 10000) / 200
    l = (d2**2 - w**2)**0.5

    pg.draw.line(screen, black, (s1[0],s1[1]), ((w + s1[0]), (-l + s1[1])))














    pg.display.flip()
    screen.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False