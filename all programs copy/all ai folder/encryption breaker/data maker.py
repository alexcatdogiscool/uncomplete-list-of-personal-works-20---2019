from cryptography.fernet import Fernet
import random
import numpy as np

size = 60000

input_set = np.empty((size, 164))
labels = np.empty((size, 44))

frame = 0
for o in range(size):
    
    if frame == 1000:
        print(o)
        frame = 0
    frame += 1

    l = []
    for i in range(50):
        c = random.randint(98,122)
        l.append(c)

    msg = (''.join(chr(i) for i in l)).encode()

    key = Fernet.generate_key()
    f = Fernet(key)
    encrypt = f.encrypt(msg)

    encrypt = encrypt.decode("utf-8")
    encrypt = [ord(c) for c in encrypt]

    key = key.decode("utf-8")
    key = [ord(c) for c in key]

    input_set[o] = encrypt
    labels[o] = key

np.savez_compressed('data\\input_set.npz', array_1=input_set)
np.savez_compressed('data\\labels.npz', array_1=labels)