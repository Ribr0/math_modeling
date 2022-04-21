import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames=180
def cicloid(R,t):
  x = R * (np.cos(t)**3)
  y = R * (np.sin(t)**3)
  return x, y

def circle(R): 
  alp = np.arange(0, np.pi*3, 0.1)
  x = R * np.cos(alp)
  y = R * np.sin(alp)
  return x, y

def circle_func(R, N, t): 
  alp = np.arange(0, np.pi*3, 0.1)
  x = R * np.cos(alp)
  y = R * np.sin(alp) 
  return x, y

def astroid_func(R, t):  
  alp = np.arange(0, np.pi*2, 0.1)
  x = R/1.35 * np.cos(t) + R/4 * np.cos(alp) 
  y = R/1.35 * np.sin(t) + R/4 * np.sin(alp) 
  return x, y
  
fig, ax = plt.subplots()
ball, = plt.plot([], [], color='r')
ball2, = plt.plot([], [], 'o', color='g', ms=5)
ball3, = plt.plot([], [], color='b')
ball4, = plt.plot([], [], color='black')

def animate(i):
  
  ball.set_data(cicloid(R=1, t=np.linspace(0, 4*np.pi*i/frames, i)))
  ball2.set_data(cicloid(R=1, t=4*np.pi*i/frames))
  
  ball3.set_data(circle(R=1))
  ball4.set_data(astroid_func(R=1, t=4*np.pi*i/frames))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)


plt.axis('equal')
plt.xlim(-2,2)
plt.ylim(-2,2)

ani.save('lab_7_doptask1_2.gif')