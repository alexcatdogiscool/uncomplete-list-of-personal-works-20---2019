import math
import pygame as pg
import random
import time

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



class node:
    def __init__(self):
        self.id = 0
        self.ke = 0.8
        self.n, self.ne, self.e, self.se, self.s, self.sw, self.w, self.nw = 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8
        self.edge = False
    def draw(self):
        x,y = node.fpos(self)
        c = abs(int(self.ke * 51))
        pg.draw.rect(screen, (c,c,c), (x*mult,y*mult, int(mult), int(mult)))
    def fpos(self):
        num = self.id/(reswidth)
        y = int(num)
        x = (num - y)*reswidth
        return int(round(x)),int(round(y))

reswidth = 20
mult = (width/reswidth)
nodes = []
for i in range(reswidth**2):
    num = i
    i = node()
    i.id = num

    x,y = i.fpos()
    if y == 0 or y == reswidth-1 or x == 0 or x == reswidth-1:
        i.edge = True
        #i.ke = 0

    nodes.append(i)


pm1,pm2,pm3 = 0,0,0
sel = 0
running = True
while running:
    m1,m2,m3 = pg.mouse.get_pressed()

    

    if m1-pm1 ==1:
        sel += 1

    for n in nodes:
        if n.id == 210:
            if m1 == 1:
                n.ke += 1

        if n.edge != True:
            bke = n.ke
            n.ke -= (n.ke * n.n) - (nodes[n.id-reswidth].ke * (nodes[n.id-reswidth].s))
            nke = n.ke
            n.ke -= (n.ke * n.ne) - (nodes[(n.id-reswidth)+1].ke * (nodes[(n.id-reswidth)+1].sw))
            neke = n.ke
            n.ke -= (n.ke * n.e) - (nodes[n.id+1].ke * (nodes[n.id+1].w))
            eke = n.ke
            n.ke -= (n.ke * n.se) - (nodes[n.id+reswidth+1].ke * (nodes[n.id-reswidth+1].nw))
            seke = n.ke
            n.ke -= (n.ke * n.s) - (nodes[n.id+reswidth].ke * (nodes[n.id+reswidth].n))
            ske = n.ke
            n.ke -= (n.ke * n.sw) - (nodes[(n.id+reswidth)-1].ke * (nodes[(n.id+reswidth)-1].ne))
            swke = n.ke
            n.ke -= (n.ke * n.w) - (nodes[n.id-1].ke * (nodes[n.id-1].e))
            wke = n.ke
            n.ke -= (n.ke * n.nw) - (nodes[(n.id-reswidth)-1].ke * (nodes[(n.id-reswidth)-1].se))
            nwke = n.ke
            netke = n.ke

            pn = nke - bke
            pne = neke - nke
            pe = eke - neke
            pse = seke - eke
            ps = ske - seke
            psw = swke - ske
            pw = wke - swke
            pnw = nwke - wke
            
            n.n = nke / netke/4
            n.ne = neke / netke/4
            n.e = eke / netke/4
            n.se = seke / netke/4
            n.s = ske / netke/4
            n.sw = swke / netke/4
            n.w = wke / netke/4
            n.nw = nwke / netke/4

            #print(n.n + n.ne + n.e+n.se+n.s+n.sw+n.w+n.nw)
            

    for n in nodes:
        n.draw()



    #time.sleep(0.1)





    pm1,pm2,pm3 = m1,m2,m3
    pg.display.flip()
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False