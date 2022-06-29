import numpy as np 

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])

print(x+y)
print(x*y) # elemen-wise product 

print(2*x) # broadcast 

a = np.array([[1, 2], [3, 4]])
b = np.array([5, 9])

print(a*b) # broadcast 

a_f = a.flatten() # convert 1-D Array
print(a_f)