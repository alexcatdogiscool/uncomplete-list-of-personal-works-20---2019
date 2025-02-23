import math
import numpy as np
from numpy.lib.histograms import _ravel_and_check_weights
import pygame as pg
import random
import operator
import time
from copy import deepcopy



def drawBoard(surface, board, head, scale):
    for y in range(len(board[:,0])):
        for x in range(len(board[0,:])):
            if board[y,x] > 0:
                if (y,x) == head:
                    pg.draw.rect(surface, (0, 217, 255), (x*scale, y*scale, scale,scale))
                else:
                    if board[y,x] == 1:
                        pg.draw.rect(surface, (22, 120, 200), (x*scale, y*scale, scale,scale))
                    else:
                        pg.draw.rect(surface, (22, 130, 219), (x*scale, y*scale, scale,scale))
            if board[y,x] == -1:
                pg.draw.rect(surface, (255,0,0), (x*scale, y*scale, scale,scale))



def updateBoard(boardN, direction, head):
    board = deepcopy(boardN)
    n = 0
    loc = (0,0)
    sub = 1

    if direction == 0:
        head = (head[0]-1, head[1])
    if direction == 1:
        head = (head[0], head[1]+1)
    if direction == 2:
        head = (head[0]+1, head[1])
    if direction == 3:
        head = (head[0], head[1]-1)
    #print(direction, head)
    if board[head] == -1:
        sub = 0
    if board[head] > 0:
        return board, head
    for y in range(len(board[:,0])):
        for x in range(len(board[0,:])):
            if board[y,x] > n:
                n = board[y,x]
                loc = (x,y)
            if board[y,x] > 0:
                board[y,x] -= sub
    if sub == 0:
        n += 1
        while True:
            apple = (random.randint(0,len(board[:,0])-1), random.randint(0,len(board[0,:])-1))
            if board[apple] == 0:
                board[apple] = -1
                break
    if direction == 0:
        board[loc[1]-1,loc[0]] = n
        loc = (loc[1]-1,loc[0])
        return board, loc
    if direction == 1:
        board[loc[1],loc[0]+1] = n
        loc = (loc[1],loc[0]+1)
        return board, loc
    if direction == 2:
        board[loc[1]+1,loc[0]] = n
        loc = (loc[1]+1,loc[0])
        return board, loc
    if direction == 3:
        board[loc[1],loc[0]-1] = n
        loc = (loc[1],loc[0]-1)
        return board, loc
    

def makeDirMap(board):
    dirMap = np.zeros((len(board[:,0]),len(board[0,:])))
    for x in range(len(dirMap[0,:])):
        if x%2 == 0:
            dirMap[:,x] = 2
            dirMap[-1,x] = 1
        else:
            dirMap[:,x] = 0
            dirMap[1,x] = 1
            
    dirMap[0,:] = 3
    dirMap[0,0] = 2
    dirMap[1,-1] = 0
    return dirMap

def checkMap(board, t):
    for y in range(len(board[:,0])):
        for x in range(len(board[0,:])):
            if t == board[y,x]:
                return (y,x)
    return (0,0)

def moveInDir(pos, dir):
    if dir == 0:
        pos = (pos[0]-1, pos[1])
        return pos
    if dir == 1:
        pos = (pos[0], pos[1]+1)
        return pos
    if dir == 2:
        pos = (pos[0]+1, pos[1])
        return pos
    if dir == 3:
        pos = (pos[0], pos[1]-1)
        return pos

def step(dirMap, board, pos):
    if dirMap[pos] == 0:
        pos = (pos[0]-1, pos[1])
        return pos, board[pos]
    if dirMap[pos] == 1:
        pos = (pos[0], pos[1]+1)
        return pos, board[pos]
    if dirMap[pos] == 2:
        pos = (pos[0]+1, pos[1])
        return pos, board[pos]
    if dirMap[pos] == 3:
        pos = (pos[0], pos[1]-1)
        return pos, board[pos]

    

def eligableSpots(board, dirMap, head):
    spots = [1,1,1,1]

    #check if on edge
    if head[0] <= 0:
        spots[0] = 0
    if head[0] >= len(board[:,0])-1:
        spots[2] = 0
    if head[1] <= 0:
        spots[3] = 0
    if head[1] >= len(board[0,:])-1:
        spots[1] = 0
    

    #check if empty
    if spots[0]:
        nhead = (head[0]-1, head[1])
        if board[nhead] > 0:
            spots[0] = 0
    if spots[1]:
        nhead = (head[0], head[1]+1)
        if board[nhead] > 0:
            spots[1] = 0
    if spots[2]:
        nhead = (head[0]+1, head[1])
        if board[nhead] > 0:
            spots[2] = 0
    if spots[3]:
        nhead = (head[0], head[1]-1)
        if board[nhead] > 0:
            spots[3] = 0

    #run into tail?
    for i in range(4):
        if spots[i]:
            t = 0
            steps = 0

            if i == 0:
                newPos = (head[0]-1, head[1])
            if i == 1:
                newPos = (head[0], head[1]+1)
            if i == 2:
                newPos = (head[0]+1, head[1])
            if i == 3:
                newPos = (head[0], head[1]-1)
            
            while t < 1:
                newPos, t = step(dirMap, board, newPos)
                steps += 1
            if steps < t:
                spots[i] = 0

    return spots

def eligableSpots2(board, head):
    spots = [1,1,1,1]

    #check if on edge
    if head[0] <= 0:
        spots[0] = 0
    if head[0] >= len(board[:,0])-1:
        spots[2] = 0
    if head[1] <= 0:
        spots[3] = 0
    if head[1] >= len(board[0,:])-1:
        spots[1] = 0
    

    #check if empty
    if spots[0]:
        nhead = (head[0]-1, head[1])
        if board[nhead] > 0:
            spots[0] = 0
    if spots[1]:
        nhead = (head[0], head[1]+1)
        if board[nhead] > 0:
            spots[1] = 0
    if spots[2]:
        nhead = (head[0]+1, head[1])
        if board[nhead] > 0:
            spots[2] = 0
    if spots[3]:
        nhead = (head[0], head[1]-1)
        if board[nhead] > 0:
            spots[3] = 0
    
    return spots




def skip(board, dirMap, head):
    spots = eligableSpots2(board, head)# [1,0,0,1] = [u,r,d,l] 0 is no 1 is yes
    if sum(spots) == 0:
        print(":(")
        e = dontDie(board, head, 10)[0]
        head2 = head
        for k in e:
            dirMap[head2] = k
            head2 = moveInDir(head2, k)
        return dirMap, len(e) 
        #time.sleep(1000)
    lens = [1000,1000,1000,1000]

    for i in range(4):
        if spots[i]:
            if i == 0:
                newPos = (head[0]-1, head[1])
            if i == 1:
                newPos = (head[0], head[1]+1)
            if i == 2:
                newPos = (head[0]+1, head[1])
            if i == 3:
                newPos = (head[0], head[1]-1)
            
            t = board[newPos]
            
            steps = 0
            
            while t != -1:
                newPos, t = step(dirMap, board, newPos)
                steps += 1
                                  
            lens[i] = steps
            
    

    
    direction = lens.index(min(lens))
    dirMap[head] = direction
    #print(lens)
    
    return dirMap, 0


def recur(board, head, depth):
    paths = [None,None,None,None]
    spots = eligableSpots2(board, head)

    if depth == 0:
        return spots

    for i in range(4):
        if spots[i] == 1:
            nb, nh = updateBoard(board, i, head)
            paths[i] = recur(nb, nh, depth-1)
    
    return paths


def evaluateRecur(paths, board, head, depth, lenList):
    for i in range(4):
        if type(paths[i]) == list:
            nb, nh = updateBoard(board, i, head)
            lenList.append(evaluateRecur(paths[i], nb, nh, depth+1, lenList)[0])
        else:
            if paths[i] == None:
                lenList.append(100)
            else:
                lenList.append(depth)
            return depth, lenList

def evaluateRecur2(paths, board, head, dest, dirList):
    for i in range(4):
        if type(paths[i]) == list:
            nb, nh = updateBoard(board, i, head)
            dirList.append(i)
            n = evaluateRecur2(paths[i], nb, nh, dest-1, dirList)
            if n != None:
                return n
        elif type(paths[i]) != None:
            if dest == 0:
                return dirList

def dontDie(board, head, depth):
    p = (recur(board, head, depth))
    d = evaluateRecur(p, board, head, 0, [])
    e = evaluateRecur2(p, board, head, (min(d[1])), [])
    return e