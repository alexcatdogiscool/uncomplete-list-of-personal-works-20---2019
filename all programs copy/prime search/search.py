import math
import numpy as np
import time


def findPrimes(n):
    start = time.time()
    arr = np.ones(n**2)
    for a in range(2,int(n/2)):
        for b in range(2,int(n/2)):
            if b > a:
                break
            arr[a*b] = 0
    end = time.time()

    return int(arr[:n].sum())-2, end-start



print(findPrimes(int(input("max number to search to: "))))





input("press close to exit")
