import numpy as np



class test:
    def __init__(self,a):
        self.val = a

arr = np.zeros((2,2))
print(arr)
arr[:,:] = test(1)
print(arr)