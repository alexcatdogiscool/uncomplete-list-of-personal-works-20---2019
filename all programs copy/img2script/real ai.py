import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import tensorflow as tf
from tensorflow import keras
import os
import cv2
import time

model = keras.models.load_model("model.h5")

path = 'induvidual'

for i in range(len(os.listdir(path))):
    img = (cv2.imread(path+'\\{}.png'.format(i), cv2.IMREAD_GRAYSCALE)/255).T.reshape(1,784)
    img = 1-img
    letter = chr(np.argmax(model.predict(img))+65)
    print(letter)
