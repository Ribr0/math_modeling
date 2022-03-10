import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
cicloid, = plt.plot([], [], 'o', color='r')

cicloid, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

def update(R, t):
  x = R * (t - (np.sin**3)*t)
  y = R * (1-(np.cos**3)*t)
  return x, y

def animate(i):
  cicloid.set_data(update(R=2, t=3))

ani = FuncAnimation(fig, animate, frames=180, interval=30)

ani.save('anima_1.gif')

