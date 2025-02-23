import numpy as np

feature_set = np.array([[0,1,0],[0,0,1],[1,0,0],[1,1,0],[1,1,1]])
labels = np.array([1,0,0,1,1])
labels = labels.reshape(5,1)

np.random.seed(42)
weights = np.random.rand(3,1)
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

    #feedforward step2
    z = sigmoid(XW)


    # backpropagation step 1
    error = z - labels

    print(error.sum())

    # backpropagation step 2
    dcost_dpred = error
    dpred_dz = sigmoid_der(z)

    z_delta = dcost_dpred * dpred_dz

    print('poo')
    print(inputs)
    print(z_delta)
    print(weights)
    print("end")

    inputs = feature_set.T
    weights -= lr * np.dot(inputs, z_delta)
    thing = (lr * np.dot(inputs, z_delta))
    

    print(thing)
    print("end")

    for num in z_delta:
        bias -= lr * num
    print("num")
    print(z_delta)
    print("num")

#    print(weights)
#    print(bias)
    print(z)


