import math
import random
import numpy as np
from random import randint

random.seed(3)


xpos = random.uniform(0,10)
ypos = random.uniform(0,10)

xvel = random.uniform(-1,1)
yvel = random.uniform(-1,1)

flist = []

for epoch in range(10000):
    xpos += xvel
    ypos += yvel

    if xpos > 10:
        xvel = xvel*-1

    if xpos < 0:
        xvel = xvel*-1

    if ypos > 10:
        yvel = yvel*-1

    if ypos < 0:
        yvel = yvel*-1

    flist.append(xpos)
    flist.append(ypos)

input_setlist = flist
del input_setlist[-5000:]
labelslist = flist
del labelslist[5000:]

input_set = np.asarray(input_setlist, dtype=np.float32)
labels = np.asarray(labelslist, dtype=np.float32)

input_set = input_set.reshape(100,50)
labels = labels.reshape(100,50)

print(input_set)

#################################################################################

def sigmoid(x):
    return 1/(1+np.exp(-x))



class leaf:
    def __init__(self):
        self.weights = np.random.rand(50,50)
        self.weights2 = np.random.rand(50,50)

        self.bias = np.random.rand(50)
        self.bias2 = np.random.rand(50)

        self.z = np.dot(input_set, self.weights)+self.bias
        self.z = sigmoid(self.z)

        self.z2 = np.dot(self.z, self.weights2)
        self.z2 = (sigmoid(self.z2))*10
        self.error = (labels - self.z2)**2
        self.fitness = self.error.sum()

population = []
children = []
best = []

for i in range(1000):
    i = leaf()
    population.append(i)


generation = 0
count = 0

for epoch in range(50):
    generation += 1
    count += 1
    

    population.sort(key=lambda x: x.fitness, reverse=True)

    #print("poop")



    del population[-500:]

    #print("poopy")

    for n in population:
        #print(n.fitness)
        children.append(n)

    #print("poopy pants")

    for n in children:
        random.seed(n)
        n.weights = n.weights+random.uniform(0,1)
        n.weights[randint(0,49), randint(0,49)] *= random.uniform(0.9,1.1)

        
        n.weights2[randint(0,49), randint(0,49)] *= random.uniform(0.9,1.1)



        n.z = np.dot(input_set, n.weights)+n.bias
        n.z = sigmoid(n.z)
        n.z2 = np.dot(n.z, n.weights2)
        n.z2 = (sigmoid(n.z2))*10
        n.error = (labels - n.z2)**2
        
        n.fitness = n.error.sum()
        #print(n.fitness)


        population.append(n)

    

    population.sort(key=lambda x: x.fitness, reverse=True)

    for n in population:
        best.append(n)

    del best[-999:]

    for n in best:
        #print(n.fitness)
        pass


    children = []

    #print("poop face man")


    if count == 1000:
        for n in best:
            #print(generation, n.fitness)
            pass

        count = 0




    best = []

del population[-999:]

for n in population:
    print(n.fitness)

