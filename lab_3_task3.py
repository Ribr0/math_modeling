import numpy as np
from lab_3_const import svobod_pad as g
x0 = int(input('x0 = '))
y0 = int(input('y0 = '))
v0 = int(input('v0 = '))
N = int(input('N = '))
z = 0 

a = np.zeros((N, 3))

for i in a[:, 0]:
  z += 1
  a[:, 0] = z

for x in a[:, 1]:
  x = x0 + v0*a[:, 0]
  a[:, 1] = x
for y in a[:, 2]:
  y = y0 + v0 * - ((g* (a[:, 0])**2) / 2)
  a[:, 2] = y

print(a)