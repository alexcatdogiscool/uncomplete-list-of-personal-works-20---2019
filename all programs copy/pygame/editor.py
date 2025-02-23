import pygame as pg
import numpy as np
import math
import time
import random

background_colour = (255,255,255)
(width, height) = (900, 600)

black = (0,0,0)

mousepos = (0,0)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('cool editor')
screen.fill(background_colour)

pg.display.flip()

click = 0

class rect:
    def __init__(self):
        self.x, self.y = mousepos
        self.sizex = 10
        self.sizey = 10
        self.mass = 100
        
    
        #self.colour = (random.randint(10, 255),random.randint(10, 255),random.randint(10, 255))
        self.colour = black
        

        self.xvel = 0.0
        self.yvel = 1.0

        self.prex = self.x
        self.prey = self.y

        self.bouncy = 0.5
        self.friction = 0.998

        self.onground = False
        self.onwall = False

        self.grabbed = False


    def run(self):
        pg.draw.rect(screen, self.colour, (int(self.x), int(self.y), self.sizex, self.sizey),1)
        self.yvel += gravityy
        self.xvel += gravityx
        self.x += self.xvel
        self.y += self.yvel


        ###### bouncy ########
        if self.y > height - self.sizey:
            self.y = height - self.sizey
            self.yvel *= self.bouncy
            self.yvel *= -1

        if self.y < 0:
            self.y = 0
            self.yvel *= self.bouncy
            self.yvel *= -1



        if self.x > width - self.sizex:
            self.x = width - self.sizex
            self.xvel *= self.bouncy
            self.xvel *= -1
            

        if self.x < 0:
            self.x = 0
            self.xvel *= self.bouncy
            self.xvel *= -1

        ####### friction #######

        if self.y > height - self.sizey - 1:
            self.onground = True
        else:
            self.onground = False

        if self.y < 1:
            self.onground = True
        else:
            self.ongrounf = False

            
        if self.onground == True:
            self.xvel *= self.friction

            



        if self.x > width - self.sizex - 1:
            self.onwall = True
            self.yvel *= self.friction
        else:
            self.onground = False

        if self.x < 1:
            self.onwall = True
            self.yvel *= self.friction
        else:
            self.onwall = False
            

        #if self.onwall == True:
        #    self.yvel *= self.friction

        ########## GRAB ############

        if leftclick == 1:
            if mouseposx > self.x:
                if mouseposx < self.x + self.sizex:
                    if mouseposy > self.y:
                        if mouseposy < self.y + self.sizey:
                            self.x = mouseposx - self.sizex/2
                            self.y = mouseposy - self.sizey/2
                            self.grabbed = True

        else:
            self.grabbed = False

        ###### prev vel #######

        if leftclick == 1:
            if self.grabbed == True:
                self.xvel = (self.x - self.prex)/5
                self.yvel = (self.y - self.prey)/5
                print("yes")

        
        
        self.prex = self.x
        self.prey = self.y



tempmouseposx = 0
tempmouseposy = 0

r = rect()
rects = []

gravityy = 0.00
gravityx = 0.00

circle = 0

x = 200
y = 200

running = True
while running:
    
    pg.display.flip()
    screen.fill(background_colour)
    
    mousepos = pg.mouse.get_pos()
    mouseposx, mouseposy = pg.mouse.get_pos()
    leftclick, midleclick, rightclick = pg.mouse.get_pressed()

    if leftclick == 1:
        if click == 0:
            print("click")
            click = 1
            tempmouseposx, tempmouseposy = pg.mouse.get_pos()

        pg.draw.rect(screen, (255,0,0), (tempmouseposx, tempmouseposy, mouseposx - tempmouseposx,mouseposy-tempmouseposy),1)
        pg.draw.line(screen, (255,0,0), (tempmouseposx, tempmouseposy), (mouseposx, mouseposy))
    
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            if leftclick == 1:
                print("up")
                r = rect()
                tempsizex, tempsizey = pg.mouse.get_pos()

                sizex = tempmouseposx - tempsizex
                sizey = tempmouseposy - tempsizey

                r.sizex = abs(sizex)
                r.sizey = abs(sizey)

                r.x = tempmouseposx
                r.y = tempmouseposy

                r.mass = r.x * r.y

                r.vely = 0
                r.velx = 0
            
                rects.append(r)
            

    if leftclick == 0:
        click = 0

    
                    
                
    y = (math.sin(circle) * 40) + height/2
    x = (math.cos(circle) * 40) + width/2

    gravityx = (math.cos(circle) / 500)
    gravityy = (math.sin(circle) / 500)
    #print(y)
                
    
    pg.draw.line(screen, black, (width/2, height/2), (x, y))


    
    
    circle += 0.0001
            


    ##### run #######
    for i in rects:
        i.run()
        #print(i.onwall)




    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

    time.sleep(0.00)

    
