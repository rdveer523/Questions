"""
17. How can you initialize a 5*5 numpy array with only zeroes?
"""
import numpy as np

n1=np.zeros((5,5))
print(n1,'dimensions : ',np.ndim(n1))
n2=np.zeros([3,3])
print(n2,'dimension is: ',np.ndim(n2))
