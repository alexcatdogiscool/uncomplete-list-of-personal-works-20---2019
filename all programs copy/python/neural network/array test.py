import numpy as np
np.random.seed(1)
z = np.random.rand(5,2)
labels = np.random.rand(5,2)
weights = np.random.rand(2,3)
weights2 = np.random.rand(3,3)
weights3 = np.random.rand(3,3)
weights4 = np.random.rand(3,2)

def arrsum(arr, n):
    return(sum(arr))

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

error = z - labels
print(error.sum())

weights -= np.dot(
