import numpy as np
import pygame as py
import random


np.random.seed(1)
input_set = np.array([[1,1],[0,0],[1,0],[0,1],[1,1]])

cbest = 10
cworst = 0






def sigmoid(x):
    return 1/(1+np.exp(-x))


class net:
    def __init__(self, index, input_layers, output_layers, hidden_neurons1, hidden_neurons2, hidden_neurons3, learning_rate):
        #print("Index : %d", index)
        lr = learning_rate
        
        self.weights = np.random.rand(input_layers, hidden_neurons1)
        self.weights2 = np.random.rand(hidden_neurons1, hidden_neurons2)
        self.weights3 = np.random.rand(hidden_neurons2, hidden_neurons3)
        self.weights4 = np.random.rand(hidden_neurons3, output_layers)
        
        self.bias = np.random.rand(hidden_neurons1)
        self.bias2 = np.random.rand(hidden_neurons2)
        self.bias3 = np.random.rand(hidden_neurons3)
        self.bias4 = np.random.rand(output_layers)

        self.weights += random.uniform(-lr, lr)
        self.weights2 += random.uniform(-lr, lr)
        self.weights3 += random.uniform(-lr, lr)
        self.weights4 += random.uniform(-lr, lr)

        self.bias += random.uniform(-lr,lr)
        self.bias2 += random.uniform(-lr,lr)
        self.bias3 += random.uniform(-lr,lr)
        self.bias4 += random.uniform(-lr,lr)

        


    def fprop(self):
        z = np.dot(input_set, self.weights) + self.bias
        z = sigmoid(z)
        z2 = np.dot(z,self.weights2) + self.bias2
        z2 = sigmoid(z2)
        z3 = np.dot(z2,self.weights3) + self.bias3
        z3 = sigmoid(z3)
        z4 = np.dot(z3,self.weights4) + self.bias4

        n.error = ((input_set - z4)*(input_set - z4))/2

    def reproduce(self):
        pass



nets = []
for i in range(100):
    nets.append(net(i,2,1,3,3,2,2))


dead = 0

running = True
while running:
    for n in nets:
        n.fprop()
        if n.error.sum() < cbest:
            cbest = n.error.sum()
            print("current best ", cbest)

        if n.error.sum() > cworst:
            cworst = n.error.sum()
            print("current worst ", cworst)

    for n in nets:
        crange = cworst - cbest
        cmid = crange / 2
        if n.error.sum() > cmid:
            nets.remove(n)
            dead += 1
            print("killed ", dead)
            

    running = False





