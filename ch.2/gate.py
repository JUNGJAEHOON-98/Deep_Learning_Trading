import numpy as np 


def andgate_1(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # initialize parameters
    tmp = (x1*w1) + (x2*w2)

    if tmp <= theta:
        return 0
    else:
        return 1


def andgate_2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b 

    if tmp <= 0:
        return 0
    else:
        return 1


def nandgate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w*x) + b 

    if tmp <= 0:
        return 1
    else:
        return 0


def orgate(x1, x2): # AND Gate와 bias 값만 다르다.
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b 

    if tmp <= 0:
        return 0
    else:
        return 1

def xorgate(x1, x2): # multi-layer
    s1 = nandgate(x1, x2)
    s2 = orgate(x1, x2)
    y = andgate_2(s1, s2)
    return y
