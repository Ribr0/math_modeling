import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time 
frames = 120

R_v = 1 # радиус воды
R_k = 1.5 #радиус капли
a_v = 1 # параметр шариков воды
a_k = 1 # параметр капли

def voda(R_v, a_v):
  x = R_v * np.sin(a_v)
  y = R_v * np.cos(a_v)
  return x, y

def kaplya(R_k, a_k):
  x = R_k * np.sin(a_k)
  y = R_k * np.cos(a_k)
  return x, y 

def animate(i):
  voda.set_data(voda(R_k=1, a_v=1)
  kaplya.set_data(kaplya(R_k=1, a_k=i))

fig, ax = plt.subplots()
voda, = plt.plot([], [], color='black')
kaplya, = plt.plot([], [], color='r')

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('square')
plt.xlim(-5,5)
plt.ylim(-5,5)

ani.save('project.gif')