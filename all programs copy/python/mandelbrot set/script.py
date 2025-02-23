import numpy as np
from PIL import Image
from numba import jit
import math

def fact(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact

print(fact(5))
        
@jit
def mandelbrot(c,maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = (1*((z**3)-z)) + c
    return 0

@jit
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],maxiter)
    return (n3)

man = mandelbrot_set(-1.25, 1.25, -1.25, 1.25, 20000, 20000, 80)
#print(man)

img = man
arr = np.array(list(img), dtype=int)
arr = arr.reshape(20000,20000)

arr = arr *10
arr = (arr.astype(np.uint8))
arr = Image.fromarray(arr)
arr.save("fract.png")




