import pygame as pg
import math
import random
import time



def pythag(sx,sy, ex,ey):
    return ((sx-ex)**2 + (sy-ey)**2)**0.5



width = 800
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


class arm:
    def __init__(self):
        self.x = 400
        self.y = 350
        self.ex = self.x
        self.len = 300
        self.ey = self.y + self.len        
        self.mass = 10
        self.friction = 1.001
        self.v = -0.05
        self.a = math.pi/2
    
    def draw(self):
        pg.draw.line(screen, black, (self.x, self.y), (int(self.ex), int(self.ey)), 5)

    def step(self):
        self.ex = (math.sin(self.a) * self.len) + self.x
        self.ey = (math.cos(self.a) * self.len) + self.y



armsize = 1
arms = []
for i in range(armsize):
    i = arm()
    arms.append(i)




running = True
while running:


    for a in arms:
        a.step()
        a.v -= math.sin(a.a)/10000
        a.v /= a.friction
        a.a += a.v
        a.draw()







    pg.display.flip()
    screen.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
