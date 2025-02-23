import gates as g
import pygame as pg

width = 800
height = 600
screen = pg.display.set_mode((width, height))


ior = pg.image.load('sprites\\or.png')
iand = pg.image.load('sprites\\and.png')
inor = pg.image.load('sprites\\nor.png')
inand = pg.image.load('sprites\\nand.png')
ixor = pg.image.load('sprites\\xor.png')
ixnor = pg.image.load('sprites\\xnor.png')
inot = pg.image.load('sprites\\not.png')


class gate:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.o = 0
        self.t = 0
        self.out = 0

        self.gate = 'OR'

    def think(self):
        if self.gate == 'OR':
            self.out = g.OR(self.o, self.t)
        if self.gate == 'AND':
            self.out = g.AND(self.o, self.t)
        if self.gate == 'NOR':
            self.out = g.NOR(self.o, self.t)
        if self.gate == 'NAND':
            self.out = g.NAND(self.o, self.t)
        if self.gate == 'XOR':
            self.out = g.XOR(self.o, self.t)
        if self.gate == 'XNOR':
            self.out = g.XNOR(self.o, self.t)
        if self.gate == 'NOT':
            self.out = g.NOT(self.o, self.t)

    def draw(self):
        if self.gate == 'OR':
            screen.blit(ior,(self.x,self.y))
        if self.gate == 'AND':
            screen.blit(iand,(self.x,self.y))
        if self.gate == 'NOR':
            screen.blit(inor ,(self.x,self.y))
        if self.gate == 'NAND':
            screen.blit(inand ,(self.x,self.y))
        if self.gate == 'XOR':
            screen.blit(ixor ,(self.x,self.y))
        if self.gate == 'XNOR':
            screen.blit(ixnor ,(self.x,self.y))
        if self.gate == 'NOT':
            screen.blit(inot ,(self.x,self.y))
        

