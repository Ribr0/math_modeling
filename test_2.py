import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

a = np.zeros(15)
b = np.ones(15)
b[5] = 0
print(b)
print()

indexes = []
i = 0
while True:
    if b[i] == 0:
        indexes.append(i)

    if i < len(b):
        i += 1

    if i >= len(b):
        for index in indexes:
            if b[index-1] > 0 and b[index+1] < len(b):
                b[index+1], b[index-1] = 0, 0
        i = 0
        time.sleep(1)
        print(b)


