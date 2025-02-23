import numpy as np
from scipy.io import wavfile



samplerate, data = wavfile.read('unedited.wav')

print(samplerate)

cur = 0
for i in range(len(data)):
    if i % samplerate == 0 and i != 0:
        wavfile.write("notes\\{0}.wav".format(cur), samplerate, data[i-samplerate:i])
        cur += 1