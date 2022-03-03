import matplotlib.pyplot as plt
import numpy as np



def lissahy(A=1, k=4):
  phi = np.arange(-4*np.pi, 4*np.pi, 0.01)
  r = np.e**(A*phi)
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  plt.plot(x, y, q)
  plt.show()
#lissany()

def rose(A=1, k=3):
  phi = np.arange(-4*np.pi, 4*np.pi, 0.01)
  r = np.sin(k*(phi))
  
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  plt.plot(x, y)
  plt.show()
rose()

def jezl(A=1, k=3):
  phi = np.arange(-4*np.pi, 4*np.pi, 0.01)
  r = k/(phi**0.5)
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  plt.xlim(-10, 20)
  plt.ylim(-10, 10)
  plt.plot(x, y)
  plt.show()
#jezl()

def arx(A=1, k=3):
  phi = np.arange(0*np.pi, 4*np.pi, 0.01)
  #r = np.sin(k*(phi))
  r = k*(phi)
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  plt.plot(x, y)
  plt.show()
#arx()