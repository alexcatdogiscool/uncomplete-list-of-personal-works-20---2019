import numpy as np

feature_set = np.array([[0],[1],[1],[0],[1]])
labels = np.array([1,0,0,1,0])
labels = labels.reshape(5,1)

np.random.seed(42)
weights = np.random.rand(1)
print("random weights:", weights)
bias = np.random.rand(1)
lr = 0.05

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

for epoch in range(10):
    inputs = feature_set

    # feedforward step1
    XW = np.dot(feature_set, weights) + bias
    #print("weights")
    #print(bias)

    #feedforward step2
    z = sigmoid(XW)

    #print('z:')
    #print(z)


    # backpropagation step 1
    error = z - labels

    print(error.sum())

    # backpropagation step 2
    dcost_dpred = error
    dpred_dz = sigmoid_der(z)

    z_delta = dcost_dpred * dpred_dz
    #print("start")
    #print(z_delta)

    inputs = feature_set.T
    z_delta = z_delta.reshape(5,5)
    thing = lr * np.dot(inputs, z_delta)
    #print("inputs")
    #print(weights)
    #print(z_delta)
    weights = thing
    
    
    
    #print("thing2")

    for num in z_delta:
        1+2
#        bias -= lr * num
    #print(z_delta)
    

#    print(weights)
#    print(bias)
#    print(z)


