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




class point:
    def __init__(self):
        self.x = width/2
        self.y = height/2

        self.id = 0

        self.a = 0
        self.dst = 0

    def draw(self, nth):
        if self.id % nth == 0:
            pg.draw.circle(screen, (240,200,60), (int(self.x), int(self.y)),3)
        else:
            pg.draw.circle(screen, (50,50,50), (int(self.x), int(self.y)),3)
    def high(self, pid):
        if self.id == pid:
            pg.draw.circle(screen, (240,200,60), (int(self.x), int(self.y)),3)

class slider:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.id = 0
        self.value = 0
    def draw(self):
        pass



mult = (1+math.sqrt(5))/2
#mult = 0.5
nth = 1000000000
power = 1
light = 0
pointsize = 1

frame = -1
running = True
while running:
    frame += 1

    #mult = 1.61803398875
    #mult += 0.000003
    #nth += 13
    power += 0.001
    #light += 1

    points = []
    pointsize = 600
    for i in range(int(pointsize)):
        num = i
        i = point()
        i.id = num
        i.a = 2*math.pi*mult*num
        if power > 0:
            i.dst = ((num/(pointsize-1))**power)*350
        if power < 0:
            i.dst = (1/(1+(num/(pointsize-1))**abs(power)))*350
        points.append(i)

    for p in points:
        p.x = (math.cos(p.a) * p.dst) + width/2
        p.y = (math.sin(p.a) * p.dst) + height/2
        p.draw(int(nth))
        p.high(light)

    pg.draw.circle(screen, white, (400,400), 350, 1)
    #pg.draw.line(screen,white, (points[frame].x,points[frame].y),(points[frame+1].x,points[frame+1].y))


    #time.sleep(0.1)






    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
