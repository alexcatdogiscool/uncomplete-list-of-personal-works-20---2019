import pygame as pg
import math
import funcs
import numpy as np



class worm:
    def __init__(self, brainSize, x,y):
        self.x = x
        self.y = y

        self.hunger = 0
        self.noses = [0,0]
        self.touches = [0,0,0,0,0,0]#list of 6 evenly spaced sensors
        self.mouth = 0

        self.angle = 0
        self.angleV = 0

        self.touchangles = 2*math.pi/6

        self.z = np.zeros(brainSize)
        self.weights = np.random.uniform(size=(brainSize,brainSize))-0.5

    def output(self, board, scale):

        if self.x < 20:
            self.x = 20
        if self.x > 400-20:
            self.x = 400-20
        if self.y < 20:
            self.y = 20
        if self.y > 400-20:
            self.y = 400-20
        

        self.angleV = 0
        
        self.angleV += self.z[-1]*0.1
        self.angleV -= self.z[-2]*0.1
        
        self.angle += self.angleV
        if self.z[-1] and self.z[-2]:
            self.x += math.cos(self.angle)
            self.y += math.sin(self.angle)

        x = math.cos(self.angle) * 15 + self.x
        y = math.sin(self.angle) * 15 + self.y

        self.hunger += board[int(y//scale), int(x//scale)]
        board[int(y//scale), int(x//scale)] = 0

        return board


    def updateSenses(self, board, scale):
        board = board.reshape(50,50)
        #touch
        for i in range(6):
            x = math.cos(i*self.touchangles + self.angle) * 10 + self.x
            y = math.sin(i*self.touchangles + self.angle) * 10 + self.y
            self.touches[i] = board[int(y//scale), int(x//scale)]

        #noses
        x = math.cos(self.angle - 0.523) * 15 + self.x
        y = math.sin(self.angle - 0.523) * 15 + self.y
        self.noses[0] = board[int(y//scale), int(x//scale)]

        x = math.cos(self.angle + 0.523) * 15 + self.x
        y = math.sin(self.angle + 0.523) * 15 + self.y
        self.noses[1] = board[int(y//scale), int(x//scale)]

        #mouth
        x = math.cos(self.angle) * 15 + self.x
        y = math.sin(self.angle) * 15 + self.y
        self.mouth = board[int(y//scale), int(x//scale)]

    def updateBrain(self):
        #t1,t2,t3,t4,t5,t6, n1,n2, mouth, hunger

        self.z[0:6] = self.touches
        self.z[6:8] = self.noses
        self.z[9] = self.mouth
        self.z[10] = self.hunger

        self.z = funcs.activation(np.dot(self.z, self.weights))
    
    def draw(self, surface):
        self.x = int(self.x)
        self.y = int(self.y)
        
        #body
        pg.draw.circle(surface, (150,150,255), (self.x, self.y), 10)

        #touch
        for i in range(6):
            x = math.cos(i*self.touchangles + self.angle) * 10 + self.x
            y = math.sin(i*self.touchangles + self.angle) * 10 + self.y
            
            pg.draw.circle(surface, (0,0,255), (int(x),int(y)), 3)

        #noses
        x = math.cos(self.angle - 0.523) * 15 + self.x
        y = math.sin(self.angle - 0.523) * 15 + self.y
        pg.draw.circle(surface, (208, 217, 33), (int(x),int(y)), 5)

        x = math.cos(self.angle + 0.523) * 15 + self.x
        y = math.sin(self.angle + 0.523) * 15 + self.y
        pg.draw.circle(surface, (208, 217, 33), (int(x),int(y)), 5)

        #mouth
        x = math.cos(self.angle) * 15 + self.x
        y = math.sin(self.angle) * 15 + self.y
        pg.draw.circle(surface, (255,100,100), (int(x),int(y)), 4)
    

        