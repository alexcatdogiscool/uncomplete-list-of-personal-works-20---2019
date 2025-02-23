import numpy as np
from PIL import Image
import pickle as pkl
import re

np.random.seed(69420)


def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative(x):
    return x * (1-x)


a = 0,0,0,0,0,0
b = 0,0,0,0,0,1
c = 0,0,0,0,1,0
d = 0,0,0,0,1,1
e = 0,0,0,1,0,0
f = 0,0,0,1,0,1
g = 0,0,0,1,1,0
h = 0,0,0,1,1,1
i = 0,0,1,0,0,0
j = 0,0,1,0,0,1
k = 0,0,1,0,1,0
l = 0,0,1,0,1,1
m = 0,0,1,1,0,0
n = 0,0,1,1,0,1
o = 0,0,1,1,1,0
p = 0,0,1,1,1,1
q = 0,1,0,0,0,0
r = 0,1,0,0,0,1
s = 0,1,0,0,1,0
t = 0,1,0,0,1,1
u = 0,1,0,1,0,0
v = 0,1,0,1,0,1
w = 0,1,0,1,1,0
x = 0,1,0,1,1,1
y = 0,1,1,0,0,0
z = 0,1,1,0,0,1
A = 0,1,1,0,1,0
B = 0,1,1,0,1,1
C = 0,1,1,1,0,0
D = 0,1,1,1,0,1
E = 0,1,1,1,1,0
F = 0,1,1,1,1,1
G = 1,0,0,0,0,0
H = 1,0,0,0,0,1
I = 1,0,0,0,1,0
J = 1,0,0,0,1,1
K = 1,0,0,1,0,0
L = 1,0,0,1,0,1
M = 1,0,0,1,1,0
N = 1,0,0,1,1,1
O = 1,0,1,0,0,0
P = 1,0,1,0,0,1
Q = 1,0,1,0,1,0
R = 1,0,1,0,1,1
S = 1,0,1,1,0,0
T = 1,0,1,1,0,1
U = 1,0,1,1,1,0
V = 1,0,1,1,1,1
W = 1,1,0,0,0,0
X = 1,1,0,0,0,1
Y = 1,1,0,0,1,0
Z = 1,1,0,0,1,1
ZERO = 1,1,0,1,0,0
ONE = 1,1,0,1,0,1
TWO = 1,1,0,1,1,0
THREE = 1,1,0,1,1,1
FOUR = 1,1,1,0,0,0
FIVE = 1,1,1,0,0,1
SIX = 1,1,1,0,1,0
SEVEN = 1,1,1,0,1,1
EIGHT = 1,1,1,1,0,0
NINE = 1,1,1,1,0,1
PLUS = 1,1,1,1,1,0
#'1,1,1,1,1,1



input_set = np.array([H,a,s,a,E,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a])
print(input_set)
input_set = input_set.reshape(1,180)
labels = np.array(input_set)
labels = labels.reshape(1,180)






def net(input_nodes, hidden_nodes, output_nodes):
    weights = np.random.rand(input_nodes, hidden_nodes)
    weights2 = np.random.rand(hidden_nodes, output_nodes)
    bias = np.random.rand(hidden_nodes)
    bias2 = np.random.rand(output_nodes)

    lr = 200.0

    itteration = 0
    count = 0
    error = np.array([100,100])

    running = True
    while (error.sum()) > 0.2:
        
        #forward prop

        z = np.dot(input_set, weights) + bias
        z = sigmoid(z)
        z2 = np.dot(z, weights2) + bias2
        z2 = sigmoid(z2)

        #back prop

        error = (labels - z2)*(labels - z2)

        bz = np.dot(z.T, (2*(labels - z2) * derivative(z2)))
        bz2 = np.dot(input_set.T, (np.dot(2*(labels - z2) * derivative(z2), weights2.T) * derivative(z)))
        weights += bz2
        weights2 += bz
    


        #image saving
        #outputimg = z2.reshape(64,64)
        #outputimg = (outputimg.astype(np.uint8))
        #outputimg = Image.fromarray(outputimg)
        #outputimg.save("smiley_output.png")

        itteration += 1
        count += 1
        if itteration == 10:
            print(count, error.sum())
            itteration = 0

            outputimg = z2.reshape(30,6)
            outputimg = outputimg * 255
            outputimg = (outputimg.astype(np.uint8))
            outputimg = Image.fromarray(outputimg)
            outputimg.save("smiley_output.png")

            

    weights2pkl = weights2
    biaspkl = bias2

    with open("weights2.pkl", "wb") as f:
        pkl.dump(weights2, f)

    with open("bias2.pkl", "wb") as f:
        pkl.dump(bias2, f)

    outputimg = z2.reshape(30,6)
    outputimg = outputimg * 255
    outputimg = (outputimg.astype(np.uint8))
    outputimg = Image.fromarray(outputimg)
    outputimg.save("smiley_output.png")
        
    return z2

    

ans = net(180,20,180)
print(ans)
