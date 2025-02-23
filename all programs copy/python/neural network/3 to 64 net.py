import numpy as np
import pickle as pkl
from PIL import Image


def sigmoid(x):
    return 1/(1+np.exp(-x))


with open('weights2.pkl', 'rb') as f:
    weights = pkl.load(f)

with open('bias2.pkl', 'rb') as f:
    bias = pkl.load(f)


input_set = np.array([ [1,0],[0,1],[0,0],[1,1] ])


z = np.dot(input_set, weights) + bias
z2 = sigmoid(z)


outputimg = z2.reshape(32,8)
outputimg = outputimg * 255
outputimg = (outputimg.astype(np.uint8))
outputimg = Image.fromarray(outputimg)
outputimg.save("smiley_output.png")


print(z.shape)

