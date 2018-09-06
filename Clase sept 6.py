import sympy as sp

T = 6
W0 = 2*sp.pi/T

t,n = sp.symbols('t n')

a0 = 3*(sp.integrate(t+1,(t,-1,0)) - sp.integrate(t-1,(t,0,1)))/T

#an = (sp.integrate((t+1) * sp.cos(n*W0*t),(t,-1,0)) - sp.integrate((t-1) * sp.cos(n*W0*t),(t,0,1))) * (2/T)
an =(sp.integrate((t+1)*sp.cos(n*W0*t), (t, -1, 0)) - sp.integrate((t-1)*sp.cos(n*W0*t), (t,0,1)))
#sp.pprint(a0)
an = sp.simplify(an)
sp.pprint(an)

gt = a0 + 2

for i in range(1,100):
	gt += (an*sp.cos(n*W0*(t+2))).subs(n,i)


sp.plot(gt) 
