import objects as objs
import pygame as pg




def createGrid(rows, cols):
    grid = [[objs.tile(0) for j in range(cols+1)] for i in range(rows+1)]
    return grid

def drawGrid(surface, grid, resolution):
    height = len(grid)-1
    width = len(grid[0])-1

    newGrid = createGrid(height, width)

    for y in range(height):
        for x in range(width):
            tile = grid[y][x]

            up = grid[y-1][x]
            down = grid[y+1][x]
            left = grid[y][x-1]
            right = grid[y][x+1]

            newGrid[y][x].tileType = grid[y][x].update(up,down,left,right)
            
            #print(tile.tileType)

            #print(tile.tileType)

            if tile.tileType == 0:
                continue
            if tile.tileType == 1:
                colour = (0,0,0)
            if tile.tileType == 2:
                colour = (255,255,255)
            if tile.tileType == 3:
                colour = (80,80,80)
            if tile.tileType == 4:
                colour = (255,0,0)
            if tile.tileType == 5:
                colour = (0, 189, 31)
            pg.draw.rect(surface, colour, (int(x/resolution), int(y/resolution), int(1/resolution), int(1/resolution)))
    return newGrid


def copyGrid(grid, reigon):
    height = len(grid)-1
    width = len(grid[0])-1

    copy = createGrid(reigon[3]-reigon[1], reigon[2]-reigon[0])

    for y in range(reigon[1], reigon[3], 1):
        for x in range(reigon[0], reigon[2], 1):
            copy[y-reigon[1]][x-reigon[0]] = grid[y][x]
    return copy


def pasteGrid(host, copy, loc):
    copyHeight = len(copy)-1
    copyWidth = len(copy[0])-1


    for y in range(loc[1], loc[1]+copyHeight, 1):
        for x in range(loc[0], loc[0]+copyWidth, 1):
            host[y][x] = copy[y-loc[1]][x-loc[0]]
    return host
            
