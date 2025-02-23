import numpy as np
import pygame as pg



def makeBoard(width, height, ambient):
    return np.zeros((int(height), int(width))) + ambient


def drawBoard(surface, b, scale):
    for r in range(len(b[0,:])):
        for c in range(len(b[:,0])):
            color = [b[r,c]*255]*3
            pg.draw.rect(surface, color, (c*scale, r*scale, scale, scale))


def updateBoard(b):
    nb = makeBoard(len(b[0,:]), len(b[:,0]), 0)

    for r in range(len(b[0,:])):
        for c in range(len(b[:,0])):
            fith = b[r,c]/5
            nb[r,c] += fith
            if r == 0:
                nb[r,c] += fith
            else:
                nb[r-1,c] += fith
            if c == 0:
                nb[r,c] += fith
            else:
                nb[r,c-1] += fith
            if r == len(b[0,:])-1:
                nb[r,c] += fith
            else:
                nb[r+1,c] += fith
            if c == len(b[:,0])-1:
                nb[r,c] += fith
            else:
                nb[r,c+1] += fith
    
    nb2 = makeBoard(len(b[0,:]), len(b[:,0]), 0)
    for r in range(len(nb[0,:])):
        for c in range(len(nb[:,0])):
            if r != len(nb[0,:])-1:
                nb2[r+1,c] += nb[r,c]
            else:
                nb2[r,c] += nb[r,c]
    
    return nb2
            
            
            