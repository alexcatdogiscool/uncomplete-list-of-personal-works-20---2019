import cv2
import math
import numpy as np


img = (((cv2.imread('img.png'))[:,:,0]))
print(img.shape)
img = img.reshape(10000)

num = ''

for i in range(10000):
    num = num.__add__(str(int(img[i]/255)))


num = int(num, 2)
print(num)