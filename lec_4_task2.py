import numpy as np 

a = [1, 2, 3, 4, 5]

b = np.array(a)

def func(a):
  for i in (0, 6, 1):
    c = b[i] * b[i+1]