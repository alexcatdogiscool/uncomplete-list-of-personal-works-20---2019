import numpy as np
from scipy.io.wavfile import write

arr = (np.load('data.npy')-0.5)*10000
arr = np.asarray(arr, dtype=np.int16)

baud = 40000

write('data.wav', baud, arr)
