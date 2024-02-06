import numpy as np
import math
import sympy

# 4 Parâmetros de Denavit e Hartenberg

n=2        # número de juntas
N=4*n      # número de parâmetros de Denavit e Hartenberg

ai=0       # tamanho do elo
alfai=0    # ângulo de elo
di=0       # offset do elo
thetai=0   # ângulo da junta

cti=sympy.cos(thetai)
sti=sympy.sin(thetai)
cai=sympy.cos(alfai)
sai=sympy.sin(alfai)

a1, alfa1, d1, theta1 = sympy.symbols("a1 alfa1 d1 theta1")

ct1=sympy.cos(theta1)
st1=sympy.sin(theta1)
ca1=sympy.cos(0)
sa1=sympy.sin(0)
a1=a1
d1=0

A1=sympy.Matrix([[ct1,-st1*ca1,st1*sa1,a1*ct1],[st1,ct1*ca1,-ct1*sa1,a1*st1],[0,sa1,ca1,d1],[0,0,0,1]])
print(A1)

a2, alfa2, d2, theta2 = sympy.symbols("a2 alfa2 d2 theta2")

ct2=sympy.cos(theta2)
st2=sympy.sin(theta2)
ca2=sympy.cos(0)
sa2=sympy.sin(0)
a2=a2
d2=0

A2=sympy.Matrix([[ct2,-st2*ca2,st2*sa2,a2*ct2],[st2,ct2*ca2,-ct2*sa2,a2*st2],[0,sa2,ca2,d2],[0,0,0,1]])
print(A2)

T02=np.matmul(A1,A2)
print(T02)






















