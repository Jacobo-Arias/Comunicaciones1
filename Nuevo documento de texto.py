import sympy as sp
t = sp.symbols('t')
a=1
b=1
c=1
ft = (a*sp.sin(2*t) + b*sp.sin(5*t))**2
sp.plot(ft)