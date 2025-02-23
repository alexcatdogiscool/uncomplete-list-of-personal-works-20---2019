import math
import pygame as pg



def align(Nlist):
    for n in range(1, len(Nlist)):
        Nlist[n].angle = ((Nlist[n-1].a2+Nlist[n-1].angle) - math.pi) - Nlist[n].a1
        Nlist[n].x = (math.cos(Nlist[n-1].a2+Nlist[n-1].angle - math.pi) * (Nlist[n].rad + Nlist[n-1].rad)) + Nlist[n-1].x
        Nlist[n].y = (math.sin(Nlist[n-1].a2+Nlist[n-1].angle - math.pi) * (Nlist[n].rad + Nlist[n-1].rad))  + Nlist[n-1].y
        


def ghostCirc(surface, x,y, rad):
    pg.draw.circle(surface, (150, 150, 150), (int(x),int(y)), rad, 2)


def drawNodes(surface, l, rad):
    for n in l:
        pg.draw.circle(surface, (0,0,0), (n[0], n[1]), rad)


def norm(a,b):
    return math.sqrt(a*a + b*b)

def fixAngle(a):
    return a%(2*math.pi)