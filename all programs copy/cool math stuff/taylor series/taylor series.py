import math
import matplotlib.pyplot as plt

def func(x):
    return (3*5)/(1+ 5**(-x) + 5**x)

def deriv(f, x, depth, res):
    if depth == 0:
        return(f(x))

    def ft(x):
        return (f(x+res)-f(x))/res
    if depth > 1:
        return deriv(ft,x,depth-1,res)
    if depth == 1:
        return(ft(x))


def taylor(f,x,terms,res):
    c = []
    for i in range(terms):
        c.append(deriv(f,x,i,res)/math.factorial(i))
    return c

def aprox(x,lst):
    val = 0
    for i in range(len(lst)):
        val += lst[i]*x**i
    return val
    

c = taylor(func,0,5,0.01)
pos = 0
print("Aprox  = ", end="")
print(aprox(pos,c))
print("Actual = ", end="")
print(func(pos))

start = -4
end = 4
ppu = 10
totaldst = abs(start)+abs(end)
totalpoints = ppu * totaldst
dx = totaldst/totalpoints

valsa = []
valsv = []
xax = []
for i in range(totalpoints):
    xax.append(i*dx+start)
    va = aprox((i*dx)+start,c)
    vv = func((i*dx)+start)
    if va > 10:
        va = 10
    if vv > 10:
        vv = 10
    if va < -10:
        va = -10
    if vv < -10:
        vv = -10
    valsa.append(va)
    valsv.append(vv)
plt.plot(xax,valsa)
plt.plot(xax,valsv)
plt.show()
