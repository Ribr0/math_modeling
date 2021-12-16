import numpy as np
from lab_3_const import acc_of_gravity as g
h = 100
a = (np.pi)/3
b = 30
v = (((g*h)*(np.tan(b)**2))/(2*(np.cos(a)**2))*(1-(np.tan(b))*(np.tan(a))))**0.5

print(v)

from lab_3_const import T, q as E, bocman_const as B, ealier as ER, plank as plk 

N = (2/np.pi)*(plk/((B*T)**1.5))*(ER**(-E/(B*T)))*(E**(T/2))

print(N)