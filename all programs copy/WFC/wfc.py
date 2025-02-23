import random
from turtle import home
import numpy as np
import pygame as pg
import funcs
import objects as obj
import time
import cv2


#sample_rules = [[[0,2],[0,2],[0,2],[0,2]], [[1,2],[1,2],[1,2],[1,2]], [[0,1,2],[0,1,2],[0,1,2],[0,1,2]]]#random non-adj black dots assuming tiletype 1 is black






TileType = obj.TileTypeTable()

#TileType.TypeTable.append((0,0,0))
#TileType.TypeTable.append((0,255,0))
#TileType.TypeTable.append((0,255,0))
#TileType.TypeTable.append((0,0,255))


rules = funcs.FindRules("sourceOG.png", TileType)
#rules = [[[0,1],[0,2],[0,3],[0,4]], [[0,1],[3],[0,1],[3]], [[3],[0,2],[3],[0,2]], [[3],[3],[3],[3]]]


home_screen = obj.HomeScreen(1000,700, (35,35,35), "Home Screen")


quitButton = obj.button(100,100, 100,50, (255,0,0), ("quit", 'arial', 32, (0,0,0)), False)
regenButton = obj.button(500, 75, 250, 100, (0,255,0), ('Generate Image', 'arial', 24, (0,0,0)), False)
stepButton = obj.button(500, 525, 250, 100, (0,255,0), ('Next Step', 'arial', 24, (0,0,0)), False)


maxWidth = 250

sourceImg = pg.image.load("sourceOG.png")
sourceImg = pg.transform.scale(sourceImg, (int(sourceImg.get_size()[0]*(maxWidth/sourceImg.get_size()[1])), int(sourceImg.get_size()[1]*(maxWidth/sourceImg.get_size()[1]))))

genSize = (50,50)


wfc = obj.wfcImg(genSize[0], genSize[1],rules)




while True:


    home_screen.screen_object.screen.blit(sourceImg, (100, funcs.fromCenter(home_screen.screen_object.height/2, 250)))
    regenButton.render(home_screen.screen_object.screen)
    quitButton.render(home_screen.screen_object.screen)
    stepButton.render(home_screen.screen_object.screen)
    wfc.display(home_screen.screen_object.screen, (500,funcs.fromCenter(home_screen.screen_object.height/2, 250)), (wfc.img.shape[1]*(maxWidth/wfc.img.shape[1]), wfc.img.shape[0]*(maxWidth/wfc.img.shape[1])))

    
    if regenButton.ClickCheck():
        wfc.TileImg = funcs.newWF(genSize, len(rules))
        wfc.TileImg[genSize[0]-1, genSize[1]-1] = [random.randint(0,len(rules)-1)]

    if stepButton.ClickCheck():
        wfc.WFcollapseStep(rules)

        preStates = []
        while True:
            preStates.append(wfc.TileImg)
            wfc.propogate(rules)
            if funcs.arr_in_list(wfc.TileImg, preStates):
                break
            wfc.RenderImg(TileType)
            wfc.SaveImg("")
            wfc.display(home_screen.screen_object.screen, (500,funcs.fromCenter(home_screen.screen_object.height/2, 250)), (wfc.img.shape[1]*(maxWidth/wfc.img.shape[1]), wfc.img.shape[0]*(maxWidth/wfc.img.shape[1])))
            home_screen.screen_object.screen.blit(sourceImg, (100, funcs.fromCenter(home_screen.screen_object.height/2, 250)))
    
            home_screen.update()

    
    


    

    if quitButton.ClickCheck():
        home_screen.quit()
        break



    home_screen.update()


    

