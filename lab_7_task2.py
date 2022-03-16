import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.sublots()
krug, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def move(alp, t=2):
  alp = np.arange(0, np.pi*2, 0.01)
  r = alp * t
  return r