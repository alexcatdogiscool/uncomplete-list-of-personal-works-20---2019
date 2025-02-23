import math


class ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
        self.v = 1
        self.mass = 1
        self.rad = 30
        self.e = 0.85
    def step(self):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v