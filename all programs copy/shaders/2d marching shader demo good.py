import random
import math
import numpy as np
import pygame as pg
import time
from PIL import Image
import cv2
import os

random.seed(1)

sky = (0,0,0)
white = (255,255,255)

image_folder = 'output imagees'
videoname = 'video.avi'

width, height = 600, 600

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()

def rad(x):
    return x * math.pi/180


class ray:
    def __init__(self):
        self.ogx = 0
        self.ogy = 300
        
        self.x = self.ogx
        self.y = self.ogy
        self.stepsize = 0
        self.anglereal = 65
        self.angle = rad(180 - (random.uniform(45, 135)))

        self.r = 0
        self.g = 0
        self.b = 0

        self.stepping = True

    def step(self, dist):
        self.stepsize = dist
        self.x += self.stepsize*math.sin(self.angle)
        self.y += self.stepsize*math.cos(self.angle)

        self.r += 5
        self.g += 5
        self.b += 5

        if self.r > 255:
            self.r = 255

        if self.g > 255:
            self.g = 255

        if self.b > 255:
            self.b = 255
        

    def draw(self):
        #pg.draw.line(screen, white, (self.ogx, self.ogy), (self.x, self.y), 1)
        #pg.draw.circle(screen, (0,255,0), (self.ogx, self.ogy), 5)
        pass

class sphere:
    def __init__(self):
        self.x = random.randint(200,600)
        self.y = random.randint(0,600)
        self.radius = np.random.randint(5, 25)

        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)

        self.distance = 100

        self.bobamount = random.uniform(1,10)
        self.bobspeed = random.uniform(1,10)

    def draw(self):
        pg.draw.circle(screen, (self.r, self.g, self.b), (self.x, self.y), self.radius, 1)
        pass

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.r = 0
        self.r = 0
        self.r = 0

    def draw(self):
        pg.draw.rect(screen, (self.r, self.g, self.b), (self.x, self.y, 1, 1))
        
        

rays = []
raysize = 1000
for i in range(raysize):
    i = ray()
    rays.append(i)

objs = []
objsize = 10
for i in range(objsize):
    i = sphere()
    objs.append(i)


points = []
pointsize = 0
for i in range(pointsize):
    i = point()
    points.append(i)



camrange = 90

anglestep = camrange/(raysize-1)

startangle = 45

for r in rays:
    r.angle = rad(180 - startangle)
    startangle += anglestep




rays = []


dist = 10

dists = []

frame = 0
running = True
for epoch in range(60):
    frame += 1
    #print(frame)

    
    

    for i in range(raysize):
        i = ray()
        i.ogx = 0
        rays.append(i)





        

    startangle = 45
    #startangle += (math.sin(frame/4))*0
    camrange -= 0

    anglestep = camrange/(raysize-1)

    for r in rays:
        r.angle = rad(180 - startangle)
        startangle += anglestep


    


    

    

    for p in points:
        p.draw()

    for o in objs:
        o.y += math.sin(frame/o.bobspeed)*o.bobamount
        o.y = int(o.y)
        o.draw()

    

    


    
    for r in rays:
        while r.stepping == True:

            for o in objs:
                dist = math.sqrt((r.x - o.x)**2 + (r.y - o.y)**2) - o.radius
                o.distance = dist
                dists.append(dist)
                dists.sort()
                
            dist = dists[0]
            #pg.draw.circle(screen, white, (int(r.x), int(r.y)), int(dist+1), 1)
            r.step(dist)
            r.draw()
            dists = []

            if dist > 600:
                r.stepping = False
                pass
                
            if dist < 0.1:
                r.stepping = False
                objs.sort(key=lambda x: x.distance, reverse=False)
                for o in objs:
                    r.r = o.r
                    r.g = o.g
                    r.b = o.b
                    break

                
                for p in range(1):
                    p = point(r.x, r.y)
                    
                    p.r = r.r
                    p.g = r.g
                    p.b = r.b
                    
                    points.append(p)




    dist = 100

    for r in rays:
        r.x = r.ogx
        r.y = r.ogy
        #r.angle -= rad(5)


    for o in objs:
        o.y += 0

    
    


    pg.display.flip()
    screen.fill(sky)

    points = []

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False

    





    imgarr = np.array(0)

    for r in rays:
        imgarr = np.append(imgarr, (r.r, r.g, r.b))

    imgarr = np.delete(imgarr, 0)

    data = np.array(imgarr, dtype=np.uint8)
    data = data.reshape(raysize,1,3)

    for i in range(8):
        data = np.append(data, data, 1)

    img = Image.fromarray(data)
    img.save('output imagees/{0}.png'.format(frame))

    rays = []

    time.sleep(0.0)


images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(videoname, 0, 6, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()



