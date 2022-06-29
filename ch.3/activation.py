import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

def relu(x):
    y = np.maximum(0, x)
    return y


x = np.array([-1, 1 ,2]) # broadcast 
print('sigmoid-', sigmoid(x))
print('relu-', relu(x))


a = np.arange(-5, 5, 0.1)
z1 = sigmoid(a)
z2 = relu(a)


plt.plot(a, z1, 'b', label="sigmoid")
plt.plot(a, z2, 'r', label="relu")
plt.ylim(-0.1, 4)
plt.legend()
plt.show()
