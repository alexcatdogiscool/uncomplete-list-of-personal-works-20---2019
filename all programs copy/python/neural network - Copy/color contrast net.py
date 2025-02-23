import numpy as np

feature_set = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
labels = np.array([1,0,0,1,0])
labels = labels.reshape(5,1)

np.random.seed(42)
weightsx1 = np.random.rand(3,1)
weightsx2 = np.random.rand(3,1)
weightsx3 = np.random.rand(3,1)

hweights1 = np.random.rand(1)
hweights2 = np.random.rand(1)
hweights3 = np.random.rand(1)
bias1 = np.random.rand(1)
bias2 = np.random.rand(1)
bias3 = np.random.rand(1)
obias = np.random.rand(1)
lr = 0.05



def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1-sigmoid(x))

for epoch in range(1000):

    inputs = feature_set

    WX1 = np.dot(feature_set, weightsx1) + bias1
    WX2 = np.dot(feature_set, weightsx2) + bias2
    WX3 = np.dot(feature_set, weightsx3) + bias3

    z1 = sigmoid(WX1)
    z2 = sigmoid(WX2)
    z3 = sigmoid(WX3)

    z1 = z1.reshape(1,5)
    z2 = z2.reshape(1,5)
    z3 = z3.reshape(1,5)

    zr = np.array([z1,z2,z3])
    zr = zr.reshape(5,3)

    feature_set2 = np.array([z1,z2,z3])
    hweights = np.array([hweights1])

    hweightsr = np.array([hweights1,hweights2,hweights3])


    value2 = (z1*hweights1)+(z2*hweights2)+(z3*hweights3) + obias
    value = np.dot(zr,hweightsr) + obias


    z = sigmoid(value)

#    print(z)

    hweights1 = hweights1.reshape(1)


#    print(out)


    #backprop step 1
    error = z - labels
    print(error.sum())

    dcost_dpred = error
    dpred_dz = sigmoid_der(z)

    z_delta = dcost_dpred * dpred_dz


    inputs = feature_set.T
    weightsx1 -= lr * np.dot(inputs, z_delta)
    weightsx2 -= lr * np.dot(inputs, z_delta)
    weightsx3 -= lr * np.dot(inputs, z_delta)

#    print(hweights)
 #   print(weightsx1)
    inputs2 = z

    inputs2 = z.T
    hweightsr -= lr * np.dot(inputs2, z_delta)

    hagus = np.dot(inputs, z_delta)



    for num in z_delta:
        bias1 -= lr*num
        bias2 -= lr*num
        bias3 -= lr*num
        obias -= lr*num
        
    print(z)



    

    


