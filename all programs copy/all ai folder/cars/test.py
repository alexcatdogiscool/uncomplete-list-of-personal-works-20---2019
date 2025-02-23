import math
import pygame as pg




width = 900
height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
sky = (80, 147, 215)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('prediction sim')
screen.fill(black)
pg.display.flip()





def intercept(oa,ox,oy,olen, ta,tx,ty,tlen):
    m1 = math.tan(oa)
    m2 = math.tan(ta)

    h1 = ox
    k1 = oy
    
    h2 = tx
    k2 = ty

    ##### ONE #####
    h1 *= m1
    j1 = h1 + k1
    a1 = m1

    ##### TWO #####    
    h2 *= m2
    j2 = h2 + k2
    a2 = m2

    ##### SOLVE #####
    j1 -= j2
    a2 -= a1
    j1 /= a2
    x = j1

    y = m1*(x-ox) + oy
    x *= -1
    x -= ltx
    x *= -1
    x += ltx

    ltex = math.cos(ta) * tlen + tx
    ltey = math.sin(ta) * tlen + ty

    loex = math.cos(oa) * olen + ox
    l0ey = math.sin(oa) * olen + oy

    if x < ox or x > loex or y > tx or y < ltex:
        return None, None
    else:
        return x, y


loa = 0
lox = 200
loy = 300

lta = -1
ltx = 300
lty = 400



frame = 0
running = True
while running:
    frame += 1
    lta = -frame/1000

    loex = (math.cos(loa) *100) + lox
    loey = (math.sin(loa) *100) + loy

    ltex = (math.cos(lta) *100) + ltx
    ltey = (math.sin(lta) *100) + lty


    pg.draw.line(screen, black, (lox, loy), (int(loex), int(loey)))

    pg.draw.line(screen, black, (ltx, lty), (int(ltex), int(ltey)))

    px, py = intercept(loa,lox,loy,100, lta,ltx,lty,100)
    #print(px,py)
    if type(px) == float:
        pg.draw.circle(screen, red, (int(px), int(py)), 3)

    
    pg.display.flip()
    screen.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
