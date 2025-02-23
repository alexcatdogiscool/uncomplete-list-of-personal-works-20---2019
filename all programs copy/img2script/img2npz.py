import cv2
import os
import numpy as np


path = '\\Users\\alex\\Desktop\\img2script\\induvidual'
files = os.listdir(path)
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.png'])))
"""
input_set = np.zeros((1400,784))
labels = np.zeros((1400,14))

for k in range(14):
    print(chr(97+k))
    for i in range(100):
        img = cv2.imread(path+"\\{}\\{}.png".format(chr(97+k), i), cv2.IMREAD_GRAYSCALE)
        img = img.reshape(784)
        input_set[i+100*k,:] = img
        labels[i+100*k,k] = 1

np.savez_compressed("a-k.npz", a=input_set, b=labels)
"""