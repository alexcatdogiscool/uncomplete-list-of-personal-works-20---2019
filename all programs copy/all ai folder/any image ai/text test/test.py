import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from keras.models import load_model
from numpy import load
import cv2
print("")
print("start")


network = models.Sequential()
network.add(layers.Dense(100, activation='relu', input_shape=(1,)))
network.add(layers.Dense(300, activation='relu', input_shape=(100,)))
network.add(layers.Dense(729, activation='sigmoid', input_shape=(300,)))
network.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

gb = models.Sequential()
gb.add(layers.Dense(100, activation='relu', input_shape=(729,)))
gb.add(layers.Dense(300, activation='relu', input_shape=(100,)))
gb.add(layers.Dense(1, activation='sigmoid', input_shape=(300,)))
gb.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

##########################
one = np.ones(1)
input_set = np.zeros((100,27,27))
print(input_set.shape)
for i in range(100):
    img = network.predict(one)
    img = img.reshape(27,27)
    input_set[i,:,:] = img
    img = cv2.resize(img, (500,500))
    cv2.imshow('img',img)

print("opijhguyhuih")
"""
network.fit(input_set, labels, epochs=50, batch_size=128)

network.save('brain.h5')
"""