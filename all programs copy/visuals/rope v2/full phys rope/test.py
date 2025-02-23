import pygame as pg
import numpy as np


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


def dst(p1,p2,p3):
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)

    if p3[0] > p1[0] and p3[0] < p2[0]:
        d = np.linalg.norm(np.cross(p2-p1, p1-p3))/np.linalg.norm(p2-p1)
    else:
        d = 100
    return d


p1 = (100,100)
p2 = (500, 250)
p3 = (250,400)

p1 = np.asarray(p1)
p2 = np.asarray(p2)
p3 = np.asarray(p3)

running = True
while running:
    mx, my = pg.mouse.get_pos()
    p3 = (mx,my)
    p3 = np.asarray(p3)

    d = dst(p1,p2,p3)
    print(d)


    pg.draw.line(screen, black, (p1), (p2), 2)
    pg.draw.circle(screen, black, (p3), 5)
    pg.draw.circle(screen, black, (p3), int(d), 1)
    


    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False