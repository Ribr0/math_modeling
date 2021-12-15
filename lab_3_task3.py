import numpy as np
from lab_3_const import svobod_pad as g
x0 = int(input('x0 = '))
y0 = int(input('y0 = '))
V0 = int(input('V0 = '))
t = int(input('t = '))
x = x0+V0*t
y = (y0+V0*t-((g*(t**2)/2)))
print(f'{x}, {y}')
