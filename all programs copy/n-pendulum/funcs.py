import objects as objs
import math


def vectadd(v1, v2):
    return objs.vector(v1.x + v2.x, v1.y + v2.y)

def norm(a,b):
    return math.sqrt(a*a + b*b)


def makePend(n, linkLen, start, direction):
    nodes = []
    lenList = [linkLen]*(n-1)
    for i in range(n):
        if direction == 0:
            nodes.append(objs.node(start.x, start.y-(i*linkLen)))
        else:
            nodes.append(objs.node(start.x, start.y+(i*linkLen)))
    
    pend = objs.pend(nodes, lenList)

    return pend