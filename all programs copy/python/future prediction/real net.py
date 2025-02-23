import numpy as np
import math
import random
np.random.seed(1)
random.seed(1)

input_set = np.load('input.npy')
labels = np.load('output.npy')

#input_set = np.array([[1,0,0,0],[1,0,1,0],[0,0,1,0],[0,1,1,0]])
#labels = np.array([[1,0],[1,0],[0,0],[0,1]])


def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
	
    return 1/(1+np.exp(-x))

lr = 0.022

innodes = 36
hidnodes = 20
hidnodes2 = 10
outnodes = 2

weights = np.random.rand(innodes, hidnodes)
weights2 = np.random.rand(hidnodes, hidnodes2)
weights3 = np.random.rand(hidnodes2, outnodes)

bias = np.random.rand(hidnodes)
bias2 = np.random.rand(hidnodes2)
bias3 = np.random.rand(outnodes)

count = 0
iteration = 0
z3error = np.array([10])
pre = 0
while abs(z3error.sum()) > 0.001:
    count += 1
    iteration += 1

    z = nonlin(np.dot(input_set, weights) + bias)
    z2 = nonlin(np.dot(z, weights2) + bias2)
    z3 = nonlin(np.dot(z2, weights3) + bias3)
    

    z3error = (labels - z3)
    z3delta = z3error*nonlin(z3,deriv=True)

    z2error = z3delta.dot(weights3.T)
    z2delta = z2error*nonlin(z2,deriv=True)
    
    zerror = z2delta.dot(weights2.T)
    zdelta = zerror*nonlin(z,deriv=True)
    
    weights3 += z2.T.dot(z3delta) * lr
    weights2 += z.T.dot(z2delta) * lr
    weights += input_set.T.dot(zdelta) * lr

    dif = pre - z3error.sum()

    if count == 1000:
        print(iteration, z3error.sum(), dif)
        count = 0

    pre = z3error.sum()

    
print(z3, z3error.sum())


    


