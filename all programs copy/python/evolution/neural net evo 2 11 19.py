import math
import random
import numpy as np

random.seed(1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

class leaf:
    def __init__(self):
        self.width = int(random.uniform(1,10))
        self.height = int(random.uniform(1,10))
        if self.width < 1:
            self.width = 1
        
        if self.height < 1:
            self.height = 1
            
        self.perimeter = (2*self.width) + (2*self.height)
        self.area = self.width * self.height
        self.fitness = self.perimeter/self.area

population = []
children = []
best = []

for i in range(1000):
    i = leaf()
    population.append(i)


generation = 0

for epoch in range(1000):
    generation += 1
    #print(generation)

    population.sort(key=lambda x: x.fitness, reverse=True)

    #print("poop")

    for n in population:
        best.append(n)
        pass

    del best[-999:]
    for n in best:
        #print("when someone misses the toilet and there is a big pile of poop on the floor")
        #print(n.fitness)
        pass

    del population[-500:]

    #print("poopy")

    for n in population:
        #print(n.fitness)
        children.append(n)

    #print("poopy pants")

    for n in children:
        random.seed(n)
        n.width += random.uniform(0.02,-0.02)
        n.height += random.uniform(0.02,-0.02)
        if n.height < 1:
            n.height = 1

        if n.width < 1:
            n.width = 1
        n.fitness = ((2*n.width)+(2*n.height)) / (n.width*n.height)
        #print(n.fitness)
        population.append(n)

    children = []

    #print("poop face man")

population.sort(key=lambda x: x.fitness, reverse=True)

del population[-999:]

for n in population:
    print(n.width)
    print(n.height)
    print(n.fitness)
    pass



