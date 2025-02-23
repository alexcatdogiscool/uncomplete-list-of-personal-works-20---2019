import math
import random
import numpy




class agent:
    def __init__(self):
        self.needs = 0.5#if below 0, die
        self.wants = 0.5#the heigher the happier
        self.happy_line = 1  # needs+wants = happyness, goal is to get above happy_line

        self.mot_mov = random.uniform(0,4)
        self.motivation = (-4*self.wants*(self.wants-self.mot_mov))/(self.mot_mov**2) # they are more motivated when they have more of what the want but to a point, then the opposite is true

        self.money = 0
        self.salery = random.uniform(0.3,1.3)