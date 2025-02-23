import numpy as np
from PIL import Image
import pickle as pkl

np.random.seed(12143)


def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative(x):
    return x * (1-x)




img = Image.open("side1.png").convert("LA")
img = np.array(img)
img = img[:,:,0]
img = img.reshape(1,100)
img = img/255

img2 = Image.open("side2.png").convert("LA")
img2 = np.array(img2)
img2 = img2[:,:,0]
img2 = img2.reshape(1,100)
img2 = img2/255

img3 = Image.open("side3.png").convert("LA")
img3 = np.array(img3)
img3 = img3[:,:,0]
img3 = img3.reshape(1,100)
img3 = img3/255

img4 = Image.open("side4.png").convert("LA")
img4 = np.array(img4)
img4 = img4[:,:,0]
img4 = img4.reshape(1,100)
img4 = img4/255

img5 = Image.open("side5.png").convert("LA")
img5 = np.array(img5)
img5 = img5[:,:,0]
img5 = img5.reshape(1,100)
img5 = img5/255

img6 = Image.open("up1.png").convert("LA")
img6 = np.array(img6)
img6 = img6[:,:,0]
img6 = img6.reshape(1,100)
img6 = img6/255

img7 = Image.open("up2.png").convert("LA")
img7 = np.array(img7)
img7 = img7[:,:,0]
img7 = img7.reshape(1,100)
img7 = img7/255

img8 = Image.open("up3.png").convert("LA")
img8 = np.array(img8)
img8 = img8[:,:,0]
img8 = img8.reshape(1,100)
img8 = img8/255

img9 = Image.open("up4.png").convert("LA")
img9 = np.array(img9)
img9 = img9[:,:,0]
img9 = img9.reshape(1,100)
img9 = img9/255

img10 = Image.open("up5.png").convert("LA")
img10 = np.array(img10)
img10 = img10[:,:,0]
img10 = img10.reshape(1,100)
img10 = img10/255


input_set = np.array([img,img2,img3,img4,img5,img6,img7,img8,img9,img10])
input_set = input_set[:,0,:]
labels = np.array([[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1]])
print(input_set)






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
    while error.sum() > 2.5:
        
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
        
        #outputimg = z2.reshape(24,8)
        #outputimg = outputimg * 255
        #outputimg = (outputimg.astype(np.uint8))
        #outputimg = Image.fromarray(outputimg)
        #outputimg.save("images/{0}.png".format(count))

        if itteration == 10000:
            print(count, error.sum())
            itteration = 0
            #outputimg.save("images/{0}.png".format(count))

            

    weights2pkl = weights2
    biaspkl = bias2

    with open("weights2.pkl", "wb") as f:
        pkl.dump(weights2, f)

    with open("bias2.pkl", "wb") as f:
        pkl.dump(bias2, f)
        
    return z2

    

ans = net(100,4,2)
print(ans)
