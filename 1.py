import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
R = 11
frames = 360
t = 0
def f_voda(r_v, t):
    alp = np.arange(0, np.pi*5, 0.1)
    x = (r_v * np.sin(alp)) + t
    y = (r_v * np.cos(alp))
    return x, y
    #t = t + 1

def f_kaplya(R, N, t):
    x = np.zeros(N)
    y = np.zeros(N)
    if R <= 2:
        for i in range(0, N, 1):
            alpha = np.linspace(0, 2 * np.pi, N)
            x[i] = R * np.cos(alpha[i])
            y[i] = (((R+1)*(R+1))**2) + (R * np.sin(alpha[i]) - t)
            if y[i]<=0.5:
                break
    else:
        for i in range(0, N, 1):
            alpha = np.linspace(0, 2 * np.pi, N)
            x[i] = R * np.cos(alpha[i])
            y[i] = (R ** 2) + (R * np.sin(alpha[i]) - t)
            if y[i] <= 0.5:
                break
    return x, y

def animate(i):
    voda.set_data(f_voda(r_v=0.1, t=1))
    kaplya.set_data(f_kaplya(R=R, N=360, t=(i+1)))

fig, ax = plt.subplots()
voda, = plt.plot([], [], color='black')
kaplya, = plt.plot([], [], color='r')

ani = FuncAnimation(fig, animate, frames=frames, interval=100)

plt.axis('square')
if R <= 10:
    plt.xlim(-20,20)
    plt.ylim(-20,20)
else:
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)

ani.save('project.gif')