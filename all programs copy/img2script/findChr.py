import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
import os


def headCheck(img, used, x,y):
    i = (x) + len(img[0])*(y-1)
    if img[y-1,x] == 0 and i not in used:
        used.append(i)
        headCheck(img, used, x, y-1)

    i = (x-1) + len(img[0])*(y)
    if img[y,x-1] == 0 and i not in used:
        used.append(i)
        headCheck(img, used, x-1, y)

    i = (x+1) + len(img[0])*(y)
    if img[y,x+1] == 0 and i not in used:
        used.append(i)
        headCheck(img, used, x+1, y)

    i = (x) + len(img[0])*(y+1)
    if img[y+1,x] == 0 and i not in used:
        used.append(i)
        headCheck(img, used, x, y+1)



img = cv2.imread('src\\deez.jpg', cv2.IMREAD_GRAYSCALE)

thresh = 90

img = cv2.threshold(img, thresh, 1, cv2.THRESH_BINARY)[1]

imgWidth = img.shape[1]
imgHeight = img.shape[0]

print(imgWidth, imgHeight)

cv2.imwrite("chrMap.png", img*255)

chrMap = np.zeros((imgHeight, imgWidth))


i = 0
for y in range(imgHeight):
    for x in range(imgWidth):
        if img[y,x] == 0:
            while x+i < imgWidth-1 and y+i < imgHeight-1 and img[y+i,x+i] == 0:
                i += 1
        if i > 10:
            break
    if i > 10:
        break

startPos = (x+i, y+i)
chrHeight = i

i = 0
for y in range(imgHeight):
    for x in range(imgWidth):
        if img[imgHeight-y-1,imgWidth-x-1] == 0:
            while img[imgHeight-y-i-1,imgWidth-x-i-1] == 0:
                i += 1
        if i > 10:
            break
    if i > 10:
        break

endPos = (imgWidth-x-i, imgHeight-y-i)
chrHeight += i
chrHeight = int(chrHeight / 2)
#chrHeight = round((endPos[1] - startPos[1])/10)
###### REVERT THIS LATER ^ done :)

print(startPos, endPos)

print(chrHeight)

####### REVERT THIS LATER v done :)
numLines = round((endPos[1] - startPos[1])/chrHeight)#10
print(numLines)

imgNew = img[startPos[1]:endPos[1], startPos[0]:endPos[0]]
print(imgNew.shape)

cv2.imwrite('trimed.png', imgNew*255)

lines = []
for l in range(numLines):
    top = l*chrHeight
    bottom = (l*chrHeight)+chrHeight
    if bottom > imgNew.shape[0]-1:
        bottom = imgNew.shape[0]-1
    lines.append(imgNew[top:bottom, :])
    #cv2.imwrite('line{}.png'.format(l), lines[-1]*255)

spaces = []

l = 0
for imgs in lines:
    spaces.append([])
    for i in range(imgs.shape[1]):
        whites = (imgs[:,i].sum())
        if whites > imgs.shape[0]-3:
            spaces[l].append(i)
    l += 1


for line in range(numLines):
    for i in range(len(spaces[line])-1):
        if spaces[line][i]+1 == spaces[line][i+1]:
            spaces[line][i] = 'd'

for i in range(numLines):
    spaces[i] = [i for i in spaces[i] if i != 'd']
    spaces[i][0] = 0

print(spaces)

for l in range(numLines):
    for i in range(len(spaces[l])-1):
        indu = lines[l][:, spaces[l][i]:spaces[l][i+1]]*255
        if indu.shape[1]/chrHeight > 1.6:
            indu = indu[:,:chrHeight]
        indu = cv2.resize(indu, (28,28))
        cv2.imwrite('induvidual\\{}x{}.png'.format(l,i), indu)

path = 'induvidual'
files = os.listdir(path)
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.png'])))