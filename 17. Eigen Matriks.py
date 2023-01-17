import numpy as np
from numpy.linalg import solve

a=np.matrix([[2,1,1],[-1,1,2],[2,2,2]]) #nilai matriks
print("matriks: ", a)

eigenvalue, eigenvektor=np.linalg.eig(a)
print("\n Eigenvalue", eigenvalue)
print("\n Eigenvektor", eigenvektor)