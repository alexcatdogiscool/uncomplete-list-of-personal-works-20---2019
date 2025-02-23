import math
import cv2
import numpy as np

b = complex(2,2)

def explode(z):
    a = z
    for n in range(100):
        a = z**a
        if abs(a.real) > 120 or abs(a.imag) > 120:
            return 0#True
    return 255#False

w = 5
center = (-0.5,0)
o = (-w/2+center[0],-w/2+center[1])
print(o)
wp = 10000

gap = (w/wp)

img = []

for v in range(wp):
    for h in range(wp):
        b = complex(o[0]+ (gap*h) , o[1] + (gap*v))
        colour = explode(b)
        img.append(colour)


img = np.array(img)
img = img.reshape(wp,wp)
cv2.imwrite('set.png', img)