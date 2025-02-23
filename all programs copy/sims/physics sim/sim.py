import math
import pygame as pg
import random

def norm(a,b):
    return (a*a + b*b)**0.5

def vectadd(v1t, v1a, v2t, v2a, loss):
    v1x = v1a * math.cos(v1t)
    v1y = v1a * math.sin(v1t)
    v2x = v2a * math.cos(v2t)
    v2y = v2a * math.sin(v2t)
    v3x = v1x + v2x
    v3y = v1y + v2y
    v3t = math.atan2(v3y,v3x)
    v3a = norm(v3x, v3y) * loss
    return v3t, v3a

def chkcoll(x1,y1,r1, x2,y2,r2):
    rads = r1 + r2
    if abs(x1 - x2) > rads+5 and abs(y1 - y2) > rads+5:
        return False, 0
    else:
        dst = norm(x1-x2, y1-y2)
        
        if dst < rads and dst > 0:
            overlap = dst - rads
            return True, overlap
        else:
            return False, 0
    

width = 800
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (158, 228, 255)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


class ball:
    def __init__(self):
        self.id = 0
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.v = random.uniform(0,1)
        self.a = random.uniform(0, 2*math.pi)
        self.m = 1
        self.rad = 10
        self.p = self.m * self.v
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    def step(self):
        self.x += self.v * math.cos(self.a)
        self.y += self.v * math.sin(self.a)
        self.p = self.m * abs(self.v)
        if self.y > height - self.rad:
            vy = self.v * math.sin(self.a)
            self.a, self.v = vectadd(self.a, self.v, -math.pi/2, 2*vy, 0.9)
            self.y -= 1
        if self.y < 0:
            self.a *= -1
            self.y += 1
        if self.x > width - self.rad:
            vx = self.v * math.cos(self.a)
            self.a, self.v = vectadd(self.a, self.v, math.pi, 2*vx, 0.9)
            self.x -= 1
        if self.x < 0 + self.rad:
            vx = abs(self.v * math.cos(self.a))
            self.a, self.v = vectadd(self.a, self.v, 0, 2*vx, 0.9)
            self.x += 1
    def reflect(self, cx,cy, loss):
        xd = cx - self.x
        yd = cy - self.y
        atc = math.atan2(yd,xd)
        tangent = atc + (math.pi/2)
        self.a = (tangent - self.a) + tangent
        self.p *= loss

    def draw(self):
        pg.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.rad)


ballsize = 200
balls = []
for i in range(ballsize):
    num = i
    i = ball()
    i.id = num
    balls.append(i)


g = 0.00

mcount = 0
running = True
while running:
    mx, my = pg.mouse.get_pos()
    m1, m2, m3 = pg.mouse.get_pressed()
    mcount += m1
    if mcount == 100:
        for i in range(1):
            num = i
            i = ball()
            i.id = num
            i.x = mx
            i.y = my
            balls.append(i)
            mcount = 0

    for b in balls:
        b.a, b.v = vectadd(b.a,b.v, math.pi/2, g, 1)
        b.step()
        b.draw()

    for b in balls:
        for d in balls:
            coll = chkcoll(b.x,b.y,b.rad, d.x,d.y,d.rad)
            if coll[0] == True:
                d.reflect(b.x,b.y, 1)
                pshare = (b.p + d.p)/2
                b.v = pshare/b.m
                d.v = pshare/d.m
                b.step()
                d.step()
                b.x -= coll[1]
                #b.y -= coll[1]







    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False