import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 120
t = 0
if t < 5:
  for i in range(0, 10, 1):
    def f_voda(r_v):
      for i in range(0, 10, 1):
        alp = np.arange(0, np.pi*5, 0.1)
        x = (r_v * np.sin(alp)) + i 
        y = (r_v * np.cos(alp)) 
      return x, y

def f_kaplya(R, N, t):
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range(0, N, 1):
        alpha = np.linspace(0, 2 * np.pi, N)
        x[i] = R * np.cos(alpha[i])
        y[i] = 5 + (R * np.sin(alpha[i]) - t)
    return x, y

def animate(i):
    voda.set_data(f_voda(r_v=1))
    kaplya.set_data(f_kaplya(R=0.5, N=360, t=i))

fig, ax = plt.subplots()
voda, = plt.plot([], [], color='black')
kaplya, = plt.plot([], [], color='r')

ani = FuncAnimation(fig, animate, frames=frames, interval=1000)

plt.axis('square')
plt.xlim(-10,10)
plt.ylim(-10,10)

ani.save('project.gif')