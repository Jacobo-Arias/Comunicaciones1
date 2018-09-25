import sympy as sp
T = 2
w0 = 2*sp.pi/T
n,w = sp.symbols('n w')

fn = (-1j/(n*sp.pi)) * (sp.sin(n*w0/2)/(n*w0/2))# * sp.euler(-1j*n*w0/2)

ft = 2*sp.pi

for i in range(1,10):
	ft += (fn*(sp.cos(n*w0/2)-1j*sp.sin(n*w0/2))).subs(n,i)

sp.plot(ft)