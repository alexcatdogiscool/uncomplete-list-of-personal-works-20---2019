import math

def pchk(p):
    for i in range(p-2):
        n = p/(i+2)
        div = n.is_integer()
        if div == True:
            print(i+2)
            return False
    return True


print(pchk(57751))


"""
frame = 0
for i in range(10000000000):
    if frame == 10000:
        print(i)
        frame = 0
    frame += 1
    
    if pchk(i) == True:
        t = abs(math.tan(i))
        if t > i:
            print("YES", i)
"""