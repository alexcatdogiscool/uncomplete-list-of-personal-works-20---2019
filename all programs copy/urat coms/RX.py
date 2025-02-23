import numpy as np
import math
import cv2

infobin = np.load('data.npy')
print(infobin.shape)


info = []


x = []
y = []


reading = False

running = True

pos = 0
pos2 = 0



while running:
    bit = int(infobin[pos])


    if bit == 0:
        if reading == True:
            pos += 1
        if reading == False:
            reading = True
            pos += 1
            
            for i in range(2):
                for o in range(8):
                    bit = int(infobin[pos])
                    pos += 1
                    if i == 0:
                        x.append(bit)
                    else:
                        y.append(bit)

                if i == 1:
                    pos += 1

                    
                    


    if bit == 1:
        if reading == True:
            reading = False
            running = False
            pos += 1

        if reading == False:
            pass

    
    #if bit == 0:
     #   reading = True
      #  pos += 1
        
    #if reading == False:    
     #   if bit == 1:
      #      reading = False
       #     pos += 1
        
    #if reading == True:
     #   if bit == 1:
      #      running = False
       #     reading = False
        #    pos += 1
        
    

    if reading == True:
        temp = []
        for i in range(8):
            temp.append(int(infobin[pos]))
            pos += 1
        #info[pos2] = int("".join(map(str, temp)))
        info.append(int("".join(map(str, temp))))
        pos2 += 1

for i in range(pos2):
    info[i] = int(str(int(info[i])), 2)

x = (int(str(int((int("".join(map(str, x)))))), 2))*10
y =  (int(str(int((int("".join(map(str, y)))))), 2))*10
print(x, y)

info = np.asarray(info)
info = info.reshape(x, y, 3)

cv2.imwrite('recive.png', info)
