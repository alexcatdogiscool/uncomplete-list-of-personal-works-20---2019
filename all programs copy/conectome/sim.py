import pygame as pg
import numpy as np
import math
import random
import funcs
import objects as objs


width = 400
height = 400

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (158, 228, 255)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()

brainSize = 60

worms = []
wormSize = 100
for i in range(wormSize):
    i = objs.worm(brainSize, 200,200)
    worms.append(i)

boardScale = 8

gens = 1000

fitnesses = []

clock = pg.time.Clock()

for gen in range(gens):
    print(gen)
    fitnesses = []
    for n, w in enumerate(worms):
        board = np.random.uniform(size=(height//boardScale, width//boardScale))
        #print(n)
        for i in range(500):

            #funcs.drawBoard(screen, board, boardScale)

            board = w.output(board, boardScale)
            w.updateSenses(board, boardScale)
            w.updateBrain()
            
            #w.draw(screen)

            #pg.display.flip()
            #screen.fill(sky)
        fitnesses.append(w.hunger)
        #print("fitness = ", w.hunger)

    wo = worms[fitnesses.index(max(fitnesses))]
    
    print(wo.hunger)
    worms = funcs.makeNewGen(wo, wormSize, brainSize)




#print(max(fitnesses))
#print(fitnesses.index(max(fitnesses)))
wo = worms[fitnesses.index(max(fitnesses))]
weights = wo.weights
w = objs.worm(brainSize,200,200)
w.weights = weights

np.save('brain.npy', weights)
#weights = np.load

#input("press any key to continue")

board = np.random.uniform(size=(height//boardScale, width//boardScale))
for i in range(5000):
    clock.tick(30)

    funcs.drawBoard(screen, board, boardScale)

    board = w.output(board, boardScale)
    w.updateSenses(board, boardScale)
    w.updateBrain()

    #print(w.hunger)
    
    w.draw(screen)

    pg.display.flip()
    screen.fill(sky)
