import pygame as pg
import numpy as np
import math
import random
import funcs
import time


#16x15  32x30
width = 480
height = 450

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (126, 212, 83)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()


apple = (random.randint(0,14), random.randint(0,15))
apple = (7,9)
board = np.zeros((15,16))
board[apple] = -1
board[7,4] = 3
board[7,3] = 2
board[7,2] = 1
direction = 2
head = (7,4)

steps = 0

dirMap = funcs.makeDirMap(board)

clock = pg.time.Clock()
running = True
while running:
    clock.tick(25)


    
    #print(head)
    dirMap, steps = funcs.skip(board, dirMap, head)

    
    
    
    board, head = funcs.updateBoard(board, dirMap[head], head)
    funcs.drawBoard(screen, board, head, 30)
    if steps == 0:
        dirMap = funcs.makeDirMap(board)
    else:
        steps -= 1
    pg.display.flip()
    #time.sleep(1000)
    screen.fill(sky)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
