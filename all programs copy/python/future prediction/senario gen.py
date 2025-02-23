import numpy as np
import random
import math
random.seed(3)


xpos = random.uniform(0,10)
ypos = random.uniform(0,10)

xvel = random.uniform(-1,1)
yvel = random.uniform(-1,1)

inlist= []
plist = []
for i in range(100):
    for i in range(20):
        xpos += xvel
        ypos += yvel

        if xpos > 10:
            xvel = xvel*-1

        if xpos < 0:
            xvel = xvel*-1

        if ypos > 10:
            yvel = yvel*-1

        if ypos < 0:
            yvel = yvel*-1
    
        if i < 18:
            inlist.append(xpos)
            inlist.append(ypos)

        if i > 18:
            plist.append(xpos)
            plist.append(ypos)



input_set = np.asarray(inlist, dtype=np.float32)
labels = np.asarray(plist, dtype=np.float32)
#print(labels)
#print(input_set)
input_set = input_set.reshape(100,36)
labels = labels.reshape(100,2)

np.save('input.npy', input_set)
np.save('output', labels)

print(input_set)
print(labels)

#########################################################################

