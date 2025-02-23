import math
import cv2
import numpy as np
import random



class ray:
    def __init__(self):
        self.a = 0

        self.r = 0
        self.g = 0
        self.b = 0

        self.hit = False


class circle:
    def __init__(self):
        self.rad = 2

        self.x = random.uniform(2,200)
        self.y = random.uniform(2,100)

        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)






raysize = 100


step = (math.pi/2)/raysize

count = -math.pi/4
rays = []
for r in range(raysize):
    r = ray()
    r.a = (math.sin(count))/(math.cos(count))
    count += step
    rays.append(r)

print(step)
print("")









circs = []
circsize = 10
for c in range(circsize):
    c = circle()
    circs.append(c)

count = 0
for r in rays:
    for c in circs:
        h = c.x
        v = c.y
        a = r.a
        
        x = -((((2*h)+(2*a*v))*-1)/(2*(a**2+1)))
        y = math.sqrt((h**2) - (2*h*x) + (x**2) + (v**2) - (2*a*x*v) + (a**2) * (x**2))

        if r.hit == True:
            y = 100

        if y < c.rad:
            r.r += c.r
            r.g += c.g
            r.b += c.b
            count += 1
print(count)


img = []

for r in rays:
    img.append(r.r)
    img.append(r.g)
    img.append(r.b)
    img.append(r.r)
    img.append(r.g)
    img.append(r.b)
    img.append(r.r)
    img.append(r.g)
    img.append(r.b)
    img.append(r.r)
    img.append(r.g)
    img.append(r.b)
    img.append(r.r)
    img.append(r.g)
    img.append(r.b)
    print(r.a)

img = np.array(img)
img = img.reshape(raysize, 5, 3)

cv2.imwrite('imgs//img.png', img)
#print(img)




















