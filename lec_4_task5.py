import numpy as np

r = 4                   #круг 
a = 5                   #прямоугольник
b = 7                   #прямоугольник
c = 9                   #прямоугольник
h = 16                  #трегольник 

q = float(input('Выберите номер фигуры: \n 1 - круг \n 2 - прямоугольник \n 3 - трегольник \n'))

def func(r, a, b, c, h):
  kr = np.pi * (r **2)
  pr = a * b
  tr = 0.5 * a * h
  if q == 1:
    return kr
  elif q == 2:
    return pr
  elif q == 3:
    return tr
  else:
    return Ne_chudi
  
print(func(r, a, b, c, h))

