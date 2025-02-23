import matplotlib.pyplot as plt
import random
import math

x = []
y = []

N = 10000
for i in range(N):
    c = random.uniform(0,1)
    b = random.uniform(-c,c)
    a = math.sqrt(c**2 - b**2)
    x.append(b)
    y.append(a)

x.append(0)
y.append(-1)
plt.scatter(x, y)
plt.show()