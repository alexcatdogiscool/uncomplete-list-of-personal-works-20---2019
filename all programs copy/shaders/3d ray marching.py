import numpy as np
import math
import random
from PIL import Image
import os
import cv2
random.seed(1)

def radtodeg(x):
    return x * 180/math.pi

def degtorad(x):
    return x * math.pi/180

def findangle(startx, starty, startz, end):
    xdist = abs(startx - end[0])
    ydist = abs(starty - end[1])
    zdist = abs(startz - end[2])

    hangle = np.arctan(ydist / xdist)

    xydist = math.sqrt(xdist**2 + ydist**2)

    vangle = np.arctan(zdist/xydist)

    return hangle, vangle

def nonlin(val):
    a = 2.7

    return (val**a)/(val**a) + (1-val)**a



image_folder = 'output imagees'
videoname = '3d raymarching.avi'




class ray:
    def __init__(self):
        #self.p = np.array([0,0,0,1])

        self.x = 0
        self.y = 0
        self.z = 0


        self.hangle = 0
        self.vangle = 0

        self.r = 100
        self.g = 100
        self.b = 100

        self.shading = False

        self.hit = False

        self.inlight = False


    def move(self, stepsize):
        ystep = stepsize * (np.sin(self.vangle))

        val = stepsize * np.cos(self.vangle)

        xstep = val * np.sin(self.hangle)

        zstep = val * np.cos(self.hangle)

        #trans = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[xstep, ystep, zstep, 1]])

        self.x += xstep
        self.y += ystep
        self.z += zstep

        r.r += 3
        r.g += 3
        r.b += 3
            



class sphere:
    def __init__(self):
        self.radius = random.uniform(4, 20)
        self.p = np.array([random.uniform(0,110),random.uniform(0,110),random.uniform(40, 100),1])
        #self.p = np.array([0,0,50,1])
        
        self.r = random.uniform(0,255)
        self.g = random.uniform(1,255)
        self.b = random.uniform(2,255)

        self.xbobrate = random.uniform(1, 10)
        self.xbobamount = random.uniform(0.1, 1)

        self.ybobrate = random.uniform(1, 10)
        self.ybobamount = random.uniform(0.1, 1)




class light:
    def __init__(self):
        self.p = np.array([0,0,-100,1])

        self.bright = 1

        self.xbobrate = random.uniform(1, 10)
        self.xbobamount = random.uniform(0.1, 1)

        self.ybobrate = random.uniform(1, 10)
        self.ybobamount = random.uniform(0.1, 1)




rays = []
raysize = 40000
for r in range(raysize):
    r = ray()
    r.hangle = degtorad(0)
    r.vangle = degtorad(0)
    rays.append(r)


sphs = []
spheresize = 4
for s in range(spheresize):
    s = sphere()
    sphs.append(s)


lights = []
lightsize = 1
for l in range(lightsize):
    l = light()
    lights.append(l)




hcamrange = 90
vcamrange = 90

hanglestep = hcamrange*raysize**0.5/(raysize-raysize**0.5)
vanglestep = vcamrange*raysize**0.5/(raysize-raysize**0.5)


starthangle = -45
startvangle = 45

count = 0
for r in rays:
    count += 1
    r.hangle = degtorad(starthangle)
    r.vangle = degtorad(startvangle)
    starthangle += hanglestep
    if count == raysize**0.5:
        starthangle = -45
        startvangle -= vanglestep
        count = 0


#for i in range(12):
 #   for s in sphs:
  #      #s.p[0] -= np.sin(i*s.xbobamount)*s.xbobrate
   #     #s.p[1] -= np.cos(i*s.ybobamount)*s.ybobrate
    #    s.p[0] += i*0.5
     #   break

px = 65
py = 23
pz = 40




dists = []

frame = 0
running = True
for epoch in range(10):
    frame += 1
    print(frame)


    rays = []
    for r in range(raysize):
        r = ray()
        
        r.x = px
        r.y = py
        r.z = pz
        
        r.hangle = degtorad(0)
        r.vangle = degtorad(0)
        rays.append(r)


    pz += 5
    

        

    starthangle = -45 - frame*6
    startvangle = 45 - frame*1.5
    
    count = 0
    for r in rays:
        count += 1
        r.hangle = degtorad(starthangle)
        r.vangle = degtorad(startvangle)
        starthangle += hanglestep
        if count == raysize**0.5:
            starthangle = -45 - frame*6
            startvangle -= vanglestep
            count = 0



    ######## raycast #######

    for r in rays:
        while r.hit == False:
            
            for s in sphs:
                dist = ((abs(r.x - s.p[0])**2 + abs(r.y - s.p[1])**2 + abs(r.z - s.p[2])**2)**0.5) - s.radius
                dists.append(dist)
                dists.sort()

                if dist < 0.1:
                    r.hit = True
                    r.shading = True

                    r.r = s.r
                    r.g = s.g
                    r.b = s.b

            dist = dists[0]
            dists = []
            #print(r.p)
            r.move(dist)

            if dist > 500:
                r.hit = True

    ###### shade ########


    for r in rays:
        while r.shading == True:
            for l in lights:
                r.hangle, r.vangle = findangle(r.x, r.x, r.z, l.p)

            for s in sphs:
                dist = ((abs(r.x - s.p[0])**2 + abs(r.y - s.p[1])**2 + abs(r.z - s.p[2])**2)**0.5) - s.radius
                dists.append(dist)
                dists.sort()

            dist = dists[0]
            dists = []
            r.move(1)
            

            for s in sphs:
                dist = ((abs(r.x - s.p[0])**2 + abs(r.y - s.p[1])**2 + abs(r.z - s.p[2])**2)**0.5) - s.radius
                dists.append(dist)
                dists.sort()

            dist = dists[0]
            dists = []

            

            if dist < 0:
                r.shading = False

                r.r *= (abs(dist)-1)*-1
                r.g *= (abs(dist)-1)*-1
                r.b *= (abs(dist)-1)*-1

                #r.r = 0
                #r.g = 0
                #r.b = 0

                pass

            if dist > 0:
                r.shading = False

                r.r += 100*dist
                r.g += 100*dist
                r.b += 100*dist

                if r.r > 255:
                    r.r = 255

                if r.g > 255:
                    r.g = 255

                if r.b > 255:
                    r.b = 255
                


    for s in sphs:
        #s.p[0] -= np.sin(frame*s.xbobamount)*s.xbobrate
        #s.p[1] -= np.cos(frame*s.ybobamount)*s.ybobrate
        #s.p[0] += frame*0.5
        pass





    

    imarr = np.array(0)

    for r in rays:
        imarr = np.append(imarr, (r.r, r.g, r.b))

    imarr = np.delete(imarr, 0)
    

    data = np.array(imarr, dtype=np.uint8)
    data = data.reshape(int(raysize**0.5), int(raysize**0.5), 3)

    img = Image.fromarray(data)
    img.save('output imagees/{0}.png'.format(frame))




    


images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(videoname, 0, 3, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()





for s in sphs:
    print(s.r, s.g, s.b)





