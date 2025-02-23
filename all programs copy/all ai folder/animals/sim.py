import numpy as np
import math
import animal
import time
import pygame as pg
import food
import functions as func


width = 800
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (78, 148, 21)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()


startpop = 100
animals = []
for i in range(startpop):
    i = animal.animal()
    animals.append(i)

foodsize = 10
foods = []
for i in range(foodsize):
    num = i
    i = food.food()
    i.id = num
    foods.append(i)


running = True
while running:


    for f in foods:
        f.grow()
        f.draw()

    for a in animals:
        dst = 1000
        t = 0
        for a2 in animals:
            temp = func.norm(a.x-a2.x, a.y-a2.y)
            if temp < dst and temp > 0:
                dst = temp
                t = 0
                x, y = a2.x, a2.y
                colour = a2.colour
        for f in foods:
            temp = func.norm(a.x-f.x, a.y-f.y)
            if temp < dst and temp > 0:
                dst = temp
                t = 1
                x,y = f.x,f.y
                colour = (55, 102, 16)
                ident = f.id
        angle = func.angleto(a.x,a.y, x,y)
        a.brain[0] = angle/(2*math.pi)
        a.brain[1] = t
        
        a.brain[2] = colour[0]/255
        a.brain[3] = colour[1]/255
        a.brain[4] = colour[2]/255

        if t == 1:
            if dst < 15:
                foods[ident].eat(a.eating)
                a.health += foods[ident].size / 5

    for a in animals:
        if a.birthing == 1 and a.health > 0.7 and a.age > 1000 and a.kids < 1:
            for i in range(1):
                a.kids += 1
                i = animal.animal()
                i.x = a.x
                i.y = a.y
                i.health = 0.3
                a.health -= 0.5
                i.weights, i.bias = a.birth()
                animals.append(i)

    num = 0
    for a in animals:
        if a.health < 0:
            del animals[num]
        num += 1

    for a in animals:
        a.age += 1
        a.think()
        a.step()
        a.draw()









    pg.display.flip()
    screen.fill(sky)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False