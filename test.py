import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

b = np.ones(30)
b[11] = 0

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
            if b[0] == 0 and b[len(b) - 1] == 0:
                break

            if index-1 >= 0 and index+1 <= len(b):
                plt.plot(index+1, 1, 'o', color='r', ms=50)
                b[index-1] = 0, 0

        i = 0
        time.sleep(1)
        print(b)
