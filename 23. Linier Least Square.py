import numpy as np
import pylab as p
import matplotlib.pyplot as plt
from numpy import*
from numpy.linalg import inv
from numpy.linalg import solve

t=np.arange(1.0,2.0,0.1)
x=np.array([1., 1.1, 1.24, 1.35, 1.451, 1.5, 1.92])
y=np.array([0.52, 0.8, 0.7, 1.8, 2.9, 2.9, 3.6])
sig=np.array([0.1, 0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
plt.errorbar(x,y,sig)
plt.title('Linear Least Square Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

Nd=7
A=np.zeros((3,3),float)
bvec=np.zeros((3,1),float)
ss = sx= sxx = sy = sxxx = sxxxx = sxy = sxy = sxxy = 0

for i in range (0,Nd):
    sig2=sig[i]*sig[i]
    ss += 1. /sig2
    sx += x[i]/sig2
    sy += y[i]/sig2
    rh1 = x[i]*x[i]
    sxx += rh1/sig2
    sxxy += rh1*y[i]/sig2
    sxy += x[i]*y[i]/sig2
    sxxx += rh1*x[i]/sig2
    sxxxx += rh1*rh1/sig2

A=np.array([[ss, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]])
bve=np.array([sy, sxy, sxxy])

xvec=multiply(inv(A),bvec)
Itest=multiply(A,inv(A))

print(' x vector via inverse: ', xvec)
print('A*inverse (A)', Itest)

xvec=solve(A,bvec)
print('x matriks via direct: ')
print(xvec, 'end= ')
print('Fit Parabola Final Results: , y(x)=a0+a1x+a2x^2')
print('a0= ', x[0])
print('a1= ', x[1])
print('a2= ', x[2])
print('i    xi      yi      yfit        ')
for i in range(0,Nd):
    s=xvec[0]+xvec[1]*x[i]+xvec[2]*x[i]*x[i]
    print(" %d %5.3f %5.3f %8.7f" % (i, x[i], y[i], s))

curve=xvec[0]+xvec[1]*t+xvec[2]*t**2
point=xvec[0]+xvec[1]*x+xvec[2]*x**2
plt.plot(t,curve,'r',x,point,'ro')
plt.show()