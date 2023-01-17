import numpy as np
from numpy import*
from numpy.linalg import solve
from numpy.linalg import inv

A=np.array([[1,2,3],[22,32,42],[55,66,100]])
B=np.array([1,2,3])
x=solve(A,B)
y=dot(inv(A),A)

print('A= ',A)
print('B= ',B)
print('x= ', x)
print ('residual= ', dot(A,x)-B)
print ('xb =', multiply(inv(A),B))