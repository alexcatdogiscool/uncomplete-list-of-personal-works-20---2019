import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import tensorflow as tf
from tensorflow import keras
from scipy.io import loadmat
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import cv2

data = loadmat("emnist\\matlab\\emnist-letters.mat")['dataset']

input_set = (data['train'][0,0]['images'][0,0]/255)
labels = data['train'][0,0]['labels'][0,0]


ohe = OneHotEncoder(sparse=False)
labels = ohe.fit_transform(labels)
print(labels.shape)



model = Sequential()
model.add(Dense(700, input_dim=784, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='softmax'))
model.add(Dense(26, activation='softmax'))

opt = SGD(lr=0.01, momentum=0.9)
model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])
#model.fit(input_set, labels, epochs=1, batch_size=32)


model = keras.models.load_model("model.h5")

t = 0
while True:
    print(t*5, "-", (t+1)*5)
    model.fit(input_set, labels, epochs=5, batch_size=32)
    model.save('model.h5')
    t += 1

x = (input_set[32,:]).reshape(1,784)

pred = newModel.predict(x)

print(pred)
print(chr(np.argmax(pred)+65))