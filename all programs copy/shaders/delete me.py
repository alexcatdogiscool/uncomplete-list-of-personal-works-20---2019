import timeit

print("using +")
code_to_test = """

import math
import numpy as np

x = 0
y = 0
z = 0

xstep = 3.1
ystep = 4.9
zstep = 2.6

for epoch in range(40000):

    x += xstep
    y += ystep
    z += zstep
    
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
