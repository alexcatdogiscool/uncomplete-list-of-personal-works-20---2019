import math
import functions as func
import pygame as pg



class node:
    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.v = 0
        self.a = 0
        self.len = 0
        self.fixed = False
    def step(self):
        if self.fixed == False:
            self.x += math.cos(self.a) * self.v * 0.3
            self.y += math.sin(self.a) * self.v * 0.3
    def draw(self, screen):
        pg.draw.circle(screen, (255,0,0), (int(self.x), int(self.y)), 5)
