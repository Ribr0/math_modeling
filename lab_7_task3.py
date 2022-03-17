import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
bab, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def ur(t):
  x = np.sin(t) * ((np.e**np.cos(t)) - 2 * (np.cos(4*t)) - ((np.sin(t / 12))**5))
  y = np.cos(t) * ((np.e**np.cos(t)) - 2 * (np.cos(4*t)) - ((np.sin(t / 12))**5))
  return x, y
edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def update(i):
  bab.set_data(ur(t=i))

ani = FuncAnimation(fig, update, frames=360, interval=30)

ani.save('anima_task3.gif')