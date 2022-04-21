import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames=300

def voda(R): 
  alp = np.arange(0, np.pi*3, 0.1)
  x = R * np.cos(alp)
  y = R * np.sin(alp)
  return x, y

  
def kaplya(R, N, t): 
  x = np.zeros(N)
  y = np.zeros(N)
  for i in range(0, N, 1):
    alpha = np.linspace(0, 2*np.pi, N)
    x[i] = R * t + R * np.cos(alpha[i])
    y[i] = R + R * np.sin(alpha[i])
  return x, y

fig, ax = plt.subplots()
voda, = plt.plot([], [], color='black')
kaplya, = plt.plot([], [], color='r')


def animate(i):
  voda.set_data(voda(R=1))
  kaplya.set_data(circle_func(R=1, N=100, t = 4*np.pi*i/frames))
  

ani = FuncAnimation (fig, animate, frames=frames, interval=30)

plt.xlim(-10,10)
plt.ylim(-10,10)
ani.save('pr.gif')