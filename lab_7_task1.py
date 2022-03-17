import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
cicloid, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def update(R, t):
  x = R * (t - (np.sin(t)**3))
  y = R * (1-((np.cos(t)**3)))
  return x, y

edge = 100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  cicloid.set_data(update(R=np.arange(-1*np.pi, 1*np.pi, 0.01), t=i))

ani = FuncAnimation(fig, animate, frames=180, interval=30)

ani.save('anima_task1.gif')

