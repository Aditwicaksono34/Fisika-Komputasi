import numpy as np
from numpy import*
import matplotlib.pylab as p
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mayavi
import mayavi.mlab as mlab

x,y=np,mgrid[-2:2:0.1,-2:2:0.1]
a=pow(4,2)
b=pow(4,2)
Z=a*b
mayavi.mlab.surf(Z)
mayavi.mlab.axes()
mayavi.mlab.outline()
mlab.show()