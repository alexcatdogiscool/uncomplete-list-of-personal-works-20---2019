import numpy as np

input_set = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[0,0,0],[0.5,0.5,0.5]])
labels1 = np.array([1,0,1,0,1,1])
labels2 = np.array([0,1,0,1,0,0])
print(labels1)
labels1 = labels1.reshape(6,1)
labels2 = labels2.reshape(6,1)

np.random.seed(1)
weights1 = np.random.rand(3,1)
weights2 = np.random.rand(3,1)
bias1 = np.random.rand(1)
bias2 = np.random.rand(1)
lr = 0.05

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1-sigmoid(x))

for epoch in range(3):
    inputs = input_set

    #feedforward
    XW1 = np.dot(input_set, weights1) + bias1

    z1 = sigmoid(XW1)

    XW2 = np.dot(input_set, weights2) + bias2

    z2 = sigmoid(XW2)

#    print(z1)
 #   print(z2)

    #backprop
    error1 = z1 - labels1
    error2 = z2 - labels2

    print(error1.sum())
    print(error2.sum())

    dcost1_dpred1 = error1
    dpred1_dz1 = sigmoid_der(z1)
    dcost2_dpred2 = error2
    dpred2_dz2 = sigmoid_der(z2)

    z1_delta = dcost1_dpred1 * dpred1_dz1
    z2_delta = dcost2_dpred2 * dpred2_dz2


    inputs = input_set.T
    weights1 -= lr * np.dot(inputs, z1_delta)
    weights2 -= lr * np.dot(inputs, z2_delta)

    for num in z1_delta:
        bias1 -= lr*num

    for num in z2_delta:
        bias2 -= lr*num

print(z1)
print(z2)

r = 0.141
g = 0.541
b = 0.2

color = np.array([r,g,b])

XWout1 = np.dot(color, weights1) + bias1

z1 = sigmoid(XW1)

XWout2 = np.dot(color, weights2) + bias2

z2 = sigmoid(XW2)


if XWout1 > 0.5:
    print("text of this color would go good over white")
else:
    print("text of this color would go good over black")

print(weights1)
print(weights2)
print(bias1)
print(bias2)
