import math
import random


class sphere:
    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.rad = 20

        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)