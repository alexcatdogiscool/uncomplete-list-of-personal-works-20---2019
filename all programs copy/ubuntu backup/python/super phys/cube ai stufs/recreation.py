import pygame as pg
import numpy as np
import math



def step(point, vec):
    point.x += math.cos(vec.angle) * vec.mag
    point.y += math.sin(vec.angle) * vec.mag
    return point


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
        self.mag = 0
        self.angle = 0

class point:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.vel = vector()

class square:
    def __init__(self):
        self.p1 = point()
        self.p2 = point()
        self.p3 = point()
        self.p4 = point()

    def draw(self):
        pg.draw.circle(screen, black, (self.p1.x, self.p1.y), 5)
        pg.draw.circle(screen, black, (self.p2.x, self.p2.y), 5)
        pg.draw.circle(screen, black, (self.p3.x, self.p3.y), 5)
        pg.draw.circle(screen, black, (self.p4.x, self.p4.y), 5)

        pg.draw.line(screen, black, (self.p1.x, self.p1.y), (self.p2.x,self.p2.y), 2)
        pg.draw.line(screen, black, (self.p2.x, self.p2.y), (self.p3.x,self.p3.y), 2)
        pg.draw.line(screen, black, (self.p3.x, self.p3.y), (self.p4.x,self.p4.y), 2)
        pg.draw.line(screen, black, (self.p4.x, self.p4.y), (self.p1.x,self.p1.y), 2)

    def move(self):
        self.p1 = step(self.p1, self.p1.vel)
        self.p2 = step(self.p2, self.p2.vel)
        self.p3 = step(self.p3, self.p3.vel)
        self.p4 = step(self.p4, self.p4.vel)


sq = square()

data = np.load('data.npz')['outs']
print(data.shape)


frame = -1
running = True
while running:
    frame += 1

    sq.p1.vel.angle = data[0,frame,4599]
    sq.p1.vel.mag = data[1,frame,4599]

    sq.p2.vel.angle = data[2,frame,4599]
    sq.p2.vel.mag = data[3,frame,4599]

    sq.p3.vel.angle = data[4,frame,4599]
    sq.p3.vel.mag = data[5,frame,4599]

    sq.p4.vel.angle = data[6,frame,4599]
    sq.p4.vel.mag = data[7,frame,4599]

    sq.move()
    sq.draw()












    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(sky)