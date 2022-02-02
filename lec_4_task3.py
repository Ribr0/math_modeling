import numpy as np 
from physic_const import gravity as g

m = 10
h = 7
v = 4

a = [m, h, v]

b = np.array(a)

def meh_energy(b):
  x = (m * g * h) + ((m * (v ** 2)) / 2)
  return x

print(meh_energy(b))

