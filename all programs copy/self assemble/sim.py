import pygame as pg
import numpy as np
import math
import random
import objects as objs
import random
import funcs

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
for i in range(nodeLen):
    if i == 0:
        i = objs.node()
        i.x = width/2
        i.y = height/2
    else:
        i = objs.node()
        i.x = random.randint(0,width)
        i.y = random.randint(0,height)
    nodes.append(i)


angles = []


clock = pg.time.Clock()

running = True
while running:
    clock.tick(30)
    mx, my = pg.mouse.get_pos()
    m1,m3,m2 = pg.mouse.get_pressed()


    for n in nodes:
        n.draw(screen)
        n.align(nodes)
        #n.a1 -= 0.001
        #n.a2 += 0.001

    
            




    if m2 and not m2pre:
        npNodes = np.load("nodes.npy")
        nodes[0].x = npNodes[0][0]
        nodes[0].t = npNodes[0][1]
        
        for i in range(len(npNodes) - 1):
            if i == 0:
                angles.append([0,math.atan2(npNodes[i][1] - npNodes[i+1][1], npNodes[i][0] - npNodes[i+1][0])])
            else:
                a1 = math.atan2(npNodes[i][1] - npNodes[i-1][1], npNodes[i][0] - npNodes[i-1][0])
                a2 = math.atan2(npNodes[i][1] - npNodes[i+1][1], npNodes[i][0] - npNodes[i+1][0])
                angles.append([a1,a2])
        a1 = math.atan2(npNodes[i][1] - npNodes[i-1][1], npNodes[i][0] - npNodes[i-1][0])
        a2 = 0
        angles.append([a1,a2])
        

        fixed = [True] * nodeLen
        while sum(fixed) > 0:
            for i in range(len(nodes)):
                if fixed[i]:
                    nodes[i].a1 += abs(funcs.fixAngle(angles[i][0]) - funcs.fixAngle(nodes[i].a1))/1600
                    nodes[i].a2 += abs(funcs.fixAngle(angles[i][1]) - funcs.fixAngle(nodes[i].a2))/1600

                nodes[i].align(nodes)
                nodes[i].draw(screen)

                
                if abs(funcs.fixAngle(nodes[i].a1) - funcs.fixAngle(angles[i][0])) < 0.04 and abs(funcs.fixAngle(nodes[i].a2) - funcs.fixAngle(angles[i][1])) < 0.04:
                    nodes[i].a1 = angles[i][0]
                    nodes[i].a2 = angles[i][1]
                    fixed[i] = False
            pg.display.flip()
            screen.fill(sky)
        


                




    pg.display.flip()
    screen.fill(sky)

    m2pre = m2
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False