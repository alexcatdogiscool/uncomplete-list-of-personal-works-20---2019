import random
import pygame as pg
import functions as func

width = 800
height = 600
screen = pg.display.set_mode((width, height))


class food:
    def __init__(self):
        self.id = 0
        self.x = random.randint(0,800)
        self.y = random.randint(0,600)
        self.size = 1
    def draw(self):
        pg.draw.circle(screen, (55, 102, 16), (self.x, self.y), int(self.size * 15))
    def grow(self):
        self.size += func.growth(self.size)
    def eat(self, bite):
        if self.size > bite*0.2:
            self.size -= bite*0.2
        if self.size < 0:
            self.size = 0