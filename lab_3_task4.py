import numpy as np 

i = int(input('i = '))
j = int(input('j = '))

if i >= 1 and j >= 1:
 A = np.sin(np.N * i + np.M * j)
elif i >= 0 and j >=0:
 A = np.sin(np.N * (i + 1) + np.M * (j + 1))
else:
  A = 0

q = np.array(A)