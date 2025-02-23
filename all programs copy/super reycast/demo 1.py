import numpy as np
import math

a = 0.91
h = 5
v = 3

x = -((((2*h)+(2*a*v))*-1)/(2*(a**2+1)))
y = math.sqrt((h**2) - (2*h*x) + (x**2) + (v**2) - (2*a*x*v) + (a**2) * (x**2))

print(x)
print(y)
