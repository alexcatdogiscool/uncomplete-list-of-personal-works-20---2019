import pygame as pg
import random
import math


def pythag(sx, ex, sy, ey):
    return math.sqrt((sx-ex)**2 + (sy-ey)**2)


width = 600
height = 660

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(white)
pg.display.flip()



class node:
    def __init__(self):
        self.id = 0
        
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.xrate = random.uniform(0,5)
        self.yrate = random.uniform(0,5)
        
    def draw(self):
        pg.draw.circle(screen, black, (int(self.x), int(self.y)), 10)


num = 0
nodesize = 50
nodes = []
for i in range(nodesize):
    num = i
    i = node()
    i.id = num
    nodes.append(i)



frame = 0
running = True
while running:
    frame += 0.01


    for n in nodes:
        n.draw()

    for n in nodes:
        if n.id == 0:
            n.x, n.y = pg.mouse.get_pos()
        for m in nodes:
            temp = pythag(n.x, m.x, n.y, m.y)
            if temp < 100 and temp > 1:
                pg.draw.line(screen, black, (int(n.x),int(n.y)), (int(m.x),int(m.y)),2)
        n.x += math.sin(frame*n.xrate)
        n.y += math.cos(frame*n.yrate)



    pg.display.flip()
    screen.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
