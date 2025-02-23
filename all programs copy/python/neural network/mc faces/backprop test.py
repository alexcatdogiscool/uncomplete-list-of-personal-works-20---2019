import numpy as np
from PIL import Image
import pickle as pkl

np.random.seed(12143)


def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative(x):
    return x * (1-x)




img = Image.open("creeper.png").convert("LA")
img = np.array(img)
img = img[:,:,0]
img = img.reshape(1,64)
img = img/255

img2 = Image.open("girl.png").convert("LA")
img2 = np.array(img2)
img2 = img2[:,:,0]
img2 = img2.reshape(1,64)
img2 = img2/255

img3 = Image.open("mooshroom.png").convert("LA")
img3 = np.array(img3)
img3 = img3[:,:,0]
img3 = img3.reshape(1,64)
img3 = img3/255

img4 = Image.open("skelleton.png").convert("LA")
img4 = np.array(img4)
img4 = img4[:,:,0]
img4 = img4.reshape(1,64)
img4 = img4/255

img5 = Image.open("steve.png").convert("LA")
img5 = np.array(img5)
img5 = img5[:,:,0]
img5 = img5.reshape(1,64)
img5 = img5/255

img6 = Image.open("tan face.png").convert("LA")
img6 = np.array(img6)
img6 = img6[:,:,0]
img6 = img6.reshape(1,64)
img6 = img6/255

img7 = Image.open("villager.png").convert("LA")
img7 = np.array(img7)
img7 = img7[:,:,0]
img7 = img7.reshape(1,64)
img7 = img7/255


input_set = np.array([img,img3,img5])
input_set = input_set[:,0,:]
labels = np.array(input_set)
print(input_set.shape)






def net(input_nodes, hidden_nodes, output_nodes):
    weights = np.random.rand(input_nodes, hidden_nodes)
    weights2 = np.random.rand(hidden_nodes, output_nodes)
    bias = np.random.rand(hidden_nodes)
    bias2 = np.random.rand(output_nodes)

    lr = 200.0

    itteration = 0
    count = 0
    error = np.array([100,100])

    running = True
    while error.sum() > 0.3:
        
        #forward prop

        z = np.dot(input_set, weights) + bias
        z = sigmoid(z)
        z2 = np.dot(z, weights2) + bias2
        z2 = sigmoid(z2)

        #back prop

        error = (labels - z2)*(labels - z2)

        bz = np.dot(z.T, (2*(labels - z2) * derivative(z2)))
        bz2 = np.dot(input_set.T, (np.dot(2*(labels - z2) * derivative(z2), weights2.T) * derivative(z)))
        weights += bz2
        weights2 += bz
    


        #image saving
        #outputimg = z2.reshape(64,64)
        #outputimg = (outputimg.astype(np.uint8))
        #outputimg = Image.fromarray(outputimg)
        #outputimg.save("smiley_output.png")

        itteration += 1
        count += 1
        
        outputimg = z2.reshape(24,8)
        outputimg = outputimg * 255
        outputimg = (outputimg.astype(np.uint8))
        outputimg = Image.fromarray(outputimg)
        #outputimg.save("images/{0}.png".format(count))

        if itteration == 100:
            print(count, error.sum())
            itteration = 0
            outputimg.save("images/{0}.png".format(count))

            

    weights2pkl = weights2
    biaspkl = bias2

    with open("weights2.pkl", "wb") as f:
        pkl.dump(weights2, f)

    with open("bias2.pkl", "wb") as f:
        pkl.dump(bias2, f)
        
    return error.sum()

    

ans = net(64,10,64)
print(ans)
