import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames=300
def cicloid(R,t):
  x = R * (np.cos(t)**3)
  y = R * (np.sin(t)**3)
  return x, y

def circle(R): #окружность 
  alp = np.arange(0, np.pi*2, 0.1)
  x = R * np.cos(alp)
  y = R * np.sin(alp)
  return x, y

def mal_circle(R, t):
  alp = np.arange(0, 2*np.pi, 0.1)
  x1 = R * np.cos(alp)
  y1 = R * np.sin(alp)
  x = x1 * (np.cos(t)**3)
  y = y1 * (np.sin(t)**3)
  return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], color='r')
ball2, = plt.plot([], [], 'o', color='g', ms=5)
ball3, = plt.plot([], [], color='b')
ball4, = plt.plot([], [], color='m')

def animate(i):
  ball.set_data(cicloid(R=1, t=np.linspace(0, 4*np.pi*i/frames, i)))
  ball2.set_data(cicloid(R=1, t=4*np.pi*i/frames))
  ball3.set_data(circle(R=1))
  ball4.set_data(mal_circle(R=1, t=1))

ani = FuncAnimation (fig, animate, frames=frames, interval=30)

plt.axis('square')
#plt.xlim(-1.5,1.5)
#plt.ylim(-1.5,1.5)
plt.xlim(3,3)
plt.ylim(3,3)
ani.save('lab_7_doptask1_2.gif')