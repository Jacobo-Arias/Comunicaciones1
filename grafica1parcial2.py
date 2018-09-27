import sympy as sp
A = 2
T = 4
w = sp.symbols('w')
to = 1
gt = 0
for i in range(0, 30):
    gt += ((A*T)/2)*((sp.sin((w*T)/4))/((w*T)/4))*sp.cos(w*to).subs(w, i)
sp.plot(gt)