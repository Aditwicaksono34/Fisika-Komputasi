#integral trapezoid a<x<b, N pts, interval N-1

import numpy as np
from numpy import*

a=0.5
b=2.3
N=1200

def func(x):
    return 5*(sin(8*x))**2*exp(-x*x)-13*cos(3*x)
def trapezoid(a,b,N):
    h=(b-a)/(N-1)
    sum=(func(a)+func(b))/2
    for i in range (1,N-1):
        sum +=func(a+i*h)
        return h*sum
print(trapezoid(a,b,N-1))