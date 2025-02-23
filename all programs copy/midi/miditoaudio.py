import numpy as np
from scipy.io import wavfile


f = open("hysteria.txt", "r")
song = f.read()
samplerate = 16000

tempo = 400

noteSamples = int((samplerate*60)//tempo)

audio = np.zeros(int(noteSamples*len(song.split(","))))

print(noteSamples)

for i, note in enumerate(song.split(",")):
    s, n = wavfile.read("notes\\{0}.wav".format(note))

    audio[i*noteSamples:(i+1)*noteSamples] = n[0:noteSamples]/10000

wavfile.write("song.wav", samplerate, audio)