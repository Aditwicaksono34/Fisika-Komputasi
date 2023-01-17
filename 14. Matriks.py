from visualpython import*
import numpy as np

np.arange(12)
np.array([0,1,2,3,4,5,6,7,8,9,10,11])
np.arange(12).reshape((3,4))
np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

a=np.arange(12).reshape((3,4))
np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(a.shape)  #shape
print(a.ndim)   #dimensi
print(a.size)   #size