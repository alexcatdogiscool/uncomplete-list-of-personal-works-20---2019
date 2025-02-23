import math

def rad(x):
    return x * math.pi/180



lstep = 10

a1 = rad(45)
a2 = rad(45)

zstep = lstep * math.sin(a1)

xystep = (lstep**2 - zstep **2)**0.5

xstep = xystep * math.cos(a2)

ystep = (xystep**2 - xstep**2)**0.5

print(xstep, ystep, zstep)
print(xystep)
