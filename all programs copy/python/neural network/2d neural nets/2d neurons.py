import numpy as np
from random import randrange, uniform
import random
from PIL import Image

np.random.seed(5)





def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

def net(inputx, inputy, hiddenx1, hiddeny1, outputx, outputy, learning_rate):
    lr = learning_rate
    
    weights = np.random.rand(inputy, hiddeny1, inputx, hiddenx1)
    weights2 = np.random.rand(hiddeny1, outputy, hiddenx1, outputx)
    
    current_best = 10000000.1
    itteration = 0



    running = True
    while running:

        
        z = np.dot(input_set, weights)
        z = np.sum(z, 1)
        z = np.sum(z, 1)
        z = sigmoid(z)
        z2 = np.dot(z, weights2)
        z2 = np.sum(z2, 1)
        z2 = np.sum(z2, 1)
        z2 = sigmoid(z2)
        #print("itteration: ", itteration)

        


        #error
        error = z - labels
        
        print(error.sum())

        dbz = derivative(z)
        delta_error = error * dbz


        inputs = input_set
        weights += lr * (np.dot(inputs, delta_error))
        #print(weights.sum())
        #break







        #make img
        zimg = z2
        zimg = z2 * 255
            
        zimg = np.zeros((1,5,5))
        zimg = zimg[0,:,:]
        #print("bjkebkebvkej ", zimg.shape)
 
        outimg = (np.array(zimg).astype(np.uint8))
        z2img = Image.fromarray(outimg)
        z2img.save('z2.png')
            
        if int(z2.all()) < (labels+100).all() and int(error.all()) > (labels-100).all():
            running = False
        
        
        


        
        itteration += 1



    return z





img = Image.open('input.png').convert('LA')
img.save('greyscale.png')
img = np.array(img)
img = img.reshape(2,5,5)


#img = np.zeros( (2,5,5) )
img = img[0,:,:]



test = np.array([[img]])
test = test.reshape(1,1,5,5)

test = test[0,:,:,:]
input_set = test
#print(test.shape)

labels = test
print(test)



ans = net(5,5, 5,5, 5,5, 0.02)
#print(ans)




#net(inputx, inputy, hiddenx, hiddeny, outputx, outputy, learning_rate)









