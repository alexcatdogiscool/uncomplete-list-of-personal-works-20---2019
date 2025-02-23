import math
import random
import numpy as np

random.seed(1)

class leaf:
    def __init__(self):
        self.width = int(random.uniform(1,10))
        self.height = int(random.uniform(1,10))
        if self.width < 0.5:
            self.width = 0.5

        if self.height < 0.5:
            self.height = 0.5
        self.perimeter = (2*self.width) + (2*self.height)
        self.area = self.width * self.height
        self.fitness = self.perimeter/self.area


population = []

for i in range(100):
    i = leaf()
    population.append(i)
    #print(i.fitness)

for population in range(100):
        print(i.fitness)

print("sorted")


for epoch in range(100):
    population.sort(key=lambda x: x.fitness, reverse=True)

    for population in range(100):
        print(i.fitness)

    del population[-50:]

    

    children = population
    #print(population)

    for population in range(50):
        #print(i.fitness)
        i.width += random.uniform(-1,1)
        i.height += random.uniform(-1,1)
        

    population.append(children)
    #print(population.count)
    


#best = population
#del best[-99:]
#for best in range(1):
#    print(i.fitness)
    








