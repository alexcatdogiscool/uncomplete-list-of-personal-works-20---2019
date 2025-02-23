import pygame as pg
import math
import random
import time



def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5



width = 600
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()




class circle:
    def __init__(self):
        self.id = 0
        self.x = 300
        self.y = 300

        self. rad = 70
    def draw(self):
        pg.draw.circle(screen, white, (self.x, self.y), self.rad)



class ray:
    def __init__(self):
        self.x = 0
        self.y = 300
        self.a = 0
    def step(self, dst):
        self.x += math.cos(self.a) * dst
        self.y += math.sin(self.a) * dst

    def reflect(self, cx,cy):
        xd = cx - self.x
        yd = cy - self.y
        atc = math.atan(yd/xd)
        tangent = atc + (math.pi/2)
        self.a = (tangent - self.a) + tangent


cs = []
for i in range(1):
    num = i
    i = circle()
    i.id = num
    cs.append(i)


rays = []
for i in range(1):
    i = ray()
    rays.append(i)

iters = 20
frame = 0
running = True
while running:
    frame += 1


    for r in rays:
        #r.y += math.sin(frame/100) * 300
        for i in range(iters):
            dst = 1000
            for c in cs:
                temp = pythag(r.x, r.y, c.x, c.y) - c.rad
                if temp < dst:
                    dst = temp
                    cid = c.id

            if dst < 0.2:
                #print("hit")
                r.reflect(300, 300)
                r.step(0.2)
                #r.a = math.pi + 0.1
                #r.step(0.2)

            ox = r.x
            oy = r.y
            r.step(dst)
            #pg.draw.circle(screen, white, (int(ox), int(oy)), int(dst+2), 1)
            pg.draw.line(screen, white, (int(ox), int(oy)), (int(r.x), int(r.y)), 1)

    for c in cs:
        c.draw()
    mx, my = pg.mouse.get_pos()
    for r in rays:
        r.x = 0
        r.y = my#math.sin(frame/10000) * 300 + 300
        r.a = math.pi/8



    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False    
