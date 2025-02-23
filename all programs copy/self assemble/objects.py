import math
import pygame as pg
import funcs



class node:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.a1 = 0
        self.a2 = math.pi
        self.rad = 5

    def align(self, Nlist):
        funcs.align(Nlist)

    def draw(self, surface):
        pg.draw.circle(surface, (0,0,0), (int(self.x), int(self.y)), self.rad)
        a1x = (math.cos(self.angle + self.a1) * self.rad/2) + self.x
        a1y = (math.sin(self.angle + self.a1) * self.rad/2) + self.y
        a2x = (math.cos(self.angle + self.a2) * self.rad/2) + self.x
        a2y = (math.sin(self.angle + self.a2) * self.rad/2) + self.y

        #pg.draw.circle(surface, (255,0,0), (int(a1x), int(a1y)), 2)
        #pg.draw.circle(surface, (0,0,255), (int(a2x), int(a2y)), 2)
        
        ax = math.cos(self.angle) * self.rad/2
        ay = math.sin(self.angle) * self.rad/2

        #pg.draw.line(surface, (0,255,0), (ax + self.x, ay + self.y),(self.x - ax, self.y - ay), 2)

        
        