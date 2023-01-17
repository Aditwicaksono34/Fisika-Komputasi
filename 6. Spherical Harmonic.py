import numpy as np
from numpy import*
import matplotlib.pylab as p
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mayavi
import mayavi.mlab as mlab
from mayavi.mlab import*
from numpy import pi , sin , cos , mgrid

n_mer, n_long=6,11
pi=np.pi
dphi=pi/1000.0
phi=np.arange(0.0,2*pi+0.5*dphi,dphi)
mu=phi*n_mer
x=np.cos(mu)*(1+np.cos(n_long*mu/n_mer)*0.5)
y=np.sin(mu)*(1+np.cos(n_long*mu/n_mer)*0.5)
z=np.sin(n_long*mu/n_mer)*0.5

plot3d(x,y,z,np.sin(mu),tube_radius=0.025,colormap='Spectral')
mayavi.mlab.show()