import math

def norm(a,b,c):
    return math.sqrt(a*a + b*b + c*c)

def cast2D(fov, x,y,z, w,h):
    angleH = math.atan2(x,z)
    angleV = math.atan2(y,z)
    return (int((angleH/fov + 0.5)*w), int((angleV/fov + 0.5)*h))

def cast3D(fov, x,y,z,w):
    angleH = math.atan2(x,z)
    angleV = math.atan2(y,z)
    angleW = math.atan2(w,z)

    hs = angleH/fov + 0.5
    vs = angleV/fov + 0.5
    ws = angleW/fov + 0.5

    return hs,vs,ws