import numpy as np
from lab_3_const import svobod_pad as g
x0 = int(input('x0 = '))
y0 = int(input('y0 = '))
v0 = int(input('v0 = '))
N = int(input('N = '))

coords = np.zeros((N, 3))

t = np.linspace(0, 5, N)

x = x0 + v0 * t

y = y0 + v0 * t - g * t**2 / 2

for i in range(N):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]

print(x)
print(y)