import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = sigmoid(-3.913)

print(x)
