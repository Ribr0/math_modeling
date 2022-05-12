import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 20
N = 15
fig, ax = plt.subplots()
kaplya, = plt.plot([], [], color='k')


def drop(R, x0, y0, vx0, vy0, t):
    x1 = x0 + vx0 * t
    y1 = y0 + vy0 * t
    alp = np.arange(0, 2*np.pi, 0.1)
    x = x1 + R * np.sin(alp)
    y = y1 + R * np.cos(alp)
    return x, y

water = []

colors = {0: 'r', 1: 'g'}

def animate(i):
    if i > 5:
        kaplya.set_data(drop(0.1, 0.5, 1, 0, 0, t=i))
    else:
        kaplya.set_data(drop(0.1, 0.5, 1, 0, -0.06, t=i))
    water.clear()
    for j in range(N):
        if i < 5:
              ball, = plt.plot([], [], color=colors[0])
              water.append(ball)
        else:
            ball, = plt.plot([], [], color=colors[1])
            water.append(ball)

    for j in range(3):
        for k in range(5):
            ball = water[k*2 + 3*j]
            ball.set_data(drop(0.1, 0.1 + k*0.2, 0.5 - 0.2*j, 0, 0, t=i))


ani = FuncAnimation(fig, animate, frames=frames, interval=100)

plt.axis('square')
plt.xlim(0,1)
plt.ylim(0,1)


ani.save('project.gif')