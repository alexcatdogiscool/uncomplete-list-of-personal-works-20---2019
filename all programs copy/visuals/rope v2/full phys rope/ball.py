import math
import pygame as pg

width = 800
height = 600
screen = pg.display.set_mode((width, height))

class ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rad = 10
        self.a = 0
        self.v = 0
        self.mass = 1
    def step(self):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v
    def draw(self):
        pg.draw.circle(screen, (61, 186, 34), (int(self.x), int(self.y)), self.rad)