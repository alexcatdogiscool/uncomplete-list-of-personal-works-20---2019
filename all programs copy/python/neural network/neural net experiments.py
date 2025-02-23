import numpy as np

input_set = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[0,0,0],[0.5,0.5,0.5],[0.25,0.25,0.25],[0.75,0.75,0.75]])
labels = np.array([1,0,1,0,1,1,1,0])
labels = labels.reshape(8,1)

np.random.seed(1)
weights1 = np.random.rand(3,1)
weights2 = np.random.rand(3,1)
weights3 = np.random.rand(3,1)
bias1 = np.random.rand(1)
bias2 = np.random.rand(1)
bias3 = np.random.rand(1)

weights21 = np.random.rand(3,1)
bias21 = np.random.rand(1)

lr = 0.05

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1-sigmoid(x))

for epoch in range(100000):
    inputs = input_set

    WX1 = np.dot(input_set, weights1) + bias1

    z1 = sigmoid(WX1)

    WX2 = np.dot(input_set, weights2) + bias2

    z2 = sigmoid(WX2)

    WX3 = np.dot(input_set, weights3) + bias3

    z3 = sigmoid(WX3)


    z1 = z1.reshape(1,8)
    z2 = z2.reshape(1,8)
    z3 = z3.reshape(1,8)
    input_set2 = np.array([[z1],[z2],[z3]])
    input_set2 = input_set2.reshape(8,3)

    
    #layer 2
    WX21 = np.dot(input_set2, weights21) + bias21

    z21 = sigmoid(WX1)

    #back prop
    error = z21 - labels

    

    dcost_dpred1 = error
    dpred_dz1 = sigmoid_der(z21)

    dcost_dpred2 = error
    dpred_dz2 = sigmoid_der(z21)

    dcost_dpred3 = error
    dpred_dz3 = sigmoid_der(z21)

    z_delta1 = dcost_dpred1 * dpred_dz1
    z_delta2 = dcost_dpred2 * dpred_dz2
    Z_delta3 = dcost_dpred3 * dpred_dz3


    inputs = input_set.T
    weights1 -= lr * np.dot(inputs, z_delta1)
    weights2 -= lr * np.dot(inputs, z_delta2)
    weights3 -= lr * np.dot(inputs, z_delta2)

    for num in z_delta1:
        bias1 -= lr*num

    for num in z_delta2:
        bias2 -= lr*num

    for num in z_delta2:
        bias2 -= lr*num

    dcost_dpred21 = error
    dpred_dz21 = sigmoid_der(z21)

    z_delta21 = dcost_dpred21 * dpred_dz21

    inputs2 = input_set2.T
    weights21 -= lr * np.dot(inputs2, z_delta21)

    for num in z_delta21:
        bias21 -= lr*num




print("error")
print(error.sum())
print("z21")
print(z21)
print(" ")
print("thought process")
print(weights1)
print(weights2)
print(weights3)
print("bias")
print(bias1)
print(bias2)
print(bias3)
print("Second layer")
print(weights21)
print(bias21)

    

