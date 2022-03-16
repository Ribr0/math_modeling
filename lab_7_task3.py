import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.sublots()
bab, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def ur(t):
  x = np.sin(t) * ((np.e**np.cos(t)) - 2 * (np.cos(4*t)) - ((np.sin(t / 12))**5))
  y = 