import math


def pythag(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def lqcoll(x1,y1,r1,x2,y2,r2):
    rads = (r1+r2)
    if x1 == x2 and y1 == y2:
        return False
    if abs(x1-x2) < rads and abs(y1-y2) < rads:
        return True
    else:
        return False

def hqcoll(x1,y1,r1,x2,y2,r2):
    if x1 == x2 and y1 == y2:
        return False
    d = pythag(x1,y1,x2,y2)
    if d <= r1+r2:
        return True
    else:
        return False

def vectadd(a1,s1,a2,s2):
    x1 = math.cos(a1) * s1
    y1 = math.sin(a1) * s1
    
    x2 = math.cos(a2) * s2
    y2 = math.sin(a2) * s2

    x = x1+x2
    y = y1+y2

    a = math.atan2(y,x)
    s = pythag(x,y,0,0)

    return a,s

def makepos(a):
    if a < 0:
        a += 2*math.pi
        makepos(a)
    if a > 2*math.pi:
        a -= 2*math.pi
        makepos(a)
    return a

def bounce(x1,y1,a1,v1,m1,r1,x2,y2,a2,v2,m2,r2):
    p = ((m1*v1)+(m2*v2))/2
    at = math.atan2(y1-y2, x1-x2)
    at = makepos(at)
    v1n = p/m1
    v2n = p/m2

    d = pythag(x1,y1,x2,y2)-r1-r2
    xo = math.cos(at) * -d/2 + x1
    yo = math.sin(at) * -d/2 + y1

    xt = math.cos(at) * d/2 + x2
    yt = math.sin(at) * d/2 + y2

    

    a1,v1 = vectadd(a1,v1, at,v1n)
    a2,v2 = vectadd(a2,v2, at+math.pi,v2n)
    return a1,v1, xo, yo,   a2,v2, xt, yt


def bounds(x,y,a,v,e,r,width,height):
    xv = math.cos(a) * v * e
    yv = math.sin(a) * v * e
    if x < r:
        a,v = vectadd(a,v,math.pi,2*xv)
        return a,v, 1+r, y
    if x > width-r:
        a,v = vectadd(a,v,math.pi,2*xv)
        return a,v, width-1-r, y
    if y < r:
        a,v = vectadd(a,v,math.pi/2,-2*yv)
        return a,v, x, r+1
    if y > height-r:
        a,v = vectadd(a,v,-math.pi/2,2*yv)
        return a,v, x, height-1-r
    return a,v,x,y


def circlegen(x,y,rm,rp,ps, n):
    fib = (1+5**0.5)/2

    a = 2*math.pi*fib*n
    d = ((n/(ps))**0.5)*rm

    x1 = math.cos(a) * d + x
    y1 = math.sin(a) * d + y
    return x1,y1
