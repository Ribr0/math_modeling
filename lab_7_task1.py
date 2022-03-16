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

def animate(i):
  cicloid.set_data(update(R=np.arange(-2*np.pi, 2*np.pi, 0.01), t=np.arange(-2*np.pi, 2*np.pi, 0.01)))

ani = FuncAnimation(fig, animate, frames=180, interval=2)

ani.save('anima_2.gif')

