import numpy as np

a = int(input('Число: '))

b = int(input('Степень: '))

def step(a, b):
  for i in range(0, b, 1):
    a = a * b[i]

print(step)