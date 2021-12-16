import numpy as np
from lab_3_const import svobod_pad as g
x0 = int(input('x0 = '))
y0 = int(input('y0 = '))
v0 = int(input('v0 = '))
N = int(input('N = '))

a = np.zeros((N, 3))

t = np.arange(0, 6, N)

x = x0 + v0 * t

y = y0 + v0 * t - g * t**2

a = np.zeros((N, 3))
a[0, 0] = t
a[0, 1] = x
a[0, 2] = y

print(a)