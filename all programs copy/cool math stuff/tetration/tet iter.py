import math

e = math.e
a = 1
b = ((e**-1)**(1/(e**-1)))

for n in range(1000):
    print(a)
    a = b**a
print("")
print("b =", b)
