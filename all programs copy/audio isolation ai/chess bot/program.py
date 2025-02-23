import math
import numpy as np
import pygame as pg
import funcs

background_colour = (255,255,255)
(width, height) = (600, 600)
black = (0,0,0)
screen = pg.display.set_mode((width, height))
pg.display.set_caption('cool editor')
screen.fill(background_colour)
pg.display.flip()

state = ['c','h','b','q','k','b','h','c','/','p','p','p','p','p','p','p','p','/',8,'/',8,'/',8,'/',8,'/','P','P','P','P','P','P','P','P','/','C','H','B','Q','K','B','H','C']


selected = [None,None]
turn = 0 #0 = white

pWhite = funcs.player(0)
pBlack = funcs.player(1)

movesTaken = 0

running = True
while running:
    mx,my = pg.mouse.get_pos()
    m1,m3,m2 = pg.mouse.get_pressed()
    if movesTaken == 0:
        turn = 0
    """
    if turn == 0:
        move = pWhite.think(state)
        selected, state, dc = funcs.movePeice(0,0,0,0,0,0,state,[None,None],turn,move)
    if turn == 1:
        move = pBlack.think(state)
        selected, state, dc = funcs.movePeice(0,0,0,0,0,0,state,[None,None],turn,move)
    
    turn = int(not turn)
    movesTaken += 1
    if movesTaken >= 120:
        bp = 0
        wp = 0
        for i in range(len(state)):
            if type(state[i]) == list:
                if state[i].isupper:
                    bp += 1
                if state[i].islower:
                    wp += 1

        if wp > bp:
            state, movesTaken = funcs.winnerWas(0,pWhite,pBlack)
        else:
            state, movesTaken = funcs.winnerWas(1,pWhite,pBlack)
        movesTaken = 0
        """
    funcs.movePeice(screen, width, height, mx,my,m1,state, sel, 1)

    if 'K' not in state:
        state, movesTaken = funcs.winnerWas(1,pWhite,pBlack)
    if 'k' not in state:
        state, movesTaken = funcs.winnerWas(0,pWhite,pBlack)

    
    funcs.drawGrid(screen, width, height, (224, 193, 90), (133, 98, 12))

    funcs.drawPeices(screen, width, height, 'sprites\\', state)

    pg.display.flip()
    screen.fill(background_colour)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()