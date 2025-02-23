import funcs
import math
import pygame as pg
import numpy as np

class point:
    def __init__(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class obj:
    def __init__(self, x,y,z,w, pointlst, linelst):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.points = pointlst#list of point objects
        self.lines = linelst#list of lists of size 2, each sublist has 2 indexs of self.points representing which 2 points get connected

    def draw(self, surface, w,h, fov):
        for i in self.points:
            p = funcs.cast3D(fov, i.x+self.x,i.y+self.y,i.z+self.z,i.w+self.w)
            p = funcs.cast2D(fov, p[0],p[1],p[2], w,h)
            
            #p = funcs.cast2D(fov, i.x+self.x,i.y+self.y,i.z+self.z, w,h)
            pg.draw.circle(surface, (0,0,0), p, 5)
        for i in self.lines:
            p1 = funcs.cast3D(fov, self.points[i[0]].x+self.x,self.points[i[0]].y+self.y,self.points[i[0]].z+self.z,self.points[i[0]].w+self.w)
            p1 = funcs.cast2D(fov, p1[0],p1[1],p1[2], w,h)

            p2 = funcs.cast3D(fov, self.points[i[1]].x+self.x,self.points[i[1]].y+self.y,self.points[i[1]].z+self.z,self.points[i[1]].w+self.w)
            p2 = funcs.cast2D(fov, p2[0],p2[1],p2[2], w,h)

            pg.draw.line(surface, (0,0,0), p1,p2, 3)