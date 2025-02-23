import numpy as np
from random import randrange, uniform
np.random.seed(1)


input_set = np.array([[1,1],[0,0],[1,0],[0,1],[1,1]])
labels = np.array([[1,1],[0,0],[1,0],[0,1],[1,1]])
#labels = labels.reshape(5,5)



def sigmoid(x):
    return 1/(1+np.exp(-x))

def cross_entropy(predictions, targets, epsilon=1e-12):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce = -np.sum(targets*np.log(predictions+1e-9))/N
    return ce

targets = labels




def net(input_layers, output_layers, hidden_neurons1, hidden_neurons2, hidden_neurons3, error, learning_rate):
    weights = np.random.rand(input_layers, hidden_neurons1)
    weights2 = np.random.rand(hidden_neurons1, hidden_neurons2)
    weights3 = np.random.rand(hidden_neurons2, hidden_neurons3)
    weights4 = np.random.rand(hidden_neurons3, output_layers)
    bias = np.random.rand(hidden_neurons1)
    bias2 = np.random.rand(hidden_neurons2)
    bias3 = np.random.rand(hidden_neurons3)
    bias4 = np.random.rand(output_layers)

    lr = learning_rate

    currentlow = 10
    currentlow2 = 10

    clweights = np.random.rand(input_layers, hidden_neurons1)
    clweights2 = np.random.rand(hidden_neurons1, hidden_neurons2)
    clweights3 = np.random.rand(hidden_neurons2, hidden_neurons3)
    clweights4 = np.random.rand(hidden_neurons3, output_layers)
    clbias = np.random.rand(hidden_neurons1)
    clbias2 = np.random.rand(hidden_neurons2)
    clbias3 = np.random.rand(hidden_neurons3)
    clbias4 = np.random.rand(output_layers)

    cl2weights = np.random.rand(input_layers, hidden_neurons1)
    cl2weights2 = np.random.rand(hidden_neurons1, hidden_neurons2)
    cl2weights3 = np.random.rand(hidden_neurons2, hidden_neurons3)
    cl2weights4 = np.random.rand(hidden_neurons3, output_layers)
    cl2bias = np.random.rand(hidden_neurons1)
    cl2bias2 = np.random.rand(hidden_neurons2)
    cl2bias3 = np.random.rand(hidden_neurons3)
    cl2bias4 = np.random.rand(output_layers)
    
    mse = np.random.rand(3,3)
    count = 0
    one = 1000
    itteration = 0
    number = 0

    while mse.sum() > error:
        z = np.dot(input_set, weights) + bias
        z = sigmoid(z)
        z2 = np.dot(z, weights2) + bias2
        z2 = sigmoid(z2)
        z3 = np.dot(z2, weights3) + bias3
        z3 = sigmoid(z3)
        z4 = np.dot(z3, weights4) + bias4
        z4 = sigmoid(z4)

        #backprop
        mse = np.square(np.subtract(labels,z4)).mean()
#        mse = cross_entropy(z4, targets)
#        mse = z4 - labels

        if mse.sum() < currentlow2:
            currentlow2 = mse.sum()
            cl2weights = weights
            cl2weights2 = weights2
            cl2weights3 = weights3
            cl2weights4 = weights4
            
            cl2bias = bias
            cl2bias2 = bias2
            cl2bias3 = bias3
            cl2bias4 = bias4

        if count == 1:
            clweights = cl2weights
            clweights2 = cl2weights2
            clweights3 = cl2weights3
            clweights4 = cl2weights4

            clbias = cl2bias
            clbias2 = cl2bias2
            clbias3 = cl2bias3
            clbias4 = cl2bias4

            count = 0

        weights = clweights + uniform(-lr,lr)
        weights2 = clweights2 + uniform(-lr,lr)
        weights3 = clweights3 + uniform(-lr,lr)
        weights4 = clweights4 + uniform(-lr,lr)

        bias = clbias + uniform(-lr,lr)
        bias2 = clbias2 + uniform(-lr,lr)
        bias3 = clbias3 + uniform(-lr,lr)
        bias4 = clbias4 + uniform(-lr,lr)
#        print(mse)

        if number == 1:
            print(itteration)
            print(mse)
            number = 0
            
        itteration += 1
        count += 1
        one += 1
        number += 1

    return z4




ans = net(2, 2, 3, 3, 3, 0.103, 0.02)
print(ans)






