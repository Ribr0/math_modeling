import matplotlib.pyplot as plt
import numpy as np

def circle_ellipse(radius=10):
  x = np.arange(-2*radius, 2*radius, 0.1)
  y = np.arange(-2*radius, 2*radius, 0.1)
  
  X, Y = np.meshgrid(x, y)
  
  fxy = X**2 + Y**2 - radius**2 

  f1x1y1 = X**2/3 + Y**2 - radius**2

  plt.contour(X, Y, fxy, levels=[0])
  plt.contour(X, Y, f1x1y1, levels=[0])
  plt.axis('equal')
  plt.show()

circle_ellipse()