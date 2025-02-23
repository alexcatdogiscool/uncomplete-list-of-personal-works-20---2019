import pygame as pg
import math
import random
random.seed(3)

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


class emiter:
    def __init__(self):
        self.clock = 0

        self.x = 0
        self.y = 0
        self.v = 0
        self.a = 0
        self.ea = 0
        self.ev = 1


        self.rate = 1#per frame
    def step(self):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v 
    def emit(self, waterLst):
        i = water()
        i.x = self.x
        i.y = self.y
        i.a = self.ea
        i.v = self.ev
        waterLst.append(i)
    def draw(self):
        pg.draw.circle(screen, black, (self.x, self.y), 10)

class water:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
        self.v = 0
    def step(self):
        self.x += math.cos(self.a) * self.v
        self.y += math.sin(self.a) * self.v
    def draw(self):
        pg.draw.circle(screen, blue, (self.x, self.y), 5)
    def die(self):
        if abs(self.x) > width:
            return True
        elif abs(self.y) > height:
            return True
        else:
            return False


wat = []
em = []
for i in range(3):
    num = i
    i = emiter()
    i.x = random.randint(0,width)
    i.y = random.randint(0,height)
    i.a = 2.0944 * num
    em.append(i)

an = 0
am = 0
running = True
while running:
    m1,m3,m2 = pg.mouse.get_pressed()

    if m1 == 1:
        am += 0.001
    if m2 == 1:
        am -= 0.001

    an += am
    for e in em:
        e.x = (math.cos(e.a+an) * 200) + 400
        e.y = (math.sin(e.a+an) * 200) + 400

        e.draw()
        e.emit(wat)
        e.ea = e.a+an+math.pi

    t = 0
    for w in wat:
        w.step()
        w.draw()
        if w.die() == True:
            del wat[t]

        t += 1




    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(sky)