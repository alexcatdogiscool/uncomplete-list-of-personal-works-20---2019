import numpy as np
from random import randrange, uniform
import scipy.special
from PIL import Image

np.random.seed(1)







class neuralNetwork:
    
    def __init__(self, input_nodes, output_nodes, hidden_nodes, learning_rate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        self.wih = np.random.normal(0.0,pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0,pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        self.lr = learning_rate

        self.activation_function = lambda x: scipy.special.expit(x)
        

    
    def train(self, input_list, target_list):

        inputs = np.array(input_list, ndmin = 2).T
        targets = np.array(target_list, ndmin = 2).T
        
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        self.output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, self.output_errors)

        #train
        self.who += self.lr * np.dot((self.output_errors * final_outputs * (1.0-final_outputs)), np.transpose(hidden_outputs))
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0-hidden_outputs)), np.transpose(inputs))

        

    def query(self, input_list):
        inputs = np.array(input_list, ndmin = 2).T

        hidden_inputs = np.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)

        final_outputs = self.activation_function(final_inputs)

        return final_outputs

        



img = Image.open("cat.png")
img = list(img.getdata())
img = [x for sets in img for x in sets]





n = neuralNetwork(12288, 12288, 12288, 0.02)
#print(n.query([1.0, 0.5, 0.1, 0.7]))
inputs = img
targets = img

unknown = img

number = 0
error = 10
lasterror = 1
itter = 1
while error > 0.1:
    n.train(inputs, targets)
    number += 1
    print("itteration number ", number)
    print(n.output_errors.sum())
    error = n.output_errors.sum()
    
    

out = n.query(unknown)
out = out * 255
print(out)











#        self.bpweights = np.random.rand(hidden_nodes, input_nodes)
 #       self.bpweights2 = np.random.rand(hidden_neurons2, hidden_nodes)
  #      self.bpweights3 = np.random.rand(hidden_neurons3, hidden_neurons2)
   #     self.bpweights4 = np.random.rand(output_nodes, hidden_neurons3)
    
     #   self.bias = np.random.rand(hidden_nodes)
      #  self.bias2 = np.random.rand(hidden_neurons2)
       # self.bias3 = np.random.rand(hidden_neurons3)
        #self.bias4 = np.random.rand(output_nodes)



