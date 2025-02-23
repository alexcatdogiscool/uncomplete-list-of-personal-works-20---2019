import numpy as np

weights1 = np.array([[0.31331673],[-10.80298386],[0.25936903]])
weights2 = np.array([[-0.26825533],[10.78488105],[-0.29924146]])
bias1 = np.array([7.20013726])
bias2 = np.array([-7.40871297])

#r,g,b values below
r = 255
g = 255
b = 255

rr = r/104
rg = g/105
rb = b/171

input_set = np.array([[rr],[rg],[rb]])




def sigmoid(x):
    return 1/(1+np.exp(-x))


inputs = input_set

inputs = inputs.reshape(1,3)

#feedforward
XWout1 = np.dot(inputs, weights1) + bias1

z1 = sigmoid(XWout1)

XWout2 = np.dot(inputs, weights2) + bias2

z2 = sigmoid(XWout2)

#print(z2)

if XWout1 > 0.5:
    print("text of this color would go good over white")
    print(z1*100)
else:
    print("text of this color would go good over black")
    print(100-(z1*100))
