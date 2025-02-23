import pygame as pg
import numpy as np
import random
import cv2



def FindRules(TileImg, TileTypeTable):
    """
    vat: vat[x, y], x is TileType in question, y is position(up,right,down,left) of adj tile,
    vat[x,y] is list of all allowed tiles in position y for TileType x
    """
    NoTypes = len(TileTypeTable)
    vat = []
    for i in range(NoTypes):
        vat.append([[],[],[],[]])

    


def fromCenter(pos, length):
    return pos - (length/2)


def newWF(size, NoTypes):
    wf = np.empty(size, dtype=object)
    for r in range(wf.shape[0]):
        for c in range(wf.shape[1]):
            wf[r,c] = []
            for i in range(NoTypes):
                wf[r,c].append(i)
    return wf

def getEntropy(wf, rules):
    n = len(rules)
    rows, cols = wf.shape
    entropy = np.zeros((rows,cols))
    for r in range(rows):
        for c in range(cols):
            ent = len(wf[r,c])
            deltaEnt = ent/2
            entropy[r,c] = ent * random.uniform(1/4, 4)
    return entropy

def WFcollapse(wf, entropy):
    newEnt = np.where(entropy > 1, entropy, entropy*np.inf)
    poses = np.where(newEnt == np.min(newEnt))
    n = random.randint(0, len(poses[0])-1)
    r,c = (poses[0][n], poses[1][n])
    
    collapsedType = random.randint(0, len(wf[r,c])-1)
    wf[r,c] = [collapsedType]

    return wf


def propogate(wf, rules):
    
    rows, cols = wf.shape

    
    newArr = newWF((rows,cols), len(rules)-1)

    for r in range(rows):
        for c in range(cols):
            if len(wf[r,c]) == 1:
                newArr[r,c] = wf[r,c]


    for r in range(rows):
        for c in range(cols):
            if r>0:
                #propogate to tile above
                if len(wf[r-1,c]) > 1:
                    potentialList = []
                    for potentialTile in wf[r,c]:
                        for v in rules[potentialTile][0]:
                            potentialList.append(v)
                            if len(potentialList) < len(newArr[r-1,c]):
                                newArr[r-1,c] = potentialList
                    cleaned = list(set(newArr[r-1,c]))
                    newArr[r-1,c] = cleaned

            if r<rows-1:
                #propogate to tile below
                if len(wf[r+1,c]) > 1:
                    potentialList = []
                    for potentialTile in wf[r,c]:
                        for v in rules[potentialTile][2]:
                            potentialList.append(v)
                            if len(potentialList) < len(newArr[r+1,c]):
                                newArr[r+1,c] = potentialList
                    cleaned = list(set(newArr[r+1,c]))
                    newArr[r+1,c] = cleaned
            if c>0:
                #propogate to tile to left
                if len(wf[r,c-1]) > 1:
                    potentialList = []
                    for potentialTile in wf[r,c]:
                        for v in rules[potentialTile][3]:
                            potentialList.append(v)
                            if len(potentialList) < len(newArr[r,c-1]):
                                newArr[r,c-1] = potentialList
                    cleaned = list(set(newArr[r,c-1]))
                    newArr[r,c-1] = cleaned
            if c<cols-1:
                #propogate to tile to right
                if len(wf[r,c+1]) > 1:
                    potentialList = []
                    for potentialTile in wf[r,c]:
                        for v in rules[potentialTile][1]:
                            potentialList.append(v)
                            if len(potentialList) < len(newArr[r,c+1]):
                                newArr[r,c+1] = potentialList
                    cleaned = list(set(newArr[r,c+1]))
                    newArr[r,c+1] = cleaned

    for r in range(rows):
        for c in range(cols):
            if len(newArr[r,c]) > 1:
                if random.randint(1,1000) == 1:
                    newArr[r,c].append(random.randint(0, len(rules))-1)
    
    return wf, newArr
             

def checkIfCollapsed(wf):
    rows, cols = wf.shape
    for r in range(rows):
        for c in range(cols):
            if len(wf[r,c]) > 1:
                return False
    return True



def WFC(wf, rules, size):
    #make 2s array of entropys for each index
    #collapse tile with lowest entropy
    #propogate the collapse to the whole array
    #check if entire wf has collapsed:
    # return wf if true
    #eles:
    # go to step 1

    #while checkIfCollapsed(wf) == False:
    entropy = getEntropy(wf)
    wf = WFcollapse(wf, entropy)
    wf = propogate(wf, rules)
    return wf
    

def twod21d(x,y,width):
    return (y*width) + x



def FindRules(img_path, TileTypes):
    imgog = cv2.imread(img_path)
    rows, cols = imgog.shape[:2]
    img = np.pad(imgog, (0,1), mode='constant', constant_values=-1)
    rules = []

    for r in range(rows):
        for c in range(cols):
            ind = twod21d(c,r,cols)
            rules.append([[twod21d(c,r-1,cols)],[twod21d(c+1,r,cols)],[twod21d(c,r+1,cols)],[twod21d(c-1,r,cols)]])
            
            if r == 0:
                rules[-1][0] = []
            if c == 0:
                rules[-1][3] = []
            
            if r == rows-1:
                rules[-1][2] = []
            if c == cols-1:
                rules[-1][1] = []

            red = imgog[r,c][2]
            green = imgog[r,c][1]
            blue = imgog[r,c][0]
            TileTypes.TypeTable.append((red,green,blue))

    #rules = list(dict.fromkeys(rules))
    return rules
                

def arr_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)
