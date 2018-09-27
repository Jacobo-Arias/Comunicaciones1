import sympy as sp
import math

T = 2
wo = 2*math.pi/T
n, t = sp.symbols('n t')
fn = (-1j*(sp.sin(n*wo/2)/n*wo/2)*sp.euler(-1j*n*wo/2))/n*math.pi