##### NAUGHTS AND CROSSES #####
import numpy as np
import math




def check(na,ca,pos):
    b = (na+ca)-1
    if b[pos] == 1:
        return True
    else:
        return False

def points(n,c,pos,player):
    if check(n,c,pos) == True:
        # wins
        if pos == 0:
            if n[pos+4]==0 and n[pos+8]==0:
                return 1000
            if n[pos+4]==0 or n[pos+8]==0:
                return 5
        if pos == 4:
            if n[pos-4]==0 and n[pos+4]==0:
                return 1000
            if n[pos-4]==0 or n[pos+4]==0:
                return 5
        if pos == 8:
            if n[pos-4]==0 and n[pos-8]==0:
                return 1000
            if n[pos-4]==0 or n[pos-8]==0:
                return 5

        if pos == 2:
            if n[pos+2]==0 and n[pos+4]==0:
                return 1000
            if n[pos+2]==0 or n[pos+4]==0:
                return 5
        if pos == 4:
            if n[pos-2]==0 and n[pos+2]==0:
                return 1000
            if n[pos-2]==0 or n[pos+2]==0:
                return 5
        if pos == 6:
            if n[pos-2]==0 and n[pos-4]==0:
                return 1000
            if n[pos-2]==0 or n[pos-4]==0:
                return 5

        if pos == 0:
            if n[pos+3]==0 and n[pos+6]==0:
                return 1000
            if n[pos+3]==0 or n[pos+6]==0:
                return 5
        if pos == 3:
            if n[pos-3]==0 and n[pos+3]==0:
                return 1000
            if n[pos-3]==0 or n[pos+3]==0:
                return 5
        if pos == 6:
            if n[pos-3]==0 and n[pos-6]==0:
                return 1000
            if n[pos-3]==0 or n[pos-6]==0:
                return 5
        
        if pos == 1:
            if n[pos+3]==0 and n[pos+6]==0:
                return 1000
            if n[pos+3]==0 or n[pos+6]==0:
                return 5
        if pos == 4:
            if n[pos-3]==0 and n[pos+3]==0:
                return 1000
            if n[pos-3]==0 or n[pos+3]==0:
                return 5
        if pos == 7:
            if n[pos-3]==0 and n[pos-6]==0:
                return 1000
            if n[pos-3]==0 or n[pos-6]==0:
                return 5
        
        if pos == 2:
            if n[pos+3]==0 and n[pos+6]==0:
                return 1000
            if n[pos+3]==0 or n[pos+6]==0:
                return 5
        if pos == 5:
            if n[pos-3]==0 and n[pos+3]==0:
                return 1000
        if pos == 8:
            if n[pos-3]==0 and n[pos-3]==0:
                return 1000
            if n[pos-3]==0 or n[pos-6]==0:
                return 5

        if pos == 0:
            if n[pos+1]==0 and n[pos+2]==0:
                return 1000
            if n[pos+1]==0 or n[pos+2]==0:
                return 5
            if n[pos-1]==0 and n[pos+1]==0:
                return 1000
            if n[pos-1]==0 or n[pos+1]==0:
                return 5
            if n[pos-2]==0 and n[pos-1]==0:
                return 1000
            if n[pos-2]==0 or n[pos-1]==0:
                return 5
        
        if pos == 3:
            if n[pos+1]==0 and n[pos+2]==0:
                return 1000
            if n[pos+1]==0 or n[pos+2]==0:
                return 5
            if n[pos-1]==0 and n[pos+1]==0:
                return 1000
            if n[pos-1]==0 or n[pos+1]==0:
                return 5
            if n[pos-2]==0 and n[pos-1]==0:
                return 1000
            if n[pos-2]==0 or n[pos-1]==0:
                return 5
        
        if pos == 6:
            if n[pos+1]==0 and n[pos+2]==0:
                return 1000
            if n[pos+1]==0 or n[pos+2]==0:
                return 5
            if n[pos-1]==0 and n[pos+1]==0:
                return 1000
            if n[pos-1]==0 or n[pos+1]==0:
                return 5
            if n[pos-2]==0 and n[pos-1]==0:
                return 1000
            if n[pos-2]==0 or n[pos-1]==0:
                return 5
        return 1
    if check(n,c,pos) == False:
        return 0
    

n = np.ones(9)
c = np.ones(9)


def alphabeta(n,c,depth,player):
    val = 0
    p=0
    for i in range(9):
        temp = points(n,c,i,player)
        if temp > val:
            val = temp
            p = i
    return(p)

for i in range(9):
    ppos = int(input())
    c[ppos] = 0
    n[alphabeta(n,c,1,0)] = 0
    print((n.reshape(3,3)-1)-(c.reshape(3,3)))