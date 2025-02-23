import pygame as pg
import numpy as np
import math
import time
import numpy as np
import random


def norm(x,y):
    return (x**2 + y**2)**0.5

def vectadd(v1,v2):
    v1x = math.cos(v1.angle) * v1.mag
    v1y = math.sin(v1.angle) * v1.mag
    v2x = math.cos(v2.angle) * v2.mag
    v2y = math.sin(v2.angle) * v2.mag
    vsx = v1x+v2x
    vsy = v1y+v2y
    vs = vector()
    vs.mag = norm(vsx,vsy)
    vs.angle = math.atan2(vsy,vsx)
    return vs

def step(point, vec):
    point.x += math.cos(vec.angle) * vec.mag
    point.y += math.sin(vec.angle) * vec.mag
    return point

def groundcol(point, floorHeight):
    if point.y > floorHeight:
        return True, point.y - floorHeight
    return False, 0

def correctlen(p1,p2, length, elasticity, efficiency):
    dst = length - norm(p1.x-p2.x, p1.y-p2.y)
    at2 = math.atan2(p1.y-p2.y, p1.x-p2.x)
    at1 = at2 + math.pi

    p1stepvec = vector()
    p1stepvec.angle = at2
    p1stepvec.mag = (dst/2) * elasticity
    p2stepvec = vector()
    p2stepvec.mag = p1stepvec.mag
    p2stepvec.angle = at1
    
    movevec1 = vector()
    movevec1.mag = p1stepvec.mag * (efficiency/elasticity)
    movevec1.angle = at1
    movevec2 = vector()
    movevec1.angle = at2
    movevec2.mag = movevec1.mag
    p1 = step(p1, movevec1)
    p2 = step(p2, movevec2)

    p1.vel = vectadd(p1.vel, p1stepvec)
    zerovec = vector()
    zerovec.mag = 0
    p2.vel = vectadd(p2.vel, p2stepvec)

    return p1,p2

    


width, height = 800,800
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
sky = (112, 232, 250)

screen = pg.display.set_mode((width,height))
screen.fill(sky)
pg.display.flip()


class vector:
    def __init__(self):
        self.mag = random.uniform(0,1)
        self.angle = random.uniform(0,2*math.pi)

class point:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.vel = vector()

class plane:
    def __init__(self):
        self.p1 = point()
        self.p1.y = 160
        self.p1.vel.mag = 0.2
        self.p2 = point()

        self.len = 50

    def draw(self):
        pg.draw.circle(screen, black, (self.p1.x, self.p1.y), 5)
        pg.draw.circle(screen, black, (self.p2.x, self.p2.y), 5)
        pg.draw.line(screen, black, (self.p1.x,self.p1.y), (self.p2.x, self.p2.y), 2)

    def lenadj(self):
        self.p1, self.p2 = correctlen(self.p1,self.p2, self.len)

    def move(self):
        self.p1 = step(self.p1, self.p1.vel)
        self.p2 = step(self.p2, self.p2.vel)

    def grav(self, G):
        self.p1.vel = vectadd(self.p1.vel, G)
        self.p2.vel = vectadd(self.p2.vel, G)

    def bounce(self, p1col,p2col, restitution, friction):
        

        if p1col[0] == True:
            self.p1.y -= p1col[1]
            self.p2.y -= p1col[1]
            vy = math.sin(self.p1.vel.angle) * self.p1.vel.mag
            vyvec = vector()
            vyvec.mag = (1+restitution) * vy
            vyvec.angle = -math.pi/2
            self.p1.vel = vectadd(self.p1.vel, vyvec)
            # friction
            vx = math.cos(self.p1.vel.angle) * self.p1.vel.mag
            vxfric = vector()
            vxfric.mag = vx * friction
            vxfric.angle = math.pi
            self.p1.vel = vectadd(self.p1.vel, vxfric)

        if p2col[0] == True:
            self.p1.y -= p2col[1]
            self.p2.y -= p2col[1]
            vy = math.sin(self.p2.vel.angle) * self.p2.vel.mag
            vyvec = vector()
            vyvec.mag = (1+restitution) * vy
            vyvec.angle = -math.pi/2
            self.p2.vel = vectadd(self.p2.vel, vyvec)
            # friction
            vx = math.cos(self.p2.vel.angle) * self.p2.vel.mag
            vxfric = vector()
            vxfric.mag = vx * friction
            vxfric.angle = math.pi
            self.p2.vel = vectadd(self.p2.vel, vxfric)



class square:
    def __init__(self):
        self.p1 = point()
        self.p2 = point()
        self.p3 = point()
        self.p4 = point()
        
        
        self.p1.vel.mag = 0.5

        self.wid = 70

    def draw(self):
        pg.draw.circle(screen, black, (self.p1.x, self.p1.y), 5)
        pg.draw.circle(screen, black, (self.p2.x, self.p2.y), 5)
        pg.draw.circle(screen, black, (self.p3.x, self.p3.y), 5)
        pg.draw.circle(screen, black, (self.p4.x, self.p4.y), 5)

        pg.draw.line(screen, black, (self.p1.x, self.p1.y), (self.p2.x,self.p2.y), 2)
        pg.draw.line(screen, black, (self.p2.x, self.p2.y), (self.p3.x,self.p3.y), 2)
        pg.draw.line(screen, black, (self.p3.x, self.p3.y), (self.p4.x,self.p4.y), 2)
        pg.draw.line(screen, black, (self.p4.x, self.p4.y), (self.p1.x,self.p1.y), 2)

    def lenadj(self):
        self.p1, self.p2 = correctlen(self.p1, self.p2, self.wid)
        self.p1, self.p4 = correctlen(self.p1, self.p4, self.wid)
        self.p1, self.p3 = correctlen(self.p1, self.p3, self.wid * 2**0.5)
        self.p2, self.p3 = correctlen(self.p2, self.p3, self.wid)
        self.p2, self.p4 = correctlen(self.p2, self.p4, self.wid * 2**0.5)
        self.p3, self.p4 = correctlen(self.p3, self.p4, self.wid)

    def move(self):
        self.p1 = step(self.p1, self.p1.vel)
        self.p2 = step(self.p2, self.p2.vel)
        self.p3 = step(self.p3, self.p3.vel)
        self.p4 = step(self.p4, self.p4.vel)

    def grav(self, G):
        self.p1.vel = vectadd(self.p1.vel, G)
        self.p2.vel = vectadd(self.p2.vel, G)
        self.p3.vel = vectadd(self.p3.vel, G)
        self.p4.vel = vectadd(self.p4.vel, G)

    def bounce(self, floorHeight, restitution, friction):
        
        if self.p1.y > floorHeight:
            col = self.p1.y - floorHeight
            self.p1.y -= col
            self.p2.y -= col
            self.p3.y -= col
            self.p4.y -= col
            vy = math.sin(self.p1.vel.angle) * self.p1.vel.mag
            vyvec = vector()
            vyvec.mag = (1+restitution) * vy
            vyvec.angle = -math.pi/2
            self.p1.vel = vectadd(self.p1.vel, vyvec)
            # friction
            vx = math.cos(self.p1.vel.angle) * self.p1.vel.mag
            vxfric = vector()
            vxfric.mag = vx * friction
            vxfric.angle = math.pi
            self.p1.vel = vectadd(self.p1.vel, vxfric)
            
        
        if self.p2.y > floorHeight:
            col = self.p2.y - floorHeight
            self.p1.y -= col
            self.p2.y -= col
            self.p3.y -= col
            self.p4.y -= col
            vy = math.sin(self.p2.vel.angle) * self.p2.vel.mag
            vyvec = vector()
            vyvec.mag = (1+restitution) * vy
            vyvec.angle = -math.pi/2
            self.p2.vel = vectadd(self.p2.vel, vyvec)
            # friction
            vx = math.cos(self.p2.vel.angle) * self.p2.vel.mag
            vxfric = vector()
            vxfric.mag = vx * friction
            vxfric.angle = math.pi
            self.p2.vel = vectadd(self.p2.vel, vxfric)
        
        if self.p3.y > floorHeight:
            col = self.p3.y - floorHeight
            self.p1.y -= col
            self.p2.y -= col
            self.p3.y -= col
            self.p4.y -= col
            vy = math.sin(self.p3.vel.angle) * self.p3.vel.mag
            vyvec = vector()
            vyvec.mag = (1+restitution) * vy
            vyvec.angle = -math.pi/2
            self.p3.vel = vectadd(self.p3.vel, vyvec)
            # friction
            vx = math.cos(self.p3.vel.angle) * self.p3.vel.mag
            vxfric = vector()
            vxfric.mag = vx * friction
            vxfric.angle = math.pi
            self.p3.vel = vectadd(self.p3.vel, vxfric)
        
        if self.p4.y > floorHeight:
            col = self.p4.y - floorHeight
            self.p1.y -= col
            self.p2.y -= col
            self.p3.y -= col
            self.p4.y -= col
            vy = math.sin(self.p4.vel.angle) * self.p4.vel.mag
            vyvec = vector()
            vyvec.mag = (1+restitution) * vy
            vyvec.angle = -math.pi/2
            self.p4.vel = vectadd(self.p4.vel, vyvec)
            # friction
            vx = math.cos(self.p4.vel.angle) * self.p4.vel.mag
            vxfric = vector()
            vxfric.mag = vx * friction
            vxfric.angle = math.pi
            self.p4.vel = vectadd(self.p4.vel, vxfric)

class shape:
    def __init__(self, vertlst):
        self.verts = vertlst
        self.lenlst = [] #p0,p1  p0,p2  p0,p3.... p1,p2 p1,p3....
        for a in range(len(self.verts)):
            for b in range(len(self.verts)):
                if a == b:
                    pass
                self.lenlst.append(norm(self.verts[a].x-self.verts[b].x, self.verts[a].y-self.verts[b].y))
    def draw(self):
        for p in range(len(self.verts)):
            pg.draw.circle(screen, black, (self.verts[p].x, self.verts[p].y), 3)
            if p > 0:
                pg.draw.line(screen, black, (self.verts[p-1].x,self.verts[p-1].y), (self.verts[p].x,self.verts[p].y), 2)
            else:
                pg.draw.line(screen, black, (self.verts[-1].x, self.verts[-1].y), (self.verts[p].x, self.verts[p].y), 2)
    
    def lenadj(self, elastic, efficiency):
        t = 0
        for a in range(len(self.verts)):
            for b in range(len(self.verts)):
                if a == b:
                    pass
                self.verts[a], self.verts[b] = correctlen(self.verts[a], self.verts[b], self.lenlst[t], elastic, efficiency)
                t += 1

    def bounce(self, fh):
        for p in self.verts:
            if p.y > fh:
                p.y = fh
                bvec = vector()
                bvec.angle = -math.pi/2
                bvec.mag = 1*p.vel.mag
                p.vel = vectadd(p.vel, bvec)

    def move(self):
        for p in self.verts:
            p = step(p, p.vel)

    def grav(self,G):
        for p in self.verts:
            p.vel = vectadd(p.vel,G)
    
    def run(self, G, floorHeight, elasticity, loss):
        self.lenadj(elasticity, loss)
        self.grav(G)
        self.bounce(floorHeight)
        self.move()


G = vector()
G.angle = math.pi/2
G.mag = 0.003
fh = height

#sq = square()
vl = []
p1 = point()
p2 = point()
p3 = point()
p4 = point()
p1.x,p1.y = 400,400
p2.x,p2.y = 450,400
p3.x,p3.y = 450,450
p4.x,p4.y = 400,450
vl.append(p1)
vl.append(p2)
vl.append(p3)
vl.append(p4)
test = shape(vl)

shapelst = []
shapelst.append(test)

editing = False

frame = -1
running = True
while running:
    frame += 1
    mx, my = pg.mouse.get_pos()
    m1,m3,m2 = pg.mouse.get_pressed()
    
    # key inputs #
    keys = pg.key.get_pressed()
    ke = (keys[pg.K_e])
    if ke == True and pke == False:
        editing = bool(((editing-0.5)*-1) + 0.5)
        if editing == True:
            tempvl = []
        if editing == False:
            i = shape(tempvl)
            print(i)
            shapelst.append(i)
    ####
    

    if editing == True:
        pg.draw.circle(screen, black, (mx,my), 3)
        for p in range(len(tempvl)):
            pg.draw.circle(screen, black, (tempvl[p].x, tempvl[p].y), 3)
            if p > 0:
                pg.draw.line(screen, black, (tempvl[p].x, tempvl[p].y), (tempvl[p-1].x, tempvl[p-1].y), 2)
        if len(tempvl) > 0:
            pg.draw.line(screen, (150,150,150), (mx,my), (tempvl[0].x, tempvl[0].y), 2)
        if len(tempvl) > 1:
            pg.draw.line(screen, black, (mx,my), (tempvl[-1].x, tempvl[-1].y), 2)

        if m1 and pm1 == False:
            p = point()
            p.x = mx
            p.y = my
            tempvl.append(p)



    for s in shapelst:
        if editing == False:
            s.run(G, fh, 0.0005, 0.02)
        s.draw()

    """
        sq.lenadj()
        sq.grav(G)

        if sq.p1.y > fh or sq.p2.y > fh or sq.p3.y > fh or sq.p4.y > fh:
            sq.bounce(fh,3,0.6)
        sq.move()
    sq.draw()
    """

    pm1 = m1
    pke = ke
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(sky)