import math
import pygame as pg
import time
import numpy as np
import cv2

def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5


def circle(x,y, cx,cy,rad):
    return pythag(x,y,cx,cy) - rad


def box(x,y, bx,by,br):
    br /=2
    #norm(max(abs(x - c) - r,0))
    xm = max(abs(x-bx)-br,0)
    ym = max(abs(y-by)-br,0)

    return (xm**2 + ym**2)**0.5


def shadow(x):
    return 1/(1+(100000000000**(-x + 0.01)))


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



class ray:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
        self.b = 30
        self.hit = False
        self.reflects = 0
        self.mina = 10
        self.light = False
        self.totaldst = 1
        self.rsteps = 0
    def step(self, dst):
        if self.hit != True:
            self.x += math.cos(self.a) * dst
            self.y += math.sin(self.a) * dst


class circ:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 80
    def draw(self):
        pg.draw.circle(screen, white, (self.x, self.y),self.r)


class square:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 50
    def draw(self):
        pg.draw.rect(screen, white, (self.x-(self.r/2), self.y-(self.r/2), self.r, self.r))

class light:
    def __init__(self):
        self.x = 0
        self.y = 0
    def draw(self):
        pg.draw.circle(screen, (255,255,0), (self.x, self.y), 10)


res = 100
fov = math.pi/2
looking = -0.2

astep = fov/(res+1)

rays = []
for i in range(res):
    num = i
    i = ray()
    i.y = 300

    i.a = ((-fov)/2) + ((num+1)*astep) + looking

    rays.append(i)


circs = []
for i in range(1):
    i = circ()
    i.x = 300
    i.y = 300
    circs.append(i)

boxes = []
for i in range(1):
    i = square()
    i.r = 20
    i.x = 220
    i.y = 200
    boxes.append(i)

lights = []
for i in range(1):
    i = light()
    i.x = 100
    i.y = 100
    lights.append(i)


toll = 0.2

frame = 0
running = True
while running:
    frame += 1
    if frame == 50:
        running = False


    for r in rays:
        dst = 1000
        ox = r.x
        oy = r.y
        for c in circs:
            temp = circle(r.x, r.y, c.x, c.y, c.r) - 0.1
            dst = min(temp, dst)
        for b in boxes:
            temp = box(r.x,r.y, b.x,b.y,b.r)
            dst = min(temp, dst)
        if r.reflects > 0:
            r.rsteps += 1
            r.totaldst += dst
            r.mina = min(r.mina, math.atan(dst/r.totaldst)+r.a)
            for l in lights:
                ltemp = circle(r.x,r.y, l.x,l.y,10)
                dst = min(dst, ltemp)
        if dst < toll:
            if r.reflects > 0:
                if ltemp < 51:
                    r.light = True
                    if r.hit != True:
                        r.b += 255
                r.hit = True
            r.reflects += 1
            for l in lights:
                r.a = math.atan2(l.y-r.y,l.x-r.x)# + (math.pi/2)
                r.step(toll)
        #print(r.a)
        r.step(dst)
        pg.draw.line(screen, white, (ox,oy), (r.x,r.y),2)

    

    for c in circs:
        c.draw()

    for b in boxes:
        b.draw()

    for l in lights:
        l.draw()



    pg.display.flip()
    screen.fill(black)

    time.sleep(0.1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False

img = []
for r in rays:
    if r.reflects == 0:
        r.b = 0
    if r.light == False and r.reflects > 0:
        r.b = 30
    if r.light == True:
        r.b = 255 - (r.rsteps*3)
    img.append(r.b)

img = np.array(img)
print(img)
img = img.reshape(1,res)

cv2.imwrite('2dout.png', img)