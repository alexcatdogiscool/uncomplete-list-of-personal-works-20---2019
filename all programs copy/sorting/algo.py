import numpy as np
import math


n = 3
l = 4

arr = np.random.randint(0,n,l)

temp = np.zeros(n*l) - 1

mi = np.min(arr)
ma = np.max(arr)

print(arr)

temp[0] = mi
temp[-1] = ma

posMin = 0
posMax = (n*l)-1
mult = n

for i in range(l):
    if arr[i] > temp[posMin] and arr[i] < temp[posMax]:
        temp[(posMin+posMax)//2] = arr[i]
