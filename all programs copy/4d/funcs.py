import math

def norm(a,b,c):
    return math.sqrt(a*a + b*b + c*c)

def cast2D(fov, x,y,z, w,h):
    angleH = math.atan2(x,z)
    angleV = math.atan2(y,z)

    return (int((angleH/fov + 0.5)*w), int((angleV/fov + 0.5)*h))