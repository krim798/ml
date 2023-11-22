import numpy as np
import random
def random(h, w):
    A=np.random.random([h,w])
    B=np.random.random([h,w])
    s=A+B
    return A,B,s
#print(random(3,4))
def norm(A,B):
    s=A+B
    n=np.linalg.norm(s)
    return n
a=np.array([2,1])
b=np.array([[1,2],[2,1]])
print("A=\n",a)
print("B=\n",b)
print(norm(a,b))
def neuralNetwork(inputs,weights):
    x=np.matmul(weights.transpose(),inputs)
    return np.tanh(x)