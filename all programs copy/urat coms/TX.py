import math
import numpy as np
import cv2

img = cv2.imread('send\\send5.png')
shape = img.shape[:2]
img = img.reshape(shape[0]*shape[1]*3)

print(shape)

info = img

infobin = []
pos = 0

infobin.append(0)
pos += 1
for i in range(2):
    byte = list(map(int, ('{0:08b}'.format(int(shape[i]/10)))))
    for o in range(8):
        infobin.append(byte[o])
        pos += 1
#infobin.append(0)
#pos += 1

for i in range(info.size):
    byte = list(map(int, ('{0:08b}'.format(info[i]))))
    #infobin[pos] = 0
    infobin.append(0)
    pos += 1
    #infobin
    for o in range(8):
        infobin.append(int(byte[o]))
        pos += 1
infobin.append(1)
pos += 1

infobin = np.asarray(infobin)
print(infobin)
print(pos)

np.save('data.npy', infobin)
