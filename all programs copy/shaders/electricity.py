import numpy as np
import matplotlib.pyplot as plt
import math



def comp(vcc, ni, i):
    if ni > i:
        return vcc
    else:
        return 0

def capcharge(vin, res, capv):
    cv = (vin-capv)/res
    return cv

def capdis(capv, res):
    cv = capv/(res+1)
    return cv


    
capacitor = 0
out = 0
rout = 0

graph = []

for i in range(200):
    #vin = math.sin(i/10)
    graph.append(rout)

    
    
    out = comp(5, 2.5, capacitor)

    if out > 4.5:
        capacitor += capcharge(5, 10, capacitor)
        #out = capacitor

    if out < 0.5:
        capacitor -= capdis(capacitor, 10)


    rout = comp(5, out, 2.5)

    
    


    









plt.plot(graph)
plt.show()
