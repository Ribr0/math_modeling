import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames=180

def circle_func(R, N, t): #окружность 
  x = np.zeros(N)
  y = np.zeros(N)
  for i in range(0, N, 1):
    alpha = np.linspace(0, 1*np.pi, N)
    x[i] = R * t + R * np.cos(alpha[i])
    y[i] = R + R * np.sin(alpha[i])
  return x, y

fig, ax = plt.subplots()

ball4, = plt.plot([], [], color='r')

def animate(i):
  ball4.set_data(circle_func(R=0.5, N=1, t=1))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)


plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-2,2)

ani.save('test.gif')