import math
import matplotlib.pyplot as plot
import numpy as np

phi = (1+math.sqrt(5))/2

def func(n):
    return (phi**n - (-1/phi)**n)/(math.sqrt(5))

start = 0
ran = 6
acc = 0.01
seqx = []
seqy = []
for i in range(int(ran/acc)):
    #seqx.append((i*acc)+start)
    seqx.append(func((i*acc)+start).real)
    seqy.append(func((i*acc)+start).imag)
    #print(i)


plot.plot(seqx, seqy)
plot.grid(True, which='both')
plot.show()