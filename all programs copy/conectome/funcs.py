import math
import numpy as np
import pygame as pg
import objects as objs
import random


def norm(a,b):
    return math.sqrt(a*a + b*b)


def activation(x):
    return x > 0.5


def drawBoard(surface, board, scale):
    for y in range(len(board[0,:])):
        for x in range(len(board[:,0])):
            pg.draw.rect(surface, (255*(1-board[y,x]), 255, 255*(1-board[y,x])), (x*scale, y*scale, scale,scale))


def mutate(worm, brainSize):
    nw = objs.worm(brainSize,200,200)
    nw.weights = worm.weights
    nw.weights[random.randint(0,29), random.randint(0,29)] += random.uniform(-0.1,0.1)
    return nw

def makeNewGen(worm, popSize, brainSize):
    nws = []
    for i in range(popSize):
        i = mutate(worm, brainSize)
        nws.append(i)
    return nws