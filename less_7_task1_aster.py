import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
cicloid, = plt.plot([], [], 'o', color='r')
cicloid_graph, = plt.plot([], [], '-', color='r')

xdata, ydata = [], []

t = 180

def update(R, t):
  x = R*(np.cos(t)**3)
  y = R*(np.sin(t)**3)
  return x, y

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  cicloid.set_data(update(R=1, t=i))
  xdata.append(update(R=1, t=i)[0])
  ydata.append(update(R=1, t=i)[1])
  cicloid_graph.set_data(xdata[:i],ydata[:i])

ani = FuncAnimation(fig, animate, frames=t, interval=10)

ani.save('anima_task1_aster.gif')
