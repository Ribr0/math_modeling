import numpy as np
from lab_3_const import svobod_pad as g
x0 = int(input('x0 = '))
y0 = int(input('y0 = '))
V0 = int(input('V0 = '))

t0 = 0
x0S = x0+V0*t0
y0S = (y0+V0*t0-((g*(t0**2)/2)))

t1 = 1
x1S = x0+V0*t1
y1S = (y0+V0*t1-((g*(t1**2)/2)))

t2 = 2
x2S = x0+V0*t2
y2S = (y0+V0*t2-((g*(t2**2)/2)))

t3 = 3
x3S = x0+V0*t3
y3S = (y0+V0*t3-((g*(t3**2)/2)))

t4 = 4
x4S = x0+V0*t4
y4S = (y0+V0*t4-((g*(t4**2)/2)))

t5 = 5
x5S = x0+V0*t5
y5S = (y0+V0*t5-((g*(t5**2)/2)))

l = [[t0, x0S, y0S], [t1, x1S, y1S], [t2, x2S, y2S], [t3, x3S, y3S], [t4, x4S, y4S], [t5, x5S, y5S]]

mas = np.array(l)
print(mas)





