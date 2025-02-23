import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from keras.models import load_model
from numpy import load
print("")
print("start")


input_set = np.load('data\\input_set.npz')['array_1']/128
labels = np.load('data\\labels.npz')['array_1']/128
print(input_set.shape)


network = models.Sequential()
network.add(layers.Dense(164, activation='relu', input_shape=(164,)))
network.add(layers.Dense(100, activation='tanh', input_shape=(164,)))
network.add(layers.Dense(60, activation='tanh', input_shape=(100,)))
network.add(layers.Dense(60, activation='tanh', input_shape=(60,)))
network.add(layers.Dense(44, activation='sigmoid', input_shape=(60,)))


network.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

network.fit(input_set, labels, epochs=1000, batch_size=128)

network.save('brain.h5')

