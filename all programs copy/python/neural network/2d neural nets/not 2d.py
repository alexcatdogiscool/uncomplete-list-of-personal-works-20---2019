import numpy as np
import random
from PIL import Image

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative(x):
    return sigmoid(x)*(1-sigmoid(x))




def net(input_nodes, output_nodes, learning_rate):
    weights = np.random.rand(input_nodes, output_nodes)
    bias = np.random.rand(output_nodes)
    lr = learning_rate



    number = 0
    running = True
    for epoch in range(1000):
        #fprop
        z = np.dot(input_set, weights) + bias
        z = sigmoid(z)

        

        #bprop
        error = (z - labels)

        dcost_dpred = error
        dpred_dz = derivative(z)

        z_delta = dcost_dpred * dpred_dz

        inputs = input_set.T
        weights += lr * np.dot(inputs, z_delta)
        #print(error.sum())

        for num in z_delta:
            bias += lr * num
        

        z = z.reshape(5,5)
        z = z*255
        imgout = (np.array(z).astype(np.uint8))
        imgout = Image.fromarray(imgout)
        imgout.save("poopy.png")

        if number == 0:
            print(z)
        number += 1

    print(z)
    



img = Image.open('cat.png').convert('LA')
img.save("hfbhefkefbke.png")
img = np.array(img)
#print(img)
img = img.reshape(2,64,64)
img = img[0,:,:]
print("ans")
print(img)
print("ans")
#imgout = (np.array(img).astype(np.uint8))
imgout = Image.fromarray(img)
print(imgout)
imgout.save("poops.png")

img = img.reshape(1,4096)
print(img.shape)
input_set = img
labels = img



ans = net(4096,4092,0.02)


