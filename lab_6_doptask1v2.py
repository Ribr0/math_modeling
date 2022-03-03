import matplotlib.pyplot as plt
import numpy as np



def lissahy(a=1, A=1, B=5, u = np.pi/2, t = 2, b=0.5):
  x = A * np.sin(a * t + u)
  y = B * np.sin(b * t)
  plt.plot(x, y)
  plt.show()

lissahy()