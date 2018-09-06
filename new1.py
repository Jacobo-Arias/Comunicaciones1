import sympy as sp
t=sp.pi*3/2
a=1
b=1
c=1
'''ft = a*sp.cos(2*t) + b*sp.sin(7*t) + c*sp.sin(13*t)
print('f(x)')
sp.pprint(ft)
ft = a*sp.cos(-2*t) + b*sp.sin(-7*t) + c*sp.sin(-13*t)
print('f(-x)')
sp.pprint(ft)
ft = -a*sp.cos(2*t) - b*sp.sin(7*t) - c*sp.sin(13*t)
print('-f(x)')
sp.pprint(ft)
ft = -a*sp.cos(-2*t) - b*sp.sin(-7*t) - c*sp.sin(-13*t)
print('-f(-x)')
sp.pprint(ft)'''

ft = (a*sp.sin(2*t) + b*sp.sin(5*t))**2
print('f(x)')
sp.pprint(ft)
ft = (a*sp.sin(-2*t) + b*sp.sin(-5*t))**2
print('f(-x)')
sp.pprint(ft)
ft = -(a*sp.sin(2*t) - b*sp.sin(5*t))**2
print('-f(x)')
sp.pprint(ft)
ft = -(a*sp.sin(-2*t) - b*sp.sin(-5*t))**2
print('-f(-x)')
sp.pprint(ft)