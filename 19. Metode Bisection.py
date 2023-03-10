#Multidimension Newton Search

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*np.cos(x)-x

def bisection (xminus, xplus, Nmax, eps):
    for it in range (0, Nmax):
        x=(xplus+xminus)/2
        print("it", it, "x", x, "fx", f(x))
        if(f(xplus)*f(x)>0.):
            xplus=x
        else:
            xminus=x
        if (abs(f(x))<eps):
            print("\n root found with precision eps= ", eps)
            break
        if it == Nmax-1:
            print("\n Root NOT fount after Nmax iterations\n")
    return x
eps=1e-6
a=0.0
b=7.0
imax=100
root=bisection(a,b,imax,eps)
print("Root= ",root)
