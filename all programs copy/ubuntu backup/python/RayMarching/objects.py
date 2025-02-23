import math
import numpy as np


class ray:
    def __init__(self):
        self.pos = np.array([0,0.001,0])
        self.direction = np.array([0,0,1])
        self.colour = (50,50,50)
        self.alive = True
        self.imgx = 0
        self.imgy = 0

    def step(self, distance, thresh):
        if self.alive == True:
            self.pos = np.add(self.pos, distance*self.direction, out=self.pos, casting="unsafe")
            self.checkcoll(distance, thresh)

    def checkcoll(self,distance, thresh):
        if distance <= thresh:
            self.alive = False
            self.pos = (np.array([100,100,100]))
            self.colour = (255,255,255)


class sphere:
    def __init__(self):
        self.pos = np.array([0.00001,0,0])
        self.rad = 1