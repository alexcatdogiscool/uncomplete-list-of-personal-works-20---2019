import pygame as pg
import numpy as np
import math
import shapes
import funcs
import camera





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

p.append(shapes.point(-50,-50,-50, -50))
p.append(shapes.point(50,-50,-50, -50))
p.append(shapes.point(-50,50,-50, -50))
p.append(shapes.point(50,50,-50, -50))
p.append(shapes.point(-50,-50,50, -50))
p.append(shapes.point(50,-50,50, -50))
p.append(shapes.point(-50,50,50, -50))
p.append(shapes.point(50,50,50, -50))

p.append(shapes.point(-50,-50,-50, 50))
p.append(shapes.point(50,-50,-50, 50))
p.append(shapes.point(-50,50,-50, 50))
p.append(shapes.point(50,50,-50, 50))
p.append(shapes.point(-50,-50,50, 50))
p.append(shapes.point(50,-50,50, 50))
p.append(shapes.point(-50,50,50, 50))
p.append(shapes.point(50,50,50, 50))
#p.append(shapes.point(0,0,0,0))


l = []
l.append([0,1])
l.append([0,2])
l.append([3,1])
l.append([3,2])
l.append([4,5])
l.append([4,6])
l.append([7,5])
l.append([7,6])
l.append([0,4])
l.append([1,5])
l.append([2,6])
l.append([3,7])

l.append([8,9])
l.append([8,10])
l.append([11,9])
l.append([11,10])
l.append([12,13])
l.append([12,14])
l.append([15,13])
l.append([15,14])
l.append([8,12])
l.append([9,13])
l.append([10,14])
l.append([11,15])

l.append([0,8])
l.append([1,9])
l.append([2,10])
l.append([3,11])
l.append([4,12])
l.append([5,13])
l.append([6,14])
l.append([7,15])

s = shapes.obj(342,-563,813,-253,p,l)

cam = camera.camera((7*math.pi)/18, width, height)
cam.x, cam.y, cam.z, cam.w = 1280, 384, -561, 543


running = True
while running:
    m1,m3,m2 = pg.mouse.get_pressed()
    keys=pg.key.get_pressed()
    if keys[pg.K_a]:
        cam.x -= 1
    if keys[pg.K_d]:
        cam.x += 1
    
    if keys[pg.K_w]:
        cam.z += 1
    if keys[pg.K_s]:
        cam.z -= 1

    if keys[pg.K_LSHIFT]:
        cam.y += 1
    if keys[pg.K_SPACE]:
        cam.y -= 1

    if keys[pg.K_q]:
        cam.w += 1
    if keys[pg.K_e]:
        cam.w -= 1

    
        

    print(cam.x,cam.y,cam.z,cam.w)

    cam.render(screen, [s])

    #s.draw(screen, width, height, (7*math.pi)/18)








    pg.display.flip()
    screen.fill(sky)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running == False