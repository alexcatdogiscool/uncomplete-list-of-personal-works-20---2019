import pygame as pg
import math
import bird
import wall
import random
import numpy as np

width, height = 800,800
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
birdCol = (217, 211, 50)
wallCol = (41, 194, 46)
sky = (60, 207, 240)

screen = pg.display.set_mode((width,height))
screen.fill(sky)
pg.display.flip()


def DrawBird(lst):
    for b in lst:
        pg.draw.circle(screen, birdCol, (b.x,b.y), 10)

def DrawWall(lst):
    for w in lst:
        pg.draw.rect(screen, wallCol, (w.x, height-w.height, 50, w.height))
        pg.draw.rect(screen, wallCol, (w.x, 0, 50, height-(w.height+90)))
        



birds = []

gensize = 100

for i in range(gensize):
    i = bird.bird()
    birds.append(i)
walls = []
for i in range(1):
        i = wall.wall()
        walls.append(i)




g = 0.01

maxMaxFit = 0
generations = 100
gens = -1
while True:
    gens += 1
    running = True
    while running:



        
        t = 0
        for w in walls:
            if w.x < -50:
                del walls[t]
            if w.x == 500:
                i = wall.wall()
                walls.append(i)
            w.move()
            t += 1
        
        
        aliveNum = 0
        for b in birds:
            dst = 1000
            h = 0
            maxScore = 0
            for w in walls:
                if b.score > maxScore:
                    maxScore = b.score
                if b.x >= w.x and not b.x > w.x+50:
                    if b.y > height-w.height:
                        b.alive = False
                    if b.y < height-(w.height+90):
                        b.alive = False
                if b.x == w.x + 50:
                    if b.score == maxScore:
                        print(b.score+1)
                    b.score += 1
                if w.x - 250 < dst:
                    dst = w.x - 250
                    h = height-w.height
            if b.y >= height:
                b.alive = False
            if b.y <= 0:
                b.alive = False
            if b.alive == True:
                aliveNum += 1
            b.think(dst/550, h/800)
            b.phys(g)
        if aliveNum == 0:
            running = False





        DrawWall(walls)
        DrawBird(birds)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()
        screen.fill(sky)



    w1 = 0
    w2 = 0
    b1 = 0
    b2 = 0
    maxFit = 0
    for b in birds:
        if b.fitness > maxFit:
            maxFit = b.fitness
            w1 = b.weights1
            w2 = b.weights2
            b1 = b.bias1
            b2 = b.bias2
    if maxFit > maxMaxFit:
        maxMaxFit = maxFit
        np.save('w1.npz', w1)
        np.save('w2.npz', w2)
        np.save('b1.npz', b1)
        np.save('b2.npz', b2)
    print(maxFit)
    birds = []
    walls = []
    walls = []
    for i in range(1):
        i = wall.wall()
        walls.append(i)


    for i in range(gensize):
        i = bird.bird()
        wso = w1
        wst = w2
        #wso[random.randint(0,3), random.randint(0,4)] += random.uniform(-0.3,0.3)
        #wst[random.randint(0,4), random.randint(0,1)] += random.uniform(-0.3,0.3)
        i.weights1 = np.random.rand(4,5)
        i.weights2 = np.random.rand(5,2)
        i.bias1 = b1
        i.bias2 = b2
        birds.append(i)
        
    print(gens)

