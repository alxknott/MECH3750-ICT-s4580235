import numpy as np
import matplotlib as mpl
import math

#array for f(x)
x = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])

def f_1(x):
    f_1 = x**3
    return f_1

def f_2(x):
    f_2 = 3*x**2 - 2*x
    return f_2

def f_3(x):
    f_3 = math.sin(x)
    return f_3

def fd_forward(x):
    fd_forward = (f(x+h)-f(x))/h
    return fd_forward

def fd_backward(x):
    fd_backward = (f(x)-f(x-h))/h
    return fd_backward

def fd_central(x):
    fd_central = (f(x+h)-f(x-h))/2*h
    return fd_central




mpl.figure()
mpl.plot(x, fd_forward)
mpl.plot(x, fd_backward)
mpl.plot(x, fd_central)
mpl.show()
