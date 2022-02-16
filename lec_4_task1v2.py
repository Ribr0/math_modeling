import numpy as np 

a = [1, 2, 3, 4, 5]

b = np.array(a)

def sr_arif(b):
 q = 0
  for i in range(len(b)):
    q = q + b[i]
  print(q)
