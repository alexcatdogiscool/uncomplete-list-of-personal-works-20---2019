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

def correctlen(p1,p2, length):
    dst = length - norm(p1.x-p2.x, p1.y-p2.y)
    at2 = math.atan2(p1.y-p2.y, p1.x-p2.x)
    at1 = at2 + math.pi

    p1stepvec = vector()
    p1stepvec.angle = at2
    p1stepvec.mag = dst/2
    p2stepvec = vector()
    p2stepvec.angle = at1
    p2stepvec.mag = dst/2
    
    p1 = step(p1, p1stepvec)
    p2 = step(p2, p2stepvec)

    p1.vel = vectadd(p1.vel, p1stepvec)
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



        
        

G = vector()
G.angle = math.pi/2
G.mag = 0.003
fh = height

#test = plane()


frames = 3000
epochs = 4400

### ai infos:   input: digit for each fram, 0 if no collisions, 1 if >= 1 colls, dim=(1,#of_frames,epochs).
###            output: angle and magnatude(angle first) of velocity of each point at each frame, dim=(2,4,#of_frame,epochs) or (8,#of_frames,epochs)
ins = np.zeros((frames,epochs))
outs = np.zeros((8,frames,epochs))



fff = 0

for epoch in range(epochs):
    print(epoch+1)

    sq = square()



    frame = 0
    running = True
    while running:
        frame += 1


        #if frame == 20:
         #   sq.p1.vel.mag = 0
          #  sq.p2.vel.mag = 0
           # sq.p3.vel.mag = 0
            #sq.p4.vel.mag = 0
        
        """
        p1c = groundcol(test.p1, fh)
        p2c = groundcol(test.p2, fh)
        if p1c[0] == True or p2c[0] == True:
            test.bounce(p1c,p2c, 1, 0)
        test.grav(G)
        test.move()
        test.lenadj()
        test.draw()
        """
        
        
        sq.lenadj()
        sq.grav(G)

        outs[0,frame-1,epoch] = sq.p1.vel.angle
        outs[1,frame-1,epoch] = sq.p1.vel.mag
        outs[2,frame-1,epoch] = sq.p2.vel.angle
        outs[3,frame-1,epoch] = sq.p2.vel.mag
        outs[4,frame-1,epoch] = sq.p3.vel.angle
        outs[5,frame-1,epoch] = sq.p3.vel.mag
        outs[6,frame-1,epoch] = sq.p4.vel.angle
        outs[7,frame-1,epoch] = sq.p4.vel.mag

        if sq.p1.y > fh or sq.p2.y > fh or sq.p3.y > fh or sq.p4.y > fh:
            sq.bounce(fh,3,0.6)
            ins[frame-1,epoch] = 1
        sq.move()
        sq.draw()


        if frame == frames:
            running = False










        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()
        screen.fill(sky)
    




np.savez('data3.npz', ins=ins, outs=outs)