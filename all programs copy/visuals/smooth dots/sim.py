import pygame as pg
import math
import numpy as np
import random

def norm(a,b):
    return math.sqrt(a*a + b*b)

def boarder(arr, dots):
    for r in range(len(arr[:,0])):
        for c in range(len(arr[0,:])):
            for d in dots:
                dst = norm(c-d.x, r-d.y)
                n = math.log(dst+0.01)/40
                arr[r,c] += n
    return arr > 1
    
def drawField(arr):
    for r in range(len(arr[:,0])):
        for c in range(len(arr[0,:])):
            if arr[r,c]:
                pg.draw.rect(screen, black, (c,r, 1,1))



width = 200
height = 200

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = white

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()



class dot:
    def __init__(self):
        self.x = 0
        self.y = 0
    def draw(self):
        pg.draw.circle(screen, red, (self.x, self.y), 3)

dots = []
for i in range(10):
    i = dot()
    i.x = random.randint(0, width)
    i.y = random.randint(0, height)
    dots.append(i)




field = np.zeros((height, width))

running = True
while running:
    mx,my = pg.mouse.get_pos()
    dots[0].x, dots[0].y = mx,my

    field = boarder(field, dots)
    drawField(field)


    for d in dots:
        d.draw()



    field = np.zeros((height, width))
    pg.display.flip()
    screen.fill(sky)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False  