import matplotlib.pyplot as plt
import numpy as np

def elps(p=1):
  ex = np.arange(-1, 1, 0.01)
  phi = np.arange(-2*np.pi, 2*np.pi, 0.1)
  r = p/(1+((ex)*np.cos(phi)))
  plt.plot(r)
  plt.show()
elps()
  