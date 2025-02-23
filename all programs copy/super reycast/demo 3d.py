import math

ha = 0
va = 0

a = (math.sin(ha))/(math.cos(ha))
b = (math.sin(va))/(math.cos(va))

sx = 0
sy = 5
sz = 0



w = sx
t = sz
q = sy

x = -(-2*q-2*w*a-2*t*b)/(2 * (1 + a**2 + b**2))

y = (1 + a**2 + b**2)*(-x)**2 - (-2*q-2*w*a-2*t*b)*(-x) + (q**2 + w**2 + t**2)

print(x, y)
