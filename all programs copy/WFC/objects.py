from importlib.resources import path
import pygame as pg
import numpy as np
import cv2
import funcs

class cols:
    def __init__(self):
        width = 1000
        height = 700

        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        green = (0,255,0)
        sky = (35,35,35)


class ScreenObject:
    def __init__(self, width, height, sky, title):
        self.width = width
        self.height = height

        self.sky = sky

        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        self.screen.fill(self.sky)
        pg.display.flip()


        
class HomeScreen:
    def __init__(self, width, height, sky, title):
        self.screen_object = ScreenObject(width, height, sky, title)

    def update(self):

        pg.display.flip()
        self.screen_object.screen.fill(self.screen_object.sky)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
    
    def quit(self):
        pg.quit()



class button:
    def __init__(self, x, y, width, height, colour, LableInfo, IsToggle):
        """
        LableInfo = (text, font, font_size, colour)
        """
        self.width = width
        self.height = height
        self.colour = colour
        self.IsToggle = IsToggle
        ButtonText = LableInfo[0]
        font = LableInfo[1]
        size = LableInfo[2]
        TextColour = LableInfo[3]
        
        self.text = text(ButtonText, font, size, TextColour)
        self.TextWidth, self.TextHeight = self.text.img.get_size()

        self.x = x
        self.y = y

    def render(self, surface):
        pg.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height))
        posX = int(((self.width - self.TextWidth)/2) + self.x)
        posY = int(((self.height - self.TextHeight)/2) + self.y)
        
        self.text.display(surface, (posX, posY))

    def ClickCheck(self):
        mx, my = pg.mouse.get_pos()
        m1,m3,m2 = pg.mouse.get_pressed()
        
        if m1:
            if mx > self.x and mx < self.x + self.width and my > self.y and my < self.y + self.height:
                return True
        return False






class text:
    def __init__(self, text, font, size, colour):
        pg.font.init()

        self.FontClass = pg.font.SysFont(font, size)
        self.img = self.FontClass.render(text, True, colour)
    
    def display(self, surface, position):
        surface.blit(self.img, position)


class TileTypeTable:
    def __init__(self):

        self.TypeTable = []


class wfcImg:
    def __init__(self, rows, cols, rules):
        #self.TileImg = np.zeros((rows,cols))
        self.TileImg = funcs.newWF((rows,cols), len(rules)-1)
        self.img = np.zeros((rows, cols,3))
        self.oldArr = funcs.newWF((rows,cols), len(rules)-1)

    def WFcollapseStep(self, rules):
        #rows, cols = self.TileImg.shape
        #self.TileImg = funcs.WFC(self.TileImg, rules, (rows,cols))

        #make 2s array of entropys for each index
        #collapse tile with lowest entropy
        #propogate the collapse to the whole array
        #check if entire wf has collapsed:
        # return wf if true
        #eles:
        # go to step 1

        #while checkIfCollapsed(wf) == False:
        entropy = funcs.getEntropy(self.TileImg, rules)
        self.TileImg = funcs.WFcollapse(self.TileImg, entropy)
        return self.TileImg
    
    def propogate(self, rules):
        self.oldArr, self.TileImg = funcs.propogate(self.TileImg, rules)
        
    
    def RenderImg(self, TileTypes):
        for r in range(self.TileImg.shape[0]):
            for c in range(self.TileImg.shape[1]):
                col = TileTypes.TypeTable[self.TileImg[r,c][0]]
                if len(self.TileImg[r,c]) > 1:
                    col = (255,0,255)
                self.img[r,c,2] = col[0]
                self.img[r,c,1] = col[1]
                self.img[r,c,0] = col[2]
                
                
                
    def SaveImg(self, img_path):
        cv2.imwrite(img_path + "source.png",  self.img)

    def display(self, surface, position, size):
        img = pg.image.load("source.png")
        img = pg.transform.scale(img, (int(size[0]), int(size[1])))
        surface.blit(img, position)


