import math
import numpy as np

def norm(a,b):
    return (a*a + b*b)**0.5

def vectadd(v1t, v1a, v1m, v2t, v2a, v2m, mult):
    v1a = v1m * v1a
    v2a = v2m * v2a
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


def dst(p1,p2,p3):
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)

    if p3[0] > p1[0] and p3[0] < p2[0]:
        d = np.linalg.norm(np.cross(p2-p1, p1-p3))/np.linalg.norm(p2-p1)
    else:
        d = 100
    return d