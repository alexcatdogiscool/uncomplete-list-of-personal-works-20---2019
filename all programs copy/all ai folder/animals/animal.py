import math
import numpy as np
import random
import pygame as pg
import functions as f



width = 800
height = 600
screen = pg.display.set_mode((width, height))
class animal:
    def __init__(self):
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.a = 0
        self.v = 0
        self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.health = 0.5
        self.eating = 0
        self.birthing = 0
        self.age = 0
        self.kids = 0

        # brain structure.   inputs: closest things(angle, animal = 0, food = 1), closest animals colour, 
        # health, angle, velocity.    total inputs: 7
        # outputs:   angle, velocity, colour, eating, birthing(bool). total outs: 7
        self.brain = np.zeros((30))
        self.bias = np.random.uniform(-1,1,(30))
        self.weights = np.random.uniform(-1,1, (30,30))
    def step(self):
        self.x += self.v * math.cos(self.a)
        self.y += self.v * math.sin(self.a)
        self.health -= (0.1 * self.v) + (0.01 * self.health) + 0.05
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
        
    def draw(self):
        pg.draw.circle(screen, self.colour, (int(self.x), int(self.y)), 7)
    def think(self):
        #self.brain[0] = 0#do closest, angle
        #self.brain[1] = 0#do closest, type
        #self.brain[2] = 0#do closest colour, r
        #self.brain[3] = 0#g
        #self.brain[4] = 0#b
        self.brain[5] = self.health
        self.brain[6] = self.a/(math.pi*2)
        self.brain[7] = self.v

        self.brain = f.sigmoid(np.dot(self.brain, self.weights) + self.bias)

        self.a = self.brain[29] * math.pi*2
        self.v = self.brain[28]
        self.colour = (abs(self.brain[27]*255), abs(self.brain[26]*255), abs(self.brain[25]*255))
        self.eating = abs(self.brain[24])
        self.birthing = int(round(abs(self.brain[23])))
    def birth(self):
        weightx, weighty = random.randint(0,29), random.randint(0,29)
        weights = self.weights
        weights[weightx, weighty] = random.uniform(-1,1)
        bias = self.bias
        bias[random.randint(0,29)] = random.uniform(-1,1)
        return weights, bias
