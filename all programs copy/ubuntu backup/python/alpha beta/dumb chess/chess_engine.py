import numpy as np
from termcolor import colored as coloured
#pawn = 1, king = 2, nothing = 0  |  0 = white, 1 = black
#1 1  1  2  1  1
#2 0  1  1  1  0
#3 0  0  0  0  0
#4 0  1  1  1  0
#5 1  1  2  1  1
#  a  b  c  d  e

# how to move: if paw is at b2 and you want to move it forward one so input, "b2b3", from b2 to b3
#np array is y,x (for some reason)
board = np.zeros((2,5,5))


def move(b,player,msg):
    if msg[0] == 'a':
        xs = 0
    if msg[0] == 'b':
        xs = 1
    if msg[0] == 'c':
        xs = 2
    if msg[0] == 'd':
        xs = 3
    if msg[0] == 'e':
        xs = 4
    
    if msg[2] == 'a':
        xe = 0
    if msg[2] == 'b':
        xe = 1
    if msg[2] == 'c':
        xe = 2
    if msg[2] == 'd':
        xe = 3
    if msg[2] == 'e':
        xe = 4
    ys = int(msg[1])-1
    ye = int(msg[3])-1
    b = np.array(b)
    peice = int(b[player,ys,xs])
    print("")
    if peice == 0:
        return 0
    if peice == 1:
        if player == 0:
            if xs == xe and ye == ys+1:
                if xs == xe and ys == ye:
                    return 0
                if b[0,ye,xe] != 0:
                    return 0
                b[0,ys,xs] = 0
                b[0,ye,xe] = peice
                if b[1,ye,xe] != 0:
                    b[1,ye,xe] = 0
                return b
            else:
                return 0
        
        if player == 1:
            if xs == xe and ye == ys-1:
                if xs == xe and ys == ye:
                    return 0
                if b[1,ye,xe] != 0:
                    return 0
                b[1,ys,xs] = 0
                b[1,ye,xe] = peice
                if b[0,ye,xe] != 0:
                    b[0,ye,xe] = 0
                return b
            else:
                return 0


    if peice == 2:
        if player == 0:
            if (xs == xe or xe == xs-1 or xe == xs+1) and (ys == ye or ye == ys-1 or ye == ys+1):
                if xs == xe and ys == ye:
                    return 0
                if b[0,ye,xe] != 0:
                    return 0
                b[0,ys,xs] = 0
                b[0,ye,xe] = peice
                if b[1,ye,xe] != 0:
                    b[1,ye,xe] = 0
                return b
            else:
                return 0
        
        if player == 1:
            if (xs == xe or xe == xs-1 or xe == xs+1) and (ys == ye or ye == ys-1 or ye == ys+1):
                if xs == xe and ys == ye:
                    return 0
                if b[1,ye,xe] != 0:
                    return 0
                b[1,ys,xs] = 0
                b[1,ye,xe] = peice
                if b[0,ye,xe] != 0:
                    b[0,ye,xe] = 0
                return b
            else:
                return 0

def draw(b):
    def line():
        return "+---+---+---+---+---+"
    print(line(), "Player 0")
    for i in range(5):
        for n in range(5):
            if b[0,i,n] == 0:
                if b[1,i,n] == 0:
                    ch = " "
                if b[1,i,n] == 1:
                    ch = "Po"
                if b[1,i,n] == 2:
                    ch = "Ko"

            if b[0,i,n] == 1:
                ch = "P"
            if b[0,i,n] == 2:
                ch = "K"
            
            print("|", end=" ")
            if ch == 'Po':
                print(coloured('P', 'red'), end=" ")
            if ch == 'Ko':
                print(coloured('K', 'red'), end=" ")
            if ch == 'K':
                print('K', end=" ")
            if ch == 'P':
                print('P', end=" ")
            if ch == " ":
                print(" ", end=" ")
            if n == 4:
                print('|')
        print(line())





board[0,0,:] = 1
board[0,0,2] = 2
board[0,1,1] = 1
board[0,1,2] = 1
board[0,1,3] = 1

board[1,4,:] = 1
board[1,4,2] = 2
board[1,3,1] = 1
board[1,3,2] = 1
board[1,3,3] = 1


curp = 0
while True:
    # do visual stuff
    draw(board)
    # end visual stuff

    print("player {0}:  ".format(curp), end="")
    play = input()
    ans = move(board, curp, play)
    if type(ans) == int:
        print("Illegal move, try again")
        if curp == 0:
            curp = 1
        else:
            curp = 0
    else:
        board = ans

    if curp == 0:
        curp = 1
    else:
        curp = 0