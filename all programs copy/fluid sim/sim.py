import pygame as pg
import numpy as np
import math
import funcs


width = 600
height = 600

sky = (0,0,0)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()


scale = 10
board = funcs.makeBoard(width/scale, height/scale, 0)



running = True
while running:
    m1,m3,m2 = pg.mouse.get_pressed()
    mx,my = pg.mouse.get_pos()

    if m1:
        board[30,30] = 1


    board = funcs.updateBoard(board)
    funcs.drawBoard(screen, board, 10)





    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False