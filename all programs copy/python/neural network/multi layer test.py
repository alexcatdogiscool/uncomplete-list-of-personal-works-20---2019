import numpy as np

input_set = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
labels = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
labels = labels.reshape(5,3)

np.random.seed(1)
weights = np.random.rand(3, 2)
weights2 = np.random.rand(2,3)
bias = np.random.rand(2)
bias2 = np.random.rand(3)
lr = 0.002

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1-sigmoid(x))

def arrsum(arr, n):
    return(sum(arr))

for epoch in range(10000):
    inputs = input_set

    z = np.dot(input_set, weights) + bias
    z = sigmoid(z)
#    print(z)

    z2 = np.dot(z, weights2) + bias2
    z2 = sigmoid(z2)
#    print(z2)

    #backprop
    error = z2 - labels

    dcost_dpred = error
    dpred_dz2 = sigmoid_der(z2)

    z2_delta = dcost_dpred * dpred_dz2

#    print(weights)
    weights = np.split(weights,2,1)
    weights2 = np.split(weights2,2,0)
#    print(weights)

    inputs = input_set.T
    weights -= lr * np.dot(labels.T, z2_delta)
    weights = weights.reshape(3,3,2)
    
    weights = arrsum(weights, 18)/9
    

    weights2 -= lr * np.dot(labels.T, z2_delta)
    weights2 = weights2.reshape(3,3,2)
    weights2 = arrsum(weights2, 18)/9
    weights2 = weights2.reshape(2,3)
    

#    bias = np.split(bias,2,0)
    for num in z2_delta:
        bias2 -= lr*num
#        bias -= lr*num
#    bias = bias.reshape(3,2)
#    bias = arrsum(bias,6)/6




print(z2)
print(weights)
print(weights2)
print(bias)
print(bias2)
print(error)






    

