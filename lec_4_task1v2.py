import numpy as np 

a = [1, 2, 3, 4, 5]

b = np.array(a)

def sr_arif(b):
  ch = np.sum(b)
  w = ch / 5
  return w

print(sr_arif(b))