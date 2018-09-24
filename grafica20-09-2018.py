import sympy as sp
from math import *
n = sp.symbols('n')
T = 2
wo = (2*sp.pi)/T
fn = ((-1j)/n*sp.pi)*(sp.sin((n*wo)/2)/((n*wo)/2))*sp.euler((-1j*n*wo)/2)
gt = 0
print(sp.euler)
for i in range(1, 100):
    gt += 2*sp.pi*(((-1j)/n*sp.pi)*(sp.sin((n*wo)/2)/((n*wo)/2))*pow(sp.euler, ((-1j*n*wo)/2))).subs(n, i)

sp.plot(gt)