import math

def norm(a,b):
    return (a*a + b*b)**0.5

def vectadd(v1t, v1a, v2t, v2a, mult):
    v1x = v1a * math.cos(v1t)
    v1y = v1a * math.sin(v1t)

    v2x = v2a * math.cos(v2t)
    v2y = v2a * math.sin(v2t)

    v3x = v1x + v2x
    v3y = v1y + v2y

    v3t = math.atan2(v3y, v3x)
    v3a = norm(v3x, v3y) * mult

    return v3t, v3a

def elastic(ropelen, dst, k):
    over = dst - ropelen
    if over < 0:
        return 0
    else:
        return (k*over)**2
