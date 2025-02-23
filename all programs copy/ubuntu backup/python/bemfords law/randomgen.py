import random

z = []
o = []
t = []
th = []
f = []
fi = []
s = []
se = []
e = []
n = []
for i in range(10000):
    val = random.randint(0,100)
    if val == 0:
        z.append(val)
    if val == 1:
        o.append(val)
    if val == 2:
        t.append(val)
    if val == 3:
        th.append(val)
    if val == 4:
        f.append(val)
    if val == 5:
        fi.append(val)
    if val == 6:
        s.append(val)
    if val == 7:
        se.append(val)
    if val == 8:
        e.append(val)
    if val == 9:
        n.append(val)

print(len(o)/10000)