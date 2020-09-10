import numpy as py
import random
def sigmoid(x):##sigmoid func  will map any value to 0 to 1 range.it convert numbers into probablities 
    return 1/(1+py.exp(-x))
def sigmoid_derivative(x):##this function is to generate derivative of an output
    return x*(1-x)

trainging_inputs=py.array([[0,0,1],
                          [0,1,1],
                          [1,0,1],
                          [1,1,1]]) 
trainging_output=py.array([[0,1,1,0]]).T##.T is for transpose of a matrix
py.random.seed(1)##By using this func number will still be randomly distributed but they will be distributed exactly the same way each time we train
synaptic_weights=2*py.random.random((3,1))-1##generate random weights of dimension (3,1) beacuse we have 3 input and 1 output layer
print('weights:')
print(synaptic_weights)
for i in range(10000):
     input_layer=trainging_inputs
     output=sigmoid(py.dot(input_layer,synaptic_weights))##here we are taking dot prodect of two matrices and then putting it in sigmoid func
     error=trainging_output-output##Error can be found by subtracting actual output from predicted output
     adjustments=error*sigmoid_derivative(output)##here we are making adjusments w.r.t error
     synaptic_weights+=py.dot(input_layer.T,adjustments)##Here we are adding previous weights with dot product of(input_layer and adjusments) to update weights.
     

print("Updated final Weights:")
print(synaptic_weights)
print('output after updated weights\n')
print(output)
