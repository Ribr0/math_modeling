import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
krug, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def circle_move():
  x = alp * t
  y = alp * t

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def update(i):
  krug.det_data(circle_move(alp = np.arange(0, np.pi*2, 0.1), t = 20))

ani = FuncAnimation(fig, update, frames=60, interval=40)

ani.save('anima_task2.gif')


  
  