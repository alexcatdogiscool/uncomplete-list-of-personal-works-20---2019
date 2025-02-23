import pygame as pg
import math
import time
import numpy as np
import node
import functions as func
import ball


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


nodesize = 50
ropelen = 400
ropespace = ropelen/nodesize
nodes = []
for i in range(nodesize):
    num = i
    i = node.node()
    i.y = height/2
    i.x = num * ropespace
    i.len = ropespace - 5
    i.id = num
    if num == 0 or num == nodesize-1:
        i.fixed = True
    nodes.append(i)


balls = []
for i in range(1):
    i = ball.ball()
    i.x = width/2 - 100
    i.y = 250
    balls.append(i)


g = 0.003

frame = 0
running = True
while running:
    frame += 1
    mx, my = pg.mouse.get_pos()
    m1,m2,m3 = pg.mouse.get_pressed()

    for n in nodes:
        f = n.mass * g
        n.a, n.v = func.vectadd(n.a,n.v,1, math.pi/2, g,1, 1)
        
    for n in range(int(nodesize-1)):
        dst = func.norm(nodes[n].x - nodes[n+1].x, nodes[n].y - nodes[n+1].y)
        force = func.elastic(nodes[n].len, dst, nodesize * 0.001) * nodes[n+1].mass
        angle = math.atan2(nodes[n].y - nodes[n+1].y, nodes[n].x - nodes[n+1].x)
        nodes[n].a, nodes[n].v = func.vectadd(nodes[n].a,nodes[n].v,1, math.pi+angle, force,1, 0.999)

    for m in range(int(nodesize)):
        n = ((nodesize-1) - m)
        dst = func.norm(nodes[n].x - nodes[n-1].x, nodes[n].y - nodes[n-1].y)
        force = func.elastic(nodes[n].len, dst, nodesize * 0.001) * nodes[n-1].mass
        angle = math.atan2(nodes[n].y - nodes[n-1].y, nodes[n].x - nodes[n-1].x)
        nodes[n].a, nodes[n].v = func.vectadd(nodes[n].a,nodes[n].v,1, math.pi+angle, force,1, 0.999)

    for n in nodes:
        mdst = func.norm(mx-n.x, my-n.y)
        if mdst < 5 and m1 == 1:
            n.x, n.y = mx, my

    for n in range(nodesize-1):
        pg.draw.line(screen,(255,0,0),(int(nodes[n].x),int(nodes[n].y)),(int(nodes[n+1].x),int(nodes[n+1].y)),5)


    #nodes[0].x, nodes[0].y = mx,my
    
    speed = 31
    f = 1/((2*math.pi)/(1/speed))
    #print(f)
    #nodes[nodesize-1].y = (math.sin(frame/speed) * 20) + 300

    for b in balls:
        d = 100
        for n in range(nodesize-1):
            temp = func.dst((nodes[n].x, nodes[n].y),(nodes[n+1].x, nodes[n+1].y),(b.x,b.y))
            if temp < d:
                d = temp
            if d < b.rad:
                angle = (math.atan2(b.y-nodes[n].y, b.x-nodes[n].x) + math.atan2(b.y-nodes[n+1].y, b.x-nodes[n+1].x))/2 + math.pi/2
                over = (b.rad - d)*0.01
                b.a, b.v = func.vectadd(b.a,b.v,b.mass,angle,over,(nodes[n].mass + nodes[n+1].mass)/2,0.999)
        #pg.draw.circle(screen, black, (int(b.x),int(b.y)), int(d), 1)


    ###############################
    for n in nodes:
        n.step()
        n.draw()


    for b in balls:
        b.a, b.v = func.vectadd(b.a,b.v,b.mass, math.pi/2, g, 1,1)
        if m3 == 1:
            b.x, b.y = mx,my
            b.v = 0
        b.step()
        b.draw()



    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
