import matplotlib.pyplot as plt
import numpy as np

def parabola_gip(x_gip1=0.01, x_gip2=10, x_par1=-10, x_par2= 10, N=0.01, a=1, b=3, c=4, k=1, label='Grafiki'):
  #парабола
  x_par = np.arange(x_par1, x_par2, N)
  y_par = a*x_par**2 + b*x_par + c
  #гипербола
  x_gip = np.arange(x_gip1, x_gip2, N)
  y_gip = k/(x_gip)
  #вывод
  plt.plot(x_gip, y_gip)
  plt.plot(x_par, y_par)
  plt.show()

parabola_gip()

