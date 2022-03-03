import matplotlib.pyplot as plt
import numpy as np

def lc(s=10): 
  N = np.arange(-1*s, s, 1)
  y = N
  x = N+(N+1)
  plt.plot(x, y)
  plt.show()
  
lc()