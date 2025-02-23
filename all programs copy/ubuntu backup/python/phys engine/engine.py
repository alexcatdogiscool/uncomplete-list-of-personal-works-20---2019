import pygame as pg
import funcs
import ball
import math
import cv2
import pyautogui as pag
import numpy as np
import random


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

def draw(x,y,r,c):
    pg.draw.circle(screen, c, (x,y), r)


radius = 5
balls = []
ballsize = 0
for i in range(ballsize):
    num = i
    i = ball.ball()
    i.x = random.randint(0,width)
    i.y = random.randint(0,height)
    i.a = random.uniform(0,2*math.pi)
    i.v = random.uniform(0,5)
    i.rad = radius


    balls.append(i)

G = 0.0

global_v = 0
global_a = 0

m1p,m2p,m3p = 0,0,0
setva = False
square = False
circle = False
frame = 0
baking = False
running = True
while running:
    m1,m3,m2 = pg.mouse.get_pressed()
    mx,my = pg.mouse.get_pos()


    if (m1 == 1 and m2 == 1) and (m1p == 0 or m2p == 0):
        setva = True
        sgvax, sgvay = mx,my



    if m3 == 1 and m3p == 0:
        baking = ((baking-0.5) *-1) + 0.5


    for b1 in balls:
        draw(b1.x, b1.y, b1.rad, red)
        if baking == True:
            b1.a,b1.v = funcs.vectadd(b1.a,b1.v,math.pi/2,G)
            b1.a,b1.v,b1.x,b1.y = funcs.bounds(b1.x,b1.y,b1.a,b1.v,b1.e,b1.rad,width,height)
            for b2 in balls:
                hit = funcs.lqcoll(b1.x,b1.y,b1.rad, b2.x,b2.y,b2.rad)
                if hit == True:
                    hit = funcs.hqcoll(b1.x,b1.y,b1.rad, b2.x,b2.y,b2.rad)
                if hit == True:
                    b1.a,b1.v,b1.x,b1.y, b2.a,b2.v,b2.x,b2.y = funcs.bounce(b1.x,b1.y,b1.a,b1.v,b1.mass,b1.rad, b2.x,b2.y,b2.a,b2.v,b2.mass,b1.rad)
            b1.step()
            
            #image = np.array(pag.screenshot())
            #cv2.imwrite('frames//{0}.png'.format(frame), image)
            frame += 1


    if m1 == 1 and m1p == 0 and m2 == 0 and m2p == 0:
        ssx, ssy = mx,my
        square = True
    
    if m2 == 1 and m2p == 0 and m1 == 0 and m1p == 0:
        scx,scy = mx,my
        circle = True

    if square == True:
        if m1 == 1:
            w = mx-ssx
            h = my-ssy
            xbs = int(w/(2*radius))
            ybs = int(h/(2*radius))
            for y in range(ybs):
                for x in range(xbs):
                    draw(2*x*radius+ssx+radius+(2*x),2*y*radius+ssy+radius+(2*y),radius,red)
            pg.draw.rect(screen, black, (ssx,ssy, w, h), 1)
        else:
            for y in range(ybs):
                for x in range(xbs):
                    i = ball.ball()
                    i.x = 2*x*radius+ssx+radius+(2*x)
                    i.y = 2*y*radius+ssy+radius+(2*y)
                    i.rad = radius
                    i.a = global_a
                    i.v = global_v
                    balls.append(i)
            square = False

    if circle == True:
        if m2 == 1:
            r = int(funcs.pythag(scx,scy,mx,my))
            pg.draw.circle(screen, black, (scx,scy), r, 1)
            ps = int(((math.pi*r**2) / (math.pi*radius**2))*0.6)
            for n in range(ps):
                x,y = funcs.circlegen(scx,scy,r,radius,ps,n+1)
                draw(x,y,radius,red)
        else:
            for n in range(ps):
                x,y = funcs.circlegen(scx,scy,r,radius,ps,n+1)
                i = ball.ball()
                i.x, i.y = x,y
                i.rad = radius
                i.a = global_a
                i.v = global_v
                balls.append(i)
                circle = False

    if setva == True:
        pg.draw.line(screen, black, (sgvax,sgvay), (mx,my))
        if m1 == 0 and m2 == 0:
            setva = False
            global_a = math.atan2(my-sgvay,mx-sgvax)
            global_v = funcs.pythag(sgvax,sgvay, mx,my) / 100




    m1p,m2p,m3p = m1,m2,m3
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(sky)