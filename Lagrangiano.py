import numpy as np
import sympy

# Exercício 1

# Parâmetros

q, m, Ic, g, r = sympy.symbols("q m Ic g r")

# Calcular a energia cinética

x=r*sympy.sin(q)
y=-r*sympy.cos(q)
x1=x.diff(q)
y1=y.diff(q)
v=sympy.sqrt(x1**2+y1**2)
print(v)
T= 1/2*m*v**2+1/2*Ic*q.diff(q)
print(T)

# Calcular a energia potencial

P = m*g*y
print(P)

# Calcular o Lagrangiano

L = T-P
print(L)

# Equação dinâmica
