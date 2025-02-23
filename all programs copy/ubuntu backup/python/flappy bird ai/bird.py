import math
import numpy as np

def sigmoid(x):
    return 1/(1+np.e**(-x))




class bird:
    def __init__(self):
        self.x, self.y = 250,400
        self.v = 0

        self.score = 0
        self.fitness = 0

        self.alive = True


        #### inputs; self.velocity, height, dist to wall, height of bottom of wall (4)
        #### outputs; jump this frame, dont jump this frame (2)
        self.weights1 = np.random.rand(4,5)
        self.weights2 = np.random.rand(5,2)
        
        self.bias1 = np.random.rand(5)
        self.bias2 = np.random.rand(2)

    def think(self, wallDst, wallHeight):
        inputs = np.array([self.v/10, self.y/800, wallDst, wallHeight])
        inputs = inputs.reshape(4)
        z1 = sigmoid(np.dot(inputs, self.weights1)+self.bias1)
        z2 = sigmoid(np.dot(z1, self.weights2)+self.bias2)

        if z2[0] > z2[1]:
            self.v = -5

    def phys(self, g):
        if self.alive == True:
            self.v += g
            self.y += self.v
            self.fitness += 0.5
        if self.alive == False:
            self.x -= 0.5