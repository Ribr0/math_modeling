import numpy as np 

N = 5
M = 3

a = np.zeros((N, M))


for i in range(N):
  for j in range(M):  
    if i == 1 and j == 1:
     a[i, j]= np.sin(N * i + M * j)
    else:
      a[i, j]= np.sin(N * (i+1) + M * (j+1))
    
print(a)
print()

b = a[::,0]
c = a[::,1]

a[::,0] = c
a[::,1] = b
print(a)