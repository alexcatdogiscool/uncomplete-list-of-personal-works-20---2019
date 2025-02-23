import math
import pygame as pg
import numpy as np
import random


def drawGrid(surface, width, height, wcol, bcol):
    wd = int(width/8)
    hd = int(height/8)

    for h in range(8):
        for w in range(8):
            if (h + w) % 2 != 0:
                pg.draw.rect(surface, bcol, (w*wd, h*hd, wd,hd))
            else:
                pg.draw.rect(surface, wcol, (w*wd, h*hd, wd,hd))


def drawPeices(surface, width, height, sspath, state):
    cx = 0
    cy = 0

    wd = int(width/8)
    hd = int(height/8)
    
    for i in range(len(state)):
        if state[i] == '/':
            cy += 1
            cx = 0
            continue
        if type(state[i]) == type(0):
            cx += state[i]
            continue
        
        if state[i] == 'P':
            pw = pg.image.load(sspath + 'PAWN_W.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'H':
            pw = pg.image.load(sspath + 'HORSE_W.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'C':
            pw = pg.image.load(sspath + 'CASTLE_W.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'B':
            pw = pg.image.load(sspath + 'BISHOP_W.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'Q':
            pw = pg.image.load(sspath + 'QUEEN_W.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'K':
            pw = pg.image.load(sspath + 'KING_W.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        


        if state[i] == 'p':
            pw = pg.image.load(sspath + 'PAWN_B.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'h':
            pw = pg.image.load(sspath + 'HORSE_B.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'c':
            pw = pg.image.load(sspath + 'CASTLE_B.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'b':
            pw = pg.image.load(sspath + 'BISHOP_B.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'q':
            pw = pg.image.load(sspath + 'QUEEN_B.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        if state[i] == 'k':
            pw = pg.image.load(sspath + 'KING_B.png')
            pw = pg.transform.scale(pw, (wd,hd))
            surface.blit(pw, (wd*cx, hd*cy))
            cx += 1

        


def movePeice(surface,width,height, mx,my,m1, state,sel, turn, move=None):
    wd = int(width/8)
    hd = int(height/8)
    px,py = (sel)
    
    if move == None:
        moves = np.zeros((8,8))

        if px != None:
            for h in range(8):
                for w in range(8):
                    if checkMove(w,h, px,py, state, turn) == True and (w,h) != (px,py):
                        pg.draw.circle(surface, (150,150,150), (int(w*wd + (wd/2)), int(h*hd + (wd/2))), 10)
                        moves[w,h] = 1

        if m1 == 1:
            tpx,tpy = int(mx/wd), int(my/hd)
            if moves[tpx,tpy] == 1:
                board = state2Arr(state)
                peice = board[sel[0],sel[1]]
                board[tpx,tpy] = peice
                board[sel[0],sel[1]] = ''
                state = arr2State(board)
                turn = int(not turn)
            else:
                px,py = tpx,tpy
    else:
        board = state2Arr(state)
        peice = board[move[0],move[1]]
        board[move[2],move[3]] = peice
        board[move[0],move[1]] = ''
        state = arr2State(board)
        turn = int(not turn)    
    return [px,py], state, turn


def checkMove(pcx,pcy,px,py,state, turn):
    board = state2Arr(state)
    peice = board[px,py]
    if peice == '':
        return False
    if peice.islower() != turn:
        return False
    

    ##### WHITES #####

    if peice == 'P':
        if py == 6 and (pcx,pcy) == (px,py-2) and board[pcx,pcy] == '':
            return True
        if pcy == py - 1 and pcx == px and board[pcx,pcy] == '':
            return True
        if (pcx,pcy) == (px-1,py-1) and board[pcx,pcy] != '' and board[pcx,pcy].islower():
            return True
        if (pcx,pcy) == (px+1,py-1) and board[pcx,pcy] != '' and board[pcx,pcy].islower():
            return True
        
    if peice == 'H':
        if (pcx,pcy) == (px-1,py-2) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        if (pcx,pcy) == (px+1,py-2) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        if (pcx,pcy) == (px-2,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        if (pcx,pcy) == (px+2,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True

        if (pcx,pcy) == (px-2,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        if (pcx,pcy) == (px+2,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        if (pcx,pcy) == (px-1,py+2) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        if (pcx,pcy) == (px+1,py+2) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True

    if peice == 'C':
        if pcx == px and pcy < py:
            tmpBoardu = (board[px,pcy:py])[::-1]
            ps = 0
            for i in range(len(tmpBoardu)):
                if tmpBoardu[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].islower():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True
            #return True
        
        if pcx == px and pcy > py:
            tmpBoardd = board[px,py+1:pcy+1][::-1]
            ps = 0
            for i in range(len(tmpBoardd)):
                if tmpBoardd[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].islower():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True
                
            #return True

    if peice == 'B':
        if abs(pcx-px) == abs(pcy-py):
            mlul = min(px+1,py+1)-1
            mlur = min(8-px,py+1)-1
            mldl = min(px+1,8-py)-1
            mldr = min(8-px,8-py)-1

            tmpBoardul = np.empty(mlul, dtype=str)
            tmpBoardur = np.empty(mlur, dtype=str)
            tmpBoarddl = np.empty(mldl, dtype=str)
            tmpBoarddr = np.empty(mldr, dtype=str)

            for i in range(mlul):
                tmpBoardul[i] = board[px-(i+1), py-(i+1)]
            
            for i in range(mlur):
                tmpBoardur[i] = board[px+(i+1), py-(i+1)]
            
            for i in range(mldl):
                tmpBoarddl[i] = board[px-(i+1), py+(i+1)]

            for i in range(mldr):
                tmpBoarddr[i] = board[px+(i+1), py+(i+1)]

            if pcx < px and pcy < py:
                ps = 0
                for i in range(len(tmpBoardul)):
                    if tmpBoardul[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcy < py and pcx > px:
                ps = 0
                for i in range(len(tmpBoardur)):
                    if tmpBoardur[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True
            
            if pcx < px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddl)):
                    if tmpBoarddl[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcx > px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddr)):
                    if tmpBoarddr[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True
    
    if peice == 'Q':
        if pcx == px and pcy < py:
            tmpBoardu = (board[px,pcy:py])[::-1]
            ps = 0
            for i in range(len(tmpBoardu)):
                if tmpBoardu[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].islower():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True
        if pcx == px and pcy > py:
            tmpBoardd = board[px,py+1:pcy+1][::-1]
            ps = 0
            for i in range(len(tmpBoardd)):
                if tmpBoardd[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].islower():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True

        
        if pcy == py and pcx < px:
            tmpBoardl = board[pcx:px,py][::-1]
            ps = 0
            for i in range(len(tmpBoardl)):
                if tmpBoardl[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(px-pcx) and board[pcx,pcy].islower():
                        return True
                    else:
                        return False
                elif i+1 == abs(px-pcx):
                    return True

        if pcy == py and pcx > px:
            tmpBoardr = board[px+1:pcx+1,py]
            ps = 0
            for i in range(len(tmpBoardr)):
                if tmpBoardr[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(px-pcx) and board[pcx,pcy].islower():
                        return True
                    else:
                        return False
                elif i+1 == abs(px-pcx):
                    return True

        ###########

        if abs(pcx-px) == abs(pcy-py):
            mlul = min(px+1,py+1)-1
            mlur = min(8-px,py+1)-1
            mldl = min(px+1,8-py)-1
            mldr = min(8-px,8-py)-1

            tmpBoardul = np.empty(mlul, dtype=str)
            tmpBoardur = np.empty(mlur, dtype=str)
            tmpBoarddl = np.empty(mldl, dtype=str)
            tmpBoarddr = np.empty(mldr, dtype=str)

            for i in range(mlul):
                tmpBoardul[i] = board[px-(i+1), py-(i+1)]
            
            for i in range(mlur):
                tmpBoardur[i] = board[px+(i+1), py-(i+1)]
            
            for i in range(mldl):
                tmpBoarddl[i] = board[px-(i+1), py+(i+1)]

            for i in range(mldr):
                tmpBoarddr[i] = board[px+(i+1), py+(i+1)]

            if pcx < px and pcy < py:
                ps = 0
                for i in range(len(tmpBoardul)):
                    if tmpBoardul[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcy < py and pcx > px:
                ps = 0
                for i in range(len(tmpBoardur)):
                    if tmpBoardur[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True
            
            if pcx < px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddl)):
                    if tmpBoarddl[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcx > px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddr)):
                    if tmpBoarddr[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].islower():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

    if peice == 'K':
        if (pcx,pcy) == (px,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
        if (pcx,pcy) == (px,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
        if (pcx,pcy) == (px-1,py) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
        if (pcx,pcy) == (px+1,py) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
        if (pcx,pcy) == (px-1,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
        if (pcx,pcy) == (px+1,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
        if (pcx,pcy) == (px-1,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
        if (pcx,pcy) == (px+1,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].islower()):
            return True
        
    ##### BLACKS #####     

    if peice == 'p':
        if py == 1 and (pcx,pcy) == (px,py+2) and board[pcx,pcy] == '':
            return True
        if pcy == py + 1 and pcx == px and board[pcx,pcy] == '':
            return True
        if (pcx,pcy) == (px-1,py+1) and board[pcx,pcy] != '' and board[pcx,pcy].isupper():
            return True
        if (pcx,pcy) == (px+1,py+1) and board[pcx,pcy] != '' and board[pcx,pcy].isupper():
            return True
        
    if peice == 'h':
        if (pcx,pcy) == (px-1,py-2) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True
        if (pcx,pcy) == (px+1,py-2) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True
        if (pcx,pcy) == (px-2,py-1) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True
        if (pcx,pcy) == (px+2,py-1) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True

        if (pcx,pcy) == (px-2,py+1) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True
        if (pcx,pcy) == (px+2,py+1) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True
        if (pcx,pcy) == (px-1,py+2) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True
        if (pcx,pcy) == (px+1,py+2) and (board[pcx,pcy] == ''or board[pcx,pcy].isupper()):
            return True

    if peice == 'c':
        if pcx == px and pcy < py:
            tmpBoardu = (board[px,pcy:py])#[::-1]
            ps = 0
            for i in range(len(tmpBoardu)):
                if tmpBoardu[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].isupper():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True
            #return True
        
        if pcx == px and pcy > py:
            tmpBoardd = board[px,py+1:pcy+1]#[::-1]
            ps = 0
            for i in range(len(tmpBoardd)):
                if tmpBoardd[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].isupper():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True
                
            #return True

    if peice == 'b':
        if abs(pcx-px) == abs(pcy-py):
            mlul = min(px+1,py+1)-1
            mlur = min(8-px,py+1)-1
            mldl = min(px+1,8-py)-1
            mldr = min(8-px,8-py)-1

            tmpBoardul = np.empty(mlul, dtype=str)
            tmpBoardur = np.empty(mlur, dtype=str)
            tmpBoarddl = np.empty(mldl, dtype=str)
            tmpBoarddr = np.empty(mldr, dtype=str)

            for i in range(mlul):
                tmpBoardul[i] = board[px-(i+1), py-(i+1)]
            
            for i in range(mlur):
                tmpBoardur[i] = board[px+(i+1), py-(i+1)]
            
            for i in range(mldl):
                tmpBoarddl[i] = board[px-(i+1), py+(i+1)]

            for i in range(mldr):
                tmpBoarddr[i] = board[px+(i+1), py+(i+1)]

            if pcx < px and pcy < py:
                ps = 0
                for i in range(len(tmpBoardul)):
                    if tmpBoardul[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcy < py and pcx > px:
                ps = 0
                for i in range(len(tmpBoardur)):
                    if tmpBoardur[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True
            
            if pcx < px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddl)):
                    if tmpBoarddl[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcx > px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddr)):
                    if tmpBoarddr[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True
    
    if peice == 'q':
        if pcx == px and pcy < py:
            tmpBoardu = (board[px,pcy:py])
            ps = 0
            for i in range(len(tmpBoardu)):
                if tmpBoardu[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].isupper():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True
        if pcx == px and pcy > py:
            tmpBoardd = board[px,py+1:pcy+1]
            ps = 0
            for i in range(len(tmpBoardd)):
                if tmpBoardd[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(py-pcy) and board[pcx,pcy].isupper():
                        return True
                    else:
                        return False
                elif i+1 == abs(py-pcy):
                    return True

        
        if pcy == py and pcx < px:
            tmpBoardl = board[pcx:px,py][::-1]
            ps = 0
            for i in range(len(tmpBoardl)):
                if tmpBoardl[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(px-pcx) and board[pcx,pcy].isupper():
                        return True
                    else:
                        return False
                elif i+1 == abs(px-pcx):
                    return True

        if pcy == py and pcx > px:
            tmpBoardr = board[px+1:pcx+1,py]
            ps = 0
            for i in range(len(tmpBoardr)):
                if tmpBoardr[i] != '':
                    ps += 1
                    if ps == 1 and i+1 == abs(px-pcx) and board[pcx,pcy].isupper():
                        return True
                    else:
                        return False
                elif i+1 == abs(px-pcx):
                    return True

        ###########

        if abs(pcx-px) == abs(pcy-py):
            mlul = min(px+1,py+1)-1
            mlur = min(8-px,py+1)-1
            mldl = min(px+1,8-py)-1
            mldr = min(8-px,8-py)-1

            tmpBoardul = np.empty(mlul, dtype=str)
            tmpBoardur = np.empty(mlur, dtype=str)
            tmpBoarddl = np.empty(mldl, dtype=str)
            tmpBoarddr = np.empty(mldr, dtype=str)

            for i in range(mlul):
                tmpBoardul[i] = board[px-(i+1), py-(i+1)]
            
            for i in range(mlur):
                tmpBoardur[i] = board[px+(i+1), py-(i+1)]
            
            for i in range(mldl):
                tmpBoarddl[i] = board[px-(i+1), py+(i+1)]

            for i in range(mldr):
                tmpBoarddr[i] = board[px+(i+1), py+(i+1)]

            if pcx < px and pcy < py:
                ps = 0
                for i in range(len(tmpBoardul)):
                    if tmpBoardul[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcy < py and pcx > px:
                ps = 0
                for i in range(len(tmpBoardur)):
                    if tmpBoardur[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True
            
            if pcx < px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddl)):
                    if tmpBoarddl[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

            if pcx > px and pcy > py:
                ps = 0
                for i in range(len(tmpBoarddr)):
                    if tmpBoarddr[i] != '':
                        ps += 1
                        if ps == 1 and (i+1 == min(abs(px-pcx),abs(py-pcy))) and board[pcx,pcy].isupper():
                            return True
                        else:
                            return False
                    elif i+1 == min(abs(px-pcx),abs(py-pcy)):
                        return True

    if peice == 'k':
        if (pcx,pcy) == (px,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
        
        if (pcx,pcy) == (px,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
        
        if (pcx,pcy) == (px-1,py) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
        
        if (pcx,pcy) == (px+1,py) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
        
        if (pcx,pcy) == (px-1,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
        
        if (pcx,pcy) == (px+1,py-1) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
        
        if (pcx,pcy) == (px-1,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
        
        if (pcx,pcy) == (px+1,py+1) and (board[pcx,pcy] == '' or board[pcx,pcy].isupper()):
            return True
    return False



def state2Arr(state):


    cx = 0
    cy = 0

    a = np.empty((8,8), dtype=str)
    
    for i in range(len(state)):
        if state[i] == '/':
            cy += 1
            cx = 0
            continue
        if type(state[i]) == type(0):
            cx += state[i]
            continue
        
        if state[i] == 'P':
            a[cx,cy] = 'P'
            cx += 1

        if state[i] == 'H':
            a[cx,cy] = 'H'
            cx += 1

        if state[i] == 'C':
            a[cx,cy] = 'C'
            cx += 1

        if state[i] == 'B':
            a[cx,cy] = 'B'
            cx += 1

        if state[i] == 'Q':
            a[cx,cy] = 'Q'
            cx += 1

        if state[i] == 'K':
            a[cx,cy] = 'K'
            cx += 1

        


        if state[i] == 'p':
            a[cx,cy] = 'p'
            cx += 1

        if state[i] == 'h':
            a[cx,cy] = 'h'
            cx += 1

        if state[i] == 'c':
            a[cx,cy] = 'c'
            cx += 1

        if state[i] == 'b':
            a[cx,cy] = 'b'
            cx += 1

        if state[i] == 'q':
            a[cx,cy] = 'q'
            cx += 1

        if state[i] == 'k':
            a[cx,cy] = 'k'
            cx += 1

    return a

def arr2State(arr):
    fen = []
    for h in range(8):
        empt = 0
        for w in range(8):
            if arr[w,h] == '':
                empt += 1
            else:
                fen.append(empt)
                empt = 0
                fen.append(arr[w,h])
        fen.append(empt)
        if h != 7:
            fen.append('/')
    for i in range(len(fen)):
        if fen[i] == 0:
            fen[i] = 'del'
        if fen[i] == '/':
            for n in range(len(fen[i:-1])):
                if fen[i+(n+1)] == '/':
                    fen[i+n] = 'del'
                else:
                    break
    fenN = []
    for i in range(len(fen)):
        if fen[i] != 'del':
            fenN.append(fen[i])

    return fenN

def evaluate(state, move, turn):
    board = state2Arr(state)
    peiceTaken = board[move[2],move[3]]
    if peiceTaken.isupper() == turn:
        #return positave value
        if peiceTaken.lower() == 'p':
            return 1

        if peiceTaken.lower() == 'h':
            return 3

        if peiceTaken.lower() == 'b':
            return 3

        if peiceTaken.lower() == 'c':
            return 5

        if peiceTaken.lower() == 'q':
            return 9

        if peiceTaken.lower() == 'k':
            return 1000

    if peiceTaken.islower() == turn:
        #return - value
        if peiceTaken.lower() == 'p':
            return -1

        if peiceTaken.lower() == 'h':
            return -3

        if peiceTaken.lower() == 'b':
            return -3

        if peiceTaken.lower() == 'c':
            return -5

        if peiceTaken.lower() == 'q':
            return -9

        if peiceTaken.lower() == 'k':
            return -1000

    return 0

"""
def runAI(state,depth,realDepth, moves):
    if depth == realDepth:
        moves = algo(state,depth,1)

    maxPoints = 0
    curMove = [None,None,None,None,0,[]]
    for move in moves:
        if type(move) != int:
            if move != [0] and move[5] != [0]:
                points, dontCare = runAI(state, depth-1,depth,move[5])
                if points > maxPoints:
                    maxPoints = points
                    curMove = move
            else:
                if move == [0]:
                    return 0, curMove
                else:
                    return move[4], curMove
    return maxPoints, move
"""
def runAI(state,depth,moves):
    if type(moves[0]) == int:
        return [0,0,0,0], 0
    #moves = algo(state,depth,1)
    maxPoints = -1
    bestMove = []
    for move in moves:
        mt = move
        points = 0
        while mt != [0]:

            tmpMove, tmpPoints = runAI(state,depth,mt)
            mt = mt[0]
            if tmpPoints > maxPoints:
                maxPoints = points
                bestMove = tmpMove
    #dc1, stateNew, dc2 = movePeice(0,0,0,0,0,0,state,[None,None],1,move=bestMove)
    return bestMove, maxPoints


"""
def algo(state, depth, curTurn):
    if depth == 0:
        return 0
    entireMoveWhole = []
    for hp in range(8):
        for wp in range(8):
            for hc in range(8):
                for wc in range(8):
                    canMove = checkMove(wc,hc,wp,hp,state,curTurn)
                    if canMove == True:
                        move = [wp,hp,wc,hc]
                        dontCare, tmpState, tmpCurTurn = movePeice(0,0,0,0,0,0,state,[None,None],curTurn,move=move)
                        moveWhole = [move[0],move[1],move[2],move[3], evaluate(state,move,curTurn), []]
                        moveWhole[5].append(algo(tmpState,depth-1,int(not curTurn)))
                        entireMoveWhole.append(moveWhole)
    return entireMoveWhole
"""

def algo(state,curTurn):
    moves = []
    for hp in range(8):
        for wp in range(8):
            for hc in range(8):
                for wc in range(8):
                    canMove = checkMove(wc,hc,wp,hp,state,curTurn)
                    if canMove == True:
                        moves.append([wp,hp,wc,hc])
    return moves[random.randint(0,len(moves)-1)]


def sigmoid(x):
    return (2/(1+np.exp(-x))) - 1


class player:
    def __init__(self, colour):
        self.col = colour

        # 768, 200, 128

        self.w1 = np.random.rand(768,200)-0.5
        self.w2 = np.random.rand(200,128)-0.5

        self.b1 = np.random.rand(200)-0.5
        self.b2 = np.random.rand(128)-0.5
        
    def think(self,state):
        board = state2Arr(state)
        input_set = []
        
        for h in range(8):
            for w in range(8):
                if board[w,h] == 'P':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'H':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'B':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'C':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'Q':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'K':
                    input_set.append(1)
                else:
                    input_set.append(0)



        for h in range(8):
            for w in range(8):
                if board[w,h] == 'p':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'h':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'b':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'c':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'q':
                    input_set.append(1)
                else:
                    input_set.append(0)

        for h in range(8):
            for w in range(8):
                if board[w,h] == 'k':
                    input_set.append(1)
                else:
                    input_set.append(0)

        z1 = sigmoid(np.dot(input_set, self.w1) + self.b1)
        z2 = sigmoid(np.dot(z1, self.w2) + self.b2).reshape(128,1)
        
        startPeice = z2[:64,0].reshape(8,8)
        goTo = z2[64:128,0].reshape(8,8)
        exclude = []
        move = [None,None,None,None]
        while None in move:
            cm = -10
            move = [None,None,None,None]
            for h in range(8):
                for w in range(8):
                    if startPeice[w,h] > cm and [w,h] not in exclude:
                        cm = startPeice[w,h]
                        move[0], move[1] = w,h
            cm = -10
            for h in range(8):
                for w in range(8):
                    canDo = checkMove(w,h,move[0],move[1],state,self.col)
                    if canDo == True:
                        if goTo[w,h] > cm:
                            cm = goTo[w,h]
                            move[2],move[3] = w,h
            exclude.append([move[0],move[1]])

        return move


def adjust(p, lr):
    p.w1 *= (np.random.rand(768,200)-0.5) * (0.5*lr)
    p.w2 *= (np.random.rand(200,128)-0.5) * (0.5*lr)
    return p

def saveBrain(p):
    if p.col == 0:
        np.savez("whiteBrain.npz", p.w1,p.w2,p.b1,p.b2)
    if p.col == 1:
        np.savez("blackBrain.npz", p.w1,p.w2,p.b1,p.b2)
    
def winnerWas(winner, p1,p2):
    if winner == 0:
        print("White won")
        adjust(p2, 0.01)
    if winner == 1:
        print("Black won")
        adjust(p1, 0.01)
    
    saveBrain(p1)
    saveBrain(p2)

    state = ['c','h','b','q','k','b','h','c','/','p','p','p','p','p','p','p','p','/',8,'/',8,'/',8,'/',8,'/','P','P','P','P','P','P','P','P','/','C','H','B','Q','K','B','H','C']

    return state, 0