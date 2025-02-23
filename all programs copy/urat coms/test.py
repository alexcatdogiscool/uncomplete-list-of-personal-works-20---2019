import numpy as np
from scipy.io.wavfile import write
import math
import matplotlib.pyplot as plt
import random

data = np.load('data.npy')
#data = np.array([0,1,0,1,0,1])

size = np.size(data)

baud = 5000

one = []
zero = []

out = []

f1 = 5/ 4
f0 = 10 / 4

res = 100

baud = (baud*res)

for i in range(res):
    one.append((math.sin((i/math.pi)/f1))*1000)

for i in range(res):
    zero.append((math.sin((i/math.pi)/f0))*1000)
    

#################################################


for i in range(size):
    if data[i] == 0:
        for o in range(res):
            out.append(zero[o])

    if data[i] == 1:
        for o in range(res):
            out.append(one[o])

out = np.asarray(out, dtype=np.int16)
write('out.wav', baud, out)
