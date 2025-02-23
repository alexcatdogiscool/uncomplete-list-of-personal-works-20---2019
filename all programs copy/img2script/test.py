import numpy as np
from scipy.io import loadmat
import cv2

data = loadmat("emnist\\matlab\\emnist-letters.mat")['dataset']

input_set = data['train'][0,0]['images'][0,0]/255
labels = data['train'][0,0]['labels'][0,0].reshape(124800)

print(input_set.shape, labels[32])

cv2.imwrite('test.png', input_set[32,:].reshape(28,28).T*255)