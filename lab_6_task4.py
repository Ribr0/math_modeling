import matplotlib.pyplot as plt
import numpy as np

def spir(b=2, alph=np.pi*5):
  r = np.e ** (b * alph)
  plt.plot(r)
  plt.show()

spir()