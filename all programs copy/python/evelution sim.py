import pygame as py
import numpy as np
import random
import time

(width, height) = (800, 600)
bg_colour = (135, 206, 235)
screen = py.display.set_mode((width, height))

py.display.set_caption("evolution")
screen.fill(bg_colour)

zwidth, zheight = int(width/2), int(height/2)
mposx, mposy = py.mouse.get_pos()
shiftdistx = 0
shiftdisty = 0

img = py.Surface((250, 250), py.SRCALPHA)
imgsmall = py.transform.rotozoom(img, 0, 0.5)


#person variables
speed = 0
health = 100
direction = (2*3.1415926)
#posx = 500
#posy = 500

def sigmoid(x):
    return 1/(1+np.exp(-x))

class person:
    def __init__(self, index, input_layers, output_layers, hidden_neurons1, hidden_neurons2, hidden_neurons3):
        print("Index : %d", index)
        self.colour = (0,0,0)
        self.age = random.randint(1, 80)
        self.health = 100
        self.posx = 500
        self.posy = 500
        self.speedx = random.randint(-5,5)
        self.speedy = random.randint(-5,5)
        self.direction = random.uniform(0, (2*np.pi))
        self.alive = True
        self.fdist = 100

        self.weights = np.random.rand(input_layers, hidden_neurons1)
        self.weights2 = np.random.rand(hidden_neurons1, hidden_neurons2)
        self.weights3 = np.random.rand(hidden_neurons2, hidden_neurons3)
        self.weights4 = np.random.rand(hidden_neurons3, output_layers)
        
        self.bias = np.random.rand(hidden_neurons1)
        self.bias2 = np.random.rand(hidden_neurons2)
        self.bias3 = np.random.rand(hidden_neurons3)
        self.bias4 = np.random.rand(output_layers)
        

        self.weights += random.uniform(-10,10)
        self.weights2 += random.uniform(-10,10)
        self.weights3 += random.uniform(-10,10)
        self.weights4 += random.uniform(-10,10)
        
        self.bias += random.uniform(-10,10)
        self.bias2 += random.uniform(-10,10)
        self.bias3 += random.uniform(-10,10)
        self.bias4 += random.uniform(-10,10)

        

    def myfunc(self):
        self.age += random.randint(1,10)
        print("im getting older", self.age)

    #def per(x,y):
        #posx = x
        #posy = y

    def draw(self):
        
        self.speedx = random.randint(-1,1)
        self.speedy = random.randint(-1,1)
        
        py.draw.circle(screen, (self.colour), (self.posx,self.posy), int(self.health/7))
        posx = (self.posx)/width
        posy = (self.posy)/height
        health = self.health/100


        #Neural Network
        
        input_set = np.array([[posx, posy,self.health]])
        input_set = input_set.reshape(1,3)

        
        

        #feed_forward
        
        z = np.dot(input_set, self.weights) + self.bias
        z = sigmoid(z)
        z2 = np.dot(z,self.weights2) + self.bias2
        z2 = sigmoid(z2)
        z3 = np.dot(z2,self.weights3) + self.bias3
        z3 = sigmoid(z3)
        z4 = np.dot(z3,self.weights4) + self.bias4

        #update position

        red = sigmoid(z4.item(2)) * 255
        green = sigmoid(z4.item(3)) * 255
        blue = sigmoid(z4.item(4)) * 255
        fposx = 0
        fposy = 0
        self.colour = (red,green,blue)
        
        if z4.item(0) < 0:
            fposx = z4.item(0)
            fposx = fposx * -1
        else:
            fposx = z4.item(0)

        if z4.item(1) < 0:
            fposy = z4.item(1)
            fposy = fposy * -1
        else:
            fposy = z4.item(1)

        self.health -= ((fposx + fposy) * 0.01) + 0.01


        self.posx += int(z4.item(0))
        self.posy += int(z4.item(1))
        
        #self.posx, self.posy = py.mouse.get_pos()














        #end of network stuff       

        if self.health < 0:
            self.alive = False
        
        if self.posx > width:
            self.posx = 0

        if self.posy > height:
            self.posy = 0

        if self.posx < 0:
            self.posx = width

        if self.posy < 0:
            self.posy = height



    def eat(self):
        for f in foods:


            a2 = abs(self.posx - f.posx)
            b2 = abs(self.posy - f.posy)


            
            self.fdist = np.sqrt(a2^2 + b2^2)
            #print(self.fdist)
            
            #if self.fdist < f.val:
            if (abs(self.posx - f.posx) < f.val) and (abs(self.posy - f.posy) < f.val):
                if f.alive == True:
                    self.health += 1
                    f.val -= 1






class food:
    def __init__(f, x, y):
        f.val = 5
        f.valp = 0
        f.posx = x
        f.posy = y
        f.alive = True
        

    def draw(f):
        py.draw.circle(screen, (0,0,0), (f.posx, f.posy), abs((f.val)))
        f.valp += 0.02
        if f.valp > 1:
            f.val += 1
            f.valp = 0

        if f.val > 30:
            f.val = 30

        if f.val < 4:
            f.alive = False
            #f.val = 1




timespeed = 0.0


players = []
for i in range (5):
    players.append(person(i,3,5,4,4,5))

foods = []
for i in range (10):
    foods.append(food((random.randint(0,width)), (random.randint(0,height))))

running = True
while running:
    mposx, mposy = py.mouse.get_pos()
    for p in players:
        if p.alive == False:
            foods.append(food(p.posx, p.posy))
            players.remove(p)            
            
        p.draw()
        p.eat()

    for f in foods:
        if f.alive == False:
            foods.remove(f)
        f.draw()




    py.draw.rect(screen, (255,0,0), (mposx - zwidth/2, mposy - zheight/2, zwidth, zheight),7)
    py.display.flip()
    screen.fill(bg_colour)
    
    


    
    




    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            running = False

        keys = py.key.get_pressed()

        for key in keys:
            if keys[py.K_EQUALS]:
                timespeed += 0.0001

            if keys[py.K_MINUS]:
                timespeed -= 0.0001

            if keys[py.K_z]:
                img = py.Surface((250, 250), py.SRCALPHA)
                imgsmall = py.transform.rotozoom(img, 0, 0.5)
                screen.blit(img, (30,30))
                screen.blit(imgsmall, (400,400))
                py.display.flip()


    if timespeed < 0:
        timespeed = 0


    time.sleep(timespeed)
