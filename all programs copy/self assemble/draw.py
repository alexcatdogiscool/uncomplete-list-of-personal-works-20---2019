import pygame as pg
import math
import funcs
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

nodeLen = 50

nodes = []

nodeNumbers = 10
nodeRad = 5

running = True
while running:
    mx, my = pg.mouse.get_pos()
    m1,m3,m2 = pg.mouse.get_pressed()

    if len(nodes) == 0:
        funcs.ghostCirc(screen, mx,my, nodeRad)
        if m1 and not m1pre:
            nodes.append([mx,my])
    else:
        angle = math.atan2(my - nodes[-1][1], mx - nodes[-1][0])
        x = int((math.cos(angle) * 2*nodeRad) + nodes[-1][0])
        y = int((math.sin(angle) * 2*nodeRad) + nodes[-1][1])
        funcs.ghostCirc(screen, x,y, nodeRad)
        if m1 and funcs.norm(mx - nodes[-1][0], my - nodes[-1][1]) > nodeRad:
            if len(nodes) < nodeLen:
                nodes.append([x,y])

    
    if m2 and not m2pre:
        npNodes = np.array(nodes)
        np.save("nodes", npNodes)
        print(len(nodes))
        running = False
        
    
    

            




    funcs.drawNodes(screen, nodes, nodeRad)

    m2pre = m2
    m1pre = m1
    pg.display.flip()
    screen.fill(sky)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False