import numpy as np
import math
import pygame as pg
import funcs


class curve:
    def __init__(self, points):
        self.points = points # list of numpy vectors[x,y]

    def lerp(self, t, points):
        newPoints = []
        #(1-t)p0 + tp1
        for i in range(len(points)-1):
            #(1-t)*self.points[i] + t*self.points(i+1)
            newPoints.append((1-t)*points[i] + t*points[i+1])
        if len(newPoints) > 1:
            newPoints = self.lerp(t, newPoints)
        else:
            newPoints = newPoints[0]
        return newPoints
    def derivitave(self, t):
        prime = self.points[0]*(-3*t**2 + 6*t - 3) + self.points[1]*(9*t**2 - 12*t + 3) + self.points[2]*(-9*t**2 + 6*t) + self.points[3]*(3*t**2)
        return prime
    def acceleration(self, t):
        acc = self.points[0]*(-6*t + 6) + self.points[1]*(18*t - 12) + self.points[2]*(-18*t + 6) + self.points[3]*(6*t)
        return acc
    def normal(self,deriv):
        return np.array([-deriv[1], deriv[0]])
    def curvature(self, t):
        v = self.derivitave(t)
        a = self.acceleration(t)
        return np.linalg.det(np.array([v,a]))/abs(v**3)

    
    def draw(self, surface, spacing, startColour, endColour):
        pg.draw.line(surface, (255,255,255), (self.points[0]), (self.points[1]), 2)
        pg.draw.line(surface, (255,255,255), (self.points[0]), ((self.points[0]-self.points[1])+self.points[0]), 2)
        pg.draw.circle(surface, (255,255,255), (self.points[0]).astype(int), 7, 3)
        pg.draw.circle(surface, (255,255,255), (self.points[1]).astype(int), 7, 3)
        pg.draw.circle(surface, (255,255,255), ((self.points[0]-self.points[1])+self.points[0]).astype(int), 7, 3)

        pg.draw.line(surface, (255,255,255), (self.points[3]), (self.points[2]), 2)
        pg.draw.line(surface, (255,255,255), (self.points[3]), ((self.points[3]-self.points[2])+self.points[3]), 2)
        pg.draw.circle(surface, (255,255,255), (self.points[3]).astype(int), 7, 3)
        pg.draw.circle(surface, (255,255,255), (self.points[2]).astype(int), 7, 3)
        pg.draw.circle(surface, (255,255,255), ((self.points[3]-self.points[2])+self.points[3]).astype(int), 7, 3)

        pList = []
        nList = []
        for t in np.arange(0,1+spacing,spacing):
            pList.append(self.lerp(t, self.points))
            deriv = funcs.normalize(self.derivitave(t), 1)
            acc = funcs.normalize(self.acceleration(t), 1)
            normal = funcs.normalize(self.normal(deriv), 1)
            curveRad = np.clip(self.curvature(t)[0], -10000, 10000)
            #pg.draw.line(surface, (255,0,0), (pList[-1][0], pList[-1][1]), ((deriv[0]*50)+pList[-1][0], (deriv[1]*50)+pList[-1][1]), 2)
            pg.draw.line(surface, (0,255,0), (pList[-1][0], pList[-1][1]), (int((normal[0]*50)+pList[-1][0]), int((normal[1]*50)+pList[-1][1])), 2)
            nList.append(np.array([int((normal[0]*50)+pList[-1][0]), int((normal[1]*50)+pList[-1][1])]))
            #pg.draw.line(surface, (0,255,0), (pList[-1][0], pList[-1][1]), (int((acc[0]*50)+pList[-1][0]), int((acc[1]*50)+pList[-1][1])), 2)
            
            pCirc = pList[-1] + (curveRad*normal)
            #pg.draw.circle(surface, (16, 148, 204), (int(pCirc[0]), int(pCirc[1])), abs(int(curveRad))+1, 1)
            if len(pList) > 1:
                pg.draw.line(surface, funcs.colourLerp(startColour, endColour, t), (pList[-1]), (pList[-2]), 4)
            if len(nList) > 1:
                pg.draw.line(surface, funcs.colourLerp(startColour, endColour, t), (nList[-1]), (nList[-2]), 4)

    def dragPoint(self, mx,my, m1):
        moved = False
        if m1:
            for p in self.points:
                dst = funcs.norm(mx - p[0], my - p[1])
                if dst < 12:
                    moved = True
                    p[0] = mx
                    p[1] = my
                    break
            p = (self.points[0]-self.points[1])+self.points[0]
            dst = funcs.norm(mx - p[0], my - p[1])
            if dst < 12:
                moved = True
                p1 = (self.points[0]-np.array([mx,my]))+self.points[0]
                self.points[1] = p1
            
            p = (self.points[3]-self.points[2])+self.points[3]
            dst = funcs.norm(mx - p[0], my - p[1])
            if dst < 12:
                moved = True
                p1 = (self.points[3]-np.array([mx,my]))+self.points[3]
                self.points[2] = p1
            return moved
        return False
        