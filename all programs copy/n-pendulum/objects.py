import funcs
import math
import pygame as pg


class vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

class node:
    def __init__(self, x,y):
        self.pos = vector(x,y)
        self.vel = vector(0,0)
    def move(self):
        self.pos = funcs.vectadd(self.pos, self.vel)
        


class pend:
    def __init__(self, nodes, lenList):
        self.start = nodes[0]
        self.lenList = lenList
        self.nodes = nodes

    def fixLen(self):
        self.nodes[0] = node(400,300)
        for k in range(10):
            for i in range(len(self.nodes)-1):
                d = funcs.norm(self.nodes[i].pos.x - self.nodes[i+1].pos.x, self.nodes[i].pos.y - self.nodes[i+1].pos.y)
                a = math.atan2(self.nodes[i].pos.y - self.nodes[i+1].pos.y, self.nodes[i].pos.x - self.nodes[i+1].pos.x)

                d -= self.lenList[i]

                #d *= 0.2

                moveVect1 = vector(math.cos(a)*d/2, math.sin(a)*d/2)
                moveVect2 = vector(math.cos(a+math.pi)*d/2, math.sin(a+math.pi)*d/2)

                self.nodes[i].pos = funcs.vectadd(self.nodes[i].pos, moveVect2)
                self.nodes[i+1].pos = funcs.vectadd(self.nodes[i+1].pos, moveVect1)

                self.nodes[i].vel = funcs.vectadd(self.nodes[i].vel, moveVect2)
                self.nodes[i+1].vel = funcs.vectadd(self.nodes[i+1].vel, moveVect1)

                


    def move(self, G):
        for n in self.nodes:
            n.vel.y += G
            n.move()
        self.nodes[0] = self.start
        


    def draw(self, surface):
        for i in range(len(self.nodes)-1):
            pg.draw.circle(surface, (0,0,0), (int(self.nodes[i].pos.x), int(self.nodes[i].pos.y)), 5)
            pg.draw.line(surface, (0,0,0), (int(self.nodes[i].pos.x), int(self.nodes[i].pos.y)), (int(self.nodes[i+1].pos.x), int(self.nodes[i+1].pos.y)), 2)
        pg.draw.circle(surface, (0,0,0), (int(self.nodes[-1].pos.x), int(self.nodes[-1].pos.y)), 5)
