import pygame as pg
import random
import math
import funcs
import objects as objs


width = 800
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (158, 228, 255)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()



pend = funcs.makePend(4, 100, objs.vector(width/2, height/2), 0)

G = 0.2

clock = pg.time.Clock()
running = True
while running:
    clock.tick(60)
    mpos = objs.vector(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
    m1, m3, m2 = pg.mouse.get_pressed()

    for n in pend.nodes:
        if m1 and funcs.norm(mpos.x - n.pos.x, mpos.y - n.pos.y) < 10:
            #n = objs.node(mpos.x, mpos.y)
            n.pos = mpos
            n.vel = objs.vector(0,0)



    pend.move(G)
    pend.fixLen()
    pend.draw(screen)




    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
