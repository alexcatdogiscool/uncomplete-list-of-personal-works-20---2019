import numpy as np
from random import randrange, uniform
np.random.seed(1)


input_set = np.array([[1,1],[0,0],[1,0],[0,1],[1,1]])
labels = np.array([[0.75,0.75],[0.801,0.852],[0.653,0.904],[0.752,0.853],[0.654,0.875]])
#labels = labels.reshape(5,5)

print(labels.ndim)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

def cross_entropy(predictions, targets, epsilon=1e-12):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce = -np.sum(targets*np.log(predictions+1e-9))/N
    return ce

def derivative(output):
    return output * (1-output)

targets = labels




def net(input_layers, output_layers, hidden_neurons1, hidden_neurons2, hidden_neurons3, error, learning_rate):
    weights = np.random.rand(input_layers, hidden_neurons1)
    weights2 = np.random.rand(hidden_neurons1, hidden_neurons2)
    weights3 = np.random.rand(hidden_neurons2, hidden_neurons3)
    weights4 = np.random.rand(hidden_neurons3, output_layers)

    bpweights = np.random.rand(hidden_neurons1, input_layers)
    bpweights2 = np.random.rand(hidden_neurons2, hidden_neurons1)
    bpweights3 = np.random.rand(hidden_neurons3, hidden_neurons2)
    bpweights4 = np.random.rand(output_layers, hidden_neurons3)
    
    bias = np.random.rand(hidden_neurons1)
    bias2 = np.random.rand(hidden_neurons2)
    bias3 = np.random.rand(hidden_neurons3)
    bias4 = np.random.rand(output_layers)
    bias, bias2, bias3, bias4 = 0, 0, 0, 0

    lr = learning_rate

    
    mse = np.random.rand(3,3)
    count = 0
    one = 1000
    itteration = 0
    number = 0
    berror = np.random.rand(2,2)

    #while berror.sum() > error:
    for epoch in range(1):
        #print("itt")
        z = np.dot(input_set, weights) + bias
        z = sigmoid(z)
        z2 = np.dot(z, weights2) + bias2
        z2 = sigmoid(z2)
        z3 = np.dot(z2, weights3) + bias3
        z3 = sigmoid(z3)
        z4 = np.dot(z3, weights4) + bias4
        z4 = sigmoid(z4)

        #backprop


        inputs = input_set


        mse = labels - z4
        #mse = ((labels - z4)*(labels - z4))/2
        #mse = derivative(mse)
        berror = mse
        
        
        

        bz = np.dot(berror, weights4.T)
        bz2 = np.dot(bz, weights3.T)
        bz3 = np.dot(bz2, weights2.T)
        bz4 = np.dot(bz3, weights.T)
        
        

       
        weights += lr * (np.dot(bz4.T, z))
        weights2 += lr * (np.dot(bz3.T, z2))
        weights3 += lr *(np.dot(bz2.T, z3))
        weights4 += lr * (np.dot(bz.T, z4))
        
        w = lr * (np.dot(bz4.T, z))
        w2 = lr * (np.dot(bz3.T, z2))
        w3 = lr *(np.dot(bz2.T, z3))
        w4 = lr * (np.dot(bz.T, z4))


        

        if itteration == 1000:
            print(berror.sum())
            itteration = 0

            
        itteration += 1
        count += 1
        one += 1
        number += 1

    #return z4
    #return berror.sum()
    #print(berror)
    



ans = net(2, 2, 3, 3, 3, 0.01, 0.01)
print(ans)






