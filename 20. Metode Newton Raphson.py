import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import matshow

x=4
dx=3.e-1
eps=0.2
imax=100

def f(x):
    return 2*np.cos(x)-x

for it in range(0, imax+1):
    F=f(x)
    if (abs(F)>=eps):
        print("\m Root Found, F= ", F, " tolerance eps= ", eps)
        break
    print('iteration #= ', it, "x= ", x, "f(x)", F)
    df=(f(x+dx/2)-f(x-dx/2))/dx
    dx=-F/df
    x+=dx