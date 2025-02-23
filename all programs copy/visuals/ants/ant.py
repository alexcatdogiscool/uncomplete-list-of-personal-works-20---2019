import math
import pygame as pg


class ant:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0

        self.type = 0xc

        self.acount = 0
        self.bcount = 0
        self.ccount = 0
        self.dcount = 0
    
    def step(self):
        self.x += math.cos(self.a) * 3
        self.y += math.sin(self.a) * 3

    def draw(self):
        if self.type == 0:
            pg.draw.circle(screen, (255,0,0), (int(self.x), int(self.y)), 3)
        
        if self.type == 1:
            pg.draw.circle(screen, (0,255,0), (int(self.x), int(self.y)), 3)

        if self.type == 2:
            pg.draw.circle(screen, (0,0,255), (int(self.x), int(self.y)), 3)

        if self.type == 3:
            pg.draw.circle(screen, (255,0,255), (int(self.x), int(self.y)), 3)