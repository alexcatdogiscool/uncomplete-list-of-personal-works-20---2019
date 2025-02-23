import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras import models
from keras import layers
from keras.models import load_model
import pygame as pg
import time
import cv2
import random
from cryptography.fernet import Fernet

model = load_model('brain.h5')


data = 'hello world, this is an encrypted message, secrets'.encode()

key = Fernet.generate_key()
f = Fernet(key)
data = f.encrypt(data)
data = data.decode("utf-8")
data = [ord(c) for c in data]
array = np.empty((1,164))
array[0] = data
array = array/128

out = model.predict(array) *128
out = out.reshape(44)
l = []
for i in range(44):
    l.append(out[i])


out = (''.join(chr(i) for i in l))

print(out)
print(key.decode("utf-8"))