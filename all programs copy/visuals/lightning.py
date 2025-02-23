import pygame as pg
import numpy as np
import math
import random
import time


def pythag(sx,sy, ex,ey):
    if abs(sx-ex) < 50 or abs(sy-ey) < 50:
        return ((sx-ex)**2 + (sy-ey)**2)**0.5
    else:
        return 100



width = 1000
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



class node:
    def __init__(self):
        self.x = random.uniform(0,width)
        self.y = random.uniform(0,height)

        self.id = 0

    def draw(self):
        pg.draw.circle(screen, white, (int(self.x), int(self.y)), 5)
        




nodes = []
nodesize = 10000
for i in range(nodesize):
    num = i
    i = node()
    i.id = num
    if i.id == 0:
        i.x = width
        i.y = height/2
    nodes.append(i)


width = 5
twidth = 5

cur = 0
was = []

striking = True
branching = False


running = True
while running:


    if striking == True:
        dist = 3000
        for n in nodes:
            #n.draw()
            temp = pythag(nodes[cur].x, nodes[cur].y, n.x, n.y)
            if n.x > nodes[cur].x:
                temp += 10
                pass
            #if n.y < nodes[cur].y:
             #   temp += 10

            if temp < dist:
                av = True
                for w in was:
                    if n.id == w:
                        av = False
                if av == True:
                    dist = temp
                    tempid = n.id

        if random.uniform(1,100) < 2:
            branching = True
            print(branching)

            tnodes = []
            tnodesize = 3000
            for i in range(tnodesize):
                num = i
                i = node()
                i.id = num
                i.x = random.uniform(nodes[cur].x - 200, nodes[cur].x + 200)
                i.y = random.uniform(nodes[cur].y - 200, nodes[cur].y + 200)
                if num == 0:
                    i.x = nodes[cur].x
                    i.y = nodes[cur].y
                tnodes.append(i)

                twas = []
                tcur = 0
                twidth = width

                if random.randint(1,2) == 1:
                    up = True
                else:
                    up = False

        pg.draw.line(screen, white, (nodes[cur].x, nodes[cur].y), (nodes[tempid].x, nodes[tempid].y), int(width))
        was.append(cur)
        cur = tempid
        width -= 0.005
        #width = 1
        #twidth = width

    
    if branching == True:
        dist = 1000
        twidth -= 0.1
        for n in tnodes:
            #n.draw()
            temp = pythag(tnodes[tcur].x,tnodes[tcur].y, n.x,n.y)
        
            if n.x > tnodes[tcur].x:
                temp += 10
            if up == True:
                if n.y > tnodes[tcur].y:
                    temp += 10
            else:
                if n.y < tnodes[tcur].y:
                    temp += 10
                


            if temp < dist and temp > 0.1:

                av = True
                for w in twas:
                    if w == n.id:
                        av = False
                if av == True:
                    dist = temp
                    ttempid = n.id

        pg.draw.line(screen, white, (tnodes[tcur].x, tnodes[tcur].y), (tnodes[ttempid].x, tnodes[ttempid].y), int(twidth))
        twas.append(tcur)
        tcur = ttempid
            

        

        

    if nodes[cur].x < 20 or nodes[cur].y > height-20:
        striking = False
        pass


        








    pg.display.flip()
    #screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
