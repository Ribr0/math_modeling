import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
krug, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def move(t):
  x = np.arange(0, np.pi*2, 0.01)
  y = x * t
  return x, y

edge = 100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  krug.set_data(move(t=i))

ani = FuncAnimation(fig, animate, frames=180, interval=2)

ani.save('anima_task2.gif')

  
  