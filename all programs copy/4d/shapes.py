import funcs
import math
import pygame as pg
import numpy as np
import random

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        

class obj:
    def __init__(self, x,y,z, pointlst, linelst):
        self.x = x
        self.y = y
        self.z = z
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.points = pointlst#list of point objects
        self.lines = linelst#list of lists of size 2, each sublist has 2 indexs of self.points representing which 2 points get connected

    def draw(self, surface, w,h, fov, az):

        for i in self.points:
            dst = funcs.norm(i.x+self.x,0,i.z+self.z)
            sAz = math.atan2(i.x+self.x,i.z+self.z)

            sAz += az
            i.x = (math.sin(sAz) * dst) - self.x
            i.z = (math.cos(sAz) * dst) - self.z



        #for i in self.points:
         #   p = funcs.cast2D(fov, i.x+self.x,i.y+self.y,i.z+self.z, w,h)
          #  pg.draw.circle(surface, (0,0,0), p, 5)
        for i in self.lines:
            p1 = funcs.cast2D(fov, self.points[i[0]].x+self.x,self.points[i[0]].y+self.y,self.points[i[0]].z+self.z, w,h)
            p2 = funcs.cast2D(fov, self.points[i[1]].x+self.x,self.points[i[1]].y+self.y,self.points[i[1]].z+self.z, w,h)
            p3 = funcs.cast2D(fov, self.points[i[2]].x+self.x,self.points[i[2]].y+self.y,self.points[i[2]].z+self.z, w,h)

            pg.draw.polygon(surface, self.colour, (p1,p2,p3))

        
        for i in self.points:
            dst = funcs.norm(i.x+self.x,0,i.z+self.z)
            sAz = math.atan2(i.x+self.x,i.z+self.z)
            sAz -= az

            i.x = (math.sin(sAz) * dst) - self.x
            i.z = (math.cos(sAz) * dst) - self.z