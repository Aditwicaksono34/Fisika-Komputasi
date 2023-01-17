import numpy as np
import matplotlib.pylab as p
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

delta = 0.1
x = p.arange(-3.,3.,delta)
y = p.arange(-3.,3.,delta)
X, Y = p . meshgrid (x , y )
Z = p . sin (X) * p. cos (Y) # Surface height

def randrange(n,vmin,vmax):
    return (vmax-vmin)*np.random.rand(n)+vmin

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
n=100
for c , m, zl , zh in [('r' , 'o' , -50, -25),( 'b' , '^' , -30, -5)] :
    xs=randrange(n,23,22)
    ys=randrange(n,0,100)
    zs=randrange(m,zl,zh)
    ax.scatter(xs,ys,zs,c=c,marker=m)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()