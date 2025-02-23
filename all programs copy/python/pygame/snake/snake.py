import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from PIL import Image

pygame.init()

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

        
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (255,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (255,0,0), circleMiddle2, radius)
        



class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)
        

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

        
sss = 5, 5
itter =+ 1
diceRoll = random.randrange(0, 5)
score = 7
width = 500
height = 600


win = pygame.display.set_mode((width, height))

def message(msg, x, y, size):
    font = pygame.font.SysFont(None, size)
    txt = font.render(str(msg), True, (0, 128, 0))
    win.blit(txt, (x, y))


def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
#    drawGrid(width,rows, surface)
    message('score ', 0, 500, 32)
    message(len(s.body), 0, 550, 32)
    message(itter, 250, 6500, 32)
    message(s.body[0].pos[0]*25-50, 255, 500, 32)
    message(500 - s.body[0].pos[0]*25-50, 255, 550, 32)
    
    pygame.display.update()
    



    


def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack
    width = 500
    height = 600
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))
    snack = cube(randomSnack(rows, s), color=(0,255,0))
    flag = True



    clock = pygame.time.Clock()

    multi = 10

    
    while flag:

        
        for event in pygame.event.get():
            mult = pygame.key.get_pressed()
            for key in mult:
                if mult[pygame.K_COMMA]:
                    multi =+ 1
            for key in mult:
                if mult[pygame.K_PERIOD]:
                    multi =- 1


        
        pygame.time.delay(25)
        clock.tick(10)
        s.move()
        
        
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0,255,0))

        

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                itter =+ 1
                print('itterations: ', itter)
                message_box('You Lost!', 'Play again...')
                s.reset((10,10))
                break

        
        
        



        Oposx = s.body[0].pos[0]*25-50
        Oposy = s.body[0].pos[1]*25-50
        
        redrawWindow(win)

        if Oposx > 0:
            if Oposy > 0:
   
                if Oposx < 375:
            
                    if Oposy < 375:
                        rect = pygame.Rect((Oposx, Oposy, 125, 125))
                    else:
                        rect = pygame.Rect((Oposx, Oposy - Oposy + 375, 125, 125))

                else:
                    if Oposy > 0:
                        if Oposy < 375:
                            rect = pygame.Rect((Oposx-Oposx+375, Oposy, 125, 125))
                        else:
                            rect = pygame.Rect(((Oposx)-(Oposx)+375, Oposy-(Oposy)+375, 125, 125))
                    else:
                        rect = pygame.Rect(((Oposx)-(Oposx)+375, Oposy-(Oposy), 125, 125))

            else:
                if Oposx < 375:
                    rect = pygame.Rect(((Oposx), Oposy-(Oposy), 125, 125))
                else:
                     rect = pygame.Rect(((Oposx)-Oposx+375, Oposy-(Oposy), 125, 125))
        else:
            if Oposy > 0:
                if Oposy < 375:
                    rect = pygame.Rect(((Oposx)-(Oposx), Oposy, 125, 125))
                else:
                    rect = pygame.Rect(((Oposx)-(Oposx), Oposy-Oposy+375, 125, 125))
            else:
                rect = pygame.Rect(((Oposx)-(Oposx), Oposy-Oposy, 125, 125))

        
        
#        rect = pygame.Rect(s.body[0].pos[0]*25-50, s.body[0].pos[1]*25-50, 125, 125)
        sub = win.subsurface(rect)
        pygame.image.save(sub, "ss.png")       
        im = Image.open("ss.png")
        sslq = im.resize(sss, Image.ANTIALIAS)
        sslq.save("sslq.jpg", "PNG")

        
        


main()
