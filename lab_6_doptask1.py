import matplotlib.pyplot as plt
import numpy as np

b = int(input('Число b = '))

a = 1

m = b / a

mm = np.array[m]

nu = len(mm)

if nu <= 5:
  def lissahy(a=1, A=1, B=5, δ = np.pi/2, t = 2):
    x = A * np.sin(a * t + δ)
    y = B * np.sin(b * t)
    plt.plot(x, y)
    plt.show()
else:
  print('Число не подходит')