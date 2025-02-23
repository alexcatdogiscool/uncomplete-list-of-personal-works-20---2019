import pygame as pg
import numpy as np
import math
import shapes
import funcs
import camera
import random





width = 800
height = 800

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (190,190,190)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(sky)
pg.display.flip()




p = []
p.append(shapes.point(-0.50,-0.50,-0.50))
p.append(shapes.point(0.50,-0.50,-0.50))
p.append(shapes.point(-0.50,0.50,-0.50))
p.append(shapes.point(0.50,0.50,-0.50))
p.append(shapes.point(-0.50,-0.50,0.50))
p.append(shapes.point(0.50,-0.50,0.50))
p.append(shapes.point(-0.50,0.50,0.50))
p.append(shapes.point(0.50,0.50,0.50))

l = []
l.append([2,0,1])
l.append([1,3,2])
l.append([4,6,7])
l.append([4,5,7])
l.append([0,4,6])
l.append([0,2,6])
l.append([3,1,5])
l.append([3,7,5])
l.append([1,0,4])
l.append([1,5,4])
l.append([3,2,6])
l.append([6,7,3])


shapelst = []

for i in range(30):
    i = shapes.obj(random.randint(-5,5), random.randint(-5,5), random.randint(-5,5), p,l)
    shapelst.append(i)




cam = camera.camera((7*math.pi)/18, width, height)


running = True
while running:
    m1,m3,m2 = pg.mouse.get_pressed()
    keys=pg.key.get_pressed()
    if keys[pg.K_a]:
        cam.z -= math.sin(cam.az) * 0.03
        cam.x -= math.cos(cam.az) * 0.03
    if keys[pg.K_d]:#would have cam.az + math.pi/2, but thats the same as swapping cos and sin
        cam.z += math.sin(cam.az) * 0.03
        cam.x += math.cos(cam.az) * 0.03
    if keys[pg.K_w]:
        cam.z += math.cos(-cam.az) * 0.03
        cam.x += math.sin(-cam.az) * 0.03
    if keys[pg.K_s]:
        cam.z -= math.cos(-cam.az) * 0.03
        cam.x -= math.sin(-cam.az) * 0.03

    if keys[pg.K_LSHIFT]:
        cam.y += 0.03
    if keys[pg.K_SPACE]:
        cam.y -= 0.03

    if keys[pg.K_LEFT]:
        cam.az += 0.004
    if keys[pg.K_RIGHT]:
        cam.az -= 0.004
    if keys[pg.K_UP]:
        cam.el += 0.004
    if keys[pg.K_DOWN]:
        cam.el -= 0.004
        


    cam.render(screen, shapelst)

    #s.draw(screen, width, height, (7*math.pi)/18)








    pg.display.flip()
    screen.fill(sky)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False