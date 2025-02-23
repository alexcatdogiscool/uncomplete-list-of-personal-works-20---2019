import math


def angle(sx,sy, ex,ey):
    return math.atan2((ey-sy), (ex-sx))



val = angle(2,1,3,2)
print(val)