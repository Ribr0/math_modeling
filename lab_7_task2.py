import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
krug, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def circle_move(R):
  alp = np.arange(0, np.pi*2, 0.1)
  x = R * np.cos(alp)
  y = R * np.sin(alp)
  return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

t = np.arange(0, 2*np.pi, 0.1)

def update(i):
  krug.set_data(circle_move(R=0.1*i))

ani = FuncAnimation(fig, update, frames=60, interval=50)

ani.save('anima_task2.gif')

  
  