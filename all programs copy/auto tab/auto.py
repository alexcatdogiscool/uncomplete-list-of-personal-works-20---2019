import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt



sr, wave = wavfile.read("note.wav")

print(len(wave))


out = np.fft.fft(wave)

#print(np.where(out == max(out)))


plt.plot(out)
plt.show()