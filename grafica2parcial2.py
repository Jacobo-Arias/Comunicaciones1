import sympy as sp
T = 2
wo = (2*sp.pi)/T
w = sp.symbols('w')
gt = 0
for i in range(0, 30, 2):
    gt += (2*sp.pi*(wo/(2*sp.pi))).subs(w, i)
sp.plot(gt)