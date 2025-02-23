import pygame as pg
import math
import random
import time

random.seed(1)

def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5

def pull(dst, pom,ptm):
    return (G*pom*ptm)/(dst**2)



width = 1200
height = 800

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


class point:
    def __init__(self):
        self.x = random.uniform(0,width)
        self.y = random.uniform(0,height)
        self.mass = 10
        self.speed = 0
        self.direction = 0

        self.poop = False

        self.player = False

        self.size = 5
        self.a = 0

        self.trace = False

    def step(self, dst, angle):
        self.x += math.cos(angle) * dst
        self.y += math.sin(angle) * dst
        
    def draw(self, zoomf):
        if self.player == False:
            pg.draw.circle(screen, white, (int(self.x*zoomf), int(self.y*zoomf)), int(self.size*zoomf))
        else:
            pg.draw.circle(screen, (240,200,60), (int(self.x*zoomf), int(self.y*zoomf)), int(self.size*zoomf))
            pg.draw.line(screen, (240,200,60), (int(self.x*zoomf), int(self.y*zoomf)), (int(self.x+math.cos(self.a)*10)*zoomf, int(self.y+math.sin(self.a)*10)*zoomf))
    def dring(self, zoomf):
        if self.poop == True:
            #rad = ((G*((self.mass * 10)/0.0005))**0.5)/3
            #pg.draw.circle(screen, white, (int(self.x*zoomf), int(self.y*zoomf)), int(rad*zoom), 1)
            pass


points = []
pointsize = 5
for i in range(pointsize):
    num = i
    i = point()

    if num == 0:
        i.player = True
        i.x = 1530
        i.y = 0
        i.speed = 0.14915 + 0.6674
        i.direction = math.pi/2
        i.mass = 10

    if num == 1:
        i.size = 10
        i.mass = 10000000000
        i.x = 1500
        i.y = 0
        i.speed = 0.6674
        i.direction = math.pi/2
        i.poop = True
    if num == 2:
        i.mass = 10000000000000
        i.size = 300
        i.x = 0
        i.y = 0
        i.poop = True
    if num == 3:
        i.size = 10
        i.mass = 10000000000
        i.x = 3000
        i.y = 0
        i.speed = 0.4719
        i.direction = math.pi/2
        i.poop = True

    if num == 4:
        i.mass = 0.000001
        i.trace = True
        i.size = 2
    
    points.append(i)


G = 0.00000000006674
zoom = 0.3

speed = 0
direction = 0

running = True
while running:

    keys = pg.key.get_pressed()

    for p in points:
        p.draw(zoom)
        if p.poop == True:
            p.dring(zoom)
        tempx = p.x
        tempy = p.y
        for pt in points:
            dist = pythag(p.x,p.y, pt.x,pt.y)
            if dist > 1 and pt.trace != True:
                force = pull(dist, p.mass, pt.mass)
                angle = math.atan2((pt.y-p.y), (pt.x-p.x))
                #if dist < pt.size:
                 #   p.step(force/p.mass, angle + math.pi)
                  #  p.step(p.speed, p.direction + math.pi)
                p.step(force/p.mass, angle)

        p.step(p.speed, p.direction)
        

        if p.player == True:
            if keys[pg.K_SPACE]:
                p.step(0.0005, p.a)
            if keys[pg.K_RIGHT]:
                p.a += 0.01
            if keys[pg.K_LEFT]:
                p.a -= 0.01


        ################### EVERYTHING BEFORE THIS ###############
        p.speed = pythag(tempx,tempy, p.x,p.y)
        p.direction = math.atan2((p.y-tempy), (p.x-tempx))





    if keys[pg.K_p]:
        zoom /= 1.01
    if keys[pg.K_m]:
        zoom *= 1.01


    #time.sleep(1)

    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
