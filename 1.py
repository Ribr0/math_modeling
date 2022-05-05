import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 20
N = 15
fig, ax = plt.subplots()
plt.plot(1, 1, 'o', color='k', ms=50)
water = []


def drop(R, x0, y0, vx0, vy0, t):
    x1 = x0 + vx0 * t
    y1 = y0 + vy0 * t
    alp = np.arange(0, 2*np.pi, 0.1)
    x = x1 + R * np.sin(alp)
    y = y1 + R * np.cos(alp)
    return x, y

#for j in range(30):
#    print(j)
#    ball, = plt.plot([], [], color='k')
#    ball = water[j]
 #   ball.set_data(drop(1, j, 1, 0, 0, t=j))
#    water.append(ball)

def animate(i):
    if i > 10:
        plt.plot(1, 1, 'o', color='r', ms=50)

def animat(i):
    for j in range(3):
        for k in range(5):
            ball = water[k*3 + j]
            ball.set_data(drop(1, 0.1 + k*0.2, 0.5 - 0.2*j, 0, 0, t=i))

ani = FuncAnimation(fig, animate, frames=frames, interval=100)

plt.axis('square')
plt.xlim(-5,5)
plt.ylim(-5,5)


ani.save('project.gif')