import numpy as np
import math

board = np.ones(9)

def printboard(n,c):
    b = (["  ",n[0],c[0],"  |  ",n[1],c[1],"  |  ",n[2],c[2],"  "],
           ["----+----+----"],   
           ["  ",n[3],c[3],"  |  ",n[4],c[4],"  |  ",n[5],c[5],"  "],
           ["----+----+----"],
           ["  ",n[6],c[6],"  |  ",n[7],c[7],"  |  ",n[8],c[8],"  "])
    
    for i in range(5):
        print(b[i])

n = np.array([0,0,0,0,0,0,0,0,0])
c = np.array([0,0,0,0,0,0,0,0,0])

printboard(n,c)