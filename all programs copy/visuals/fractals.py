import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import cv2

# co ords   (-2,1), (1,-1) #
width = 400
height = int((width*2)/3)
res = width*height
print(height)
depth = 7
frames = 1

zoom = 1

box = -2/zoom,-1/zoom, 1/zoom,1/zoom

x = box[0]
y = box[1]

xstep = abs(box[0] - box[2])/width
ystep = abs(box[1] - box[3])/height

img = np.zeros((width, height,frames))

for f in range(frames):
    zoom = 1/0.005
    cx = -0.7436
    cy = 0.1102
    box = (cx-1.5),(cy-1), (cx+1.5)/zoom,(cy+1)/zoom

    
    xstep = abs(box[0] - box[2])/width
    ystep = abs(box[1] - box[3])/height


    print(f)
    depth = f+20
    x, y = box[0], box[1]

    for w in range(width):
        for h in range(height):

            z = 0
            c = complex(x,y)
            for i in range(depth):
                z = z**2 + c
                if abs(z) > (x+y)+10:
                    img[w,h,f] = 255
                    break
            y += ystep
        x += xstep
        y = box[1]
    



for i in range(frames):
    cv2.imwrite('fractal file\\{0}.png'.format(i), img[:,:,i])



imgplot = plt.imshow(img[:,:,0])
plt.show()
