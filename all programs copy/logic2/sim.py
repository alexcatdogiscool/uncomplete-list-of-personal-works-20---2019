import numpy as np
import math
import pygame as pg
import objects as objs
import funcs




width = 700
height = 700

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (60,60,60)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()


resolution = 0.1


grid = funcs.createGrid(int(height*resolution), int(width*resolution))

#for k in grid:
 #   for j in k:
  #      j.tileType = 2

comp = 1
copy = False

m2pre = 0
m1pre = 0
clock = pg.time.Clock()
running = True
while running:
    #clock.tick(30)
    m1,m3,m2 = pg.mouse.get_pressed()
    mx,my = pg.mouse.get_pos()
    keys = pg.key.get_pressed()

    if keys[pg.K_t]:
        comp = 5
    if keys[pg.K_n]:
        comp = 4
    if keys[pg.K_w]:
        comp = 1
    if keys[pg.K_LCTRL] and keys[pg.K_c]:
        copy = True
        reigon = [None,None,None,None]

    

    if m1 and not copy:
        grid[int(my*resolution)][int(mx*resolution)].tileType = comp
    if m2pre and not m2:
        grid[int(my*resolution)][int(mx*resolution)].tileType = 3
    if m2:
        grid[int(my*resolution)][int(mx*resolution)].tileType = 2
    if keys[pg.K_ESCAPE]:
        grid[int(my*resolution)][int(mx*resolution)].tileType = 0
    

    
    grid = funcs.drawGrid(screen, grid, resolution)


    if copy:
        tempGrid = funcs.createGrid(int(height*resolution), int(width*resolution))
        if reigon[2] == None and reigon[0] != None:
            pg.draw.rect(screen, (255,0,0), (reigon[0]//resolution, reigon[1]//resolution, (int(mx*resolution+1)-reigon[0])//resolution, (int(my*resolution+1)-reigon[1])//resolution), 1)
        if reigon[0] != None and reigon[2] != None:
            tempGrid = funcs.pasteGrid(tempGrid, tempCopy, [int(mx*resolution), int(my*resolution)])
            funcs.drawGrid(screen, tempGrid, resolution)
            if m1 and not m1pre:
                copy = False
                grid = funcs.pasteGrid(grid, tempCopy, [int(mx*resolution), int(my*resolution)])
        if m1 and not m1pre:
            if reigon[0] == None:
                reigon[0] = int(mx*resolution)
                reigon[1] = int(my*resolution)
            else:
                reigon[2] = int(mx*resolution)+1
                reigon[3] = int(my*resolution)+1
                tempCopy = funcs.copyGrid(grid, reigon)
        


    m1pre = m1
    m2pre = m2

    pg.display.flip()
    screen.fill(sky)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False
