import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

a = np.zeros(15)
b = np.ones(15)
b[5] = 0
print(b)
print()

i = 0
flag = False
while True:
    if b[0] == 0 or b[len(b)-1] == 0:
        break
    if b[i] == 0 and flag == False:
        b[i-1], b[i+1] = 0, 0
        i = 0
        flag = True
        time.sleep(1)
        print(b)

    if b[i] == 0 and flag == True:
        b[i-1], b[len(b)-i+1] = 0, 0
        i = 0
        time.sleep(1)
        print(b)
    else:
        i += 1