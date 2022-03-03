import matplotlib.pyplot as plt
import numpy as np



def lissahy(a=3, A=2, B=5, u = np.pi/2, b=0.5):
  t = np.arange(-4*np.pi, 4*np.pi, 0.01)
  x = A * np.cos(a * t + u)
  y = B * np.sin(b * t)
  plt.xlim(-10, 10)
  plt.ylim(-10, 10)
  plt.plot(x, y)
  plt.show()

lissahy()