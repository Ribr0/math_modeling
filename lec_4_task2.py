import numpy as np 

a = [1, 2, 3, 4, 5]

b = np.array(a)

def func(b):
  for i in range(len(b)):
    c = b[i] * b[i+1]

func(b)