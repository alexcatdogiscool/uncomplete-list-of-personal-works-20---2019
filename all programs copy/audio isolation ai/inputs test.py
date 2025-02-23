import numpy as np
import math
import scipy.io.wavfile

rate, data = scipy.io.wavfile.read('audio smaples\clap4.wav')
rate2, data2 = scipy.io.wavfile.read('audio smaples\clap3.wav')

data = data[:,0]
data2 = data2[:,0]
print(data2.size)
wantlength = 8000
length = data.size
add = wantlength - length
addarr = np.zeros(add)
data = np.array(data)

#for i in range(add):
#data = np.append(data, addarr)
for i in range(data2.size):
    data[i] += data2[i]
#data = data.astype(int)

print(data)

scipy.io.wavfile.write('output.wav', rate, data)



