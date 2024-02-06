import numpy as np
import math
import sympy

# 4 Parâmetros de Denavit e Hartenberg

n=4        # número de juntas
N=4*n      # número de parâmetros de Denavit e Hartenberg

a1, alfa1, d1, theta1 = sympy.symbols("a1 alfa1 d1 theta1")

ct1=sympy.cos(theta1)
st1=sympy.sin(theta1)
ca1=1
sa1=0
a1=a1
d1=0

A1=sympy.Matrix([[ct1,-st1*ca1,st1*sa1,a1*ct1],[st1,ct1*ca1,-ct1*sa1,a1*st1],[0,sa1,ca1,d1],[0,0,0,1]])
print(A1)

a2, alfa2, d2, theta2 = sympy.symbols("a2 alfa2 d2 theta2")

ct2=sympy.cos(theta2)
st2=sympy.sin(theta2)
ca2=-1
sa2=0
a2=a2
d2=0

A2=sympy.Matrix([[ct2,-st2*ca2,st2*sa2,a2*ct2],[st2,ct2*ca2,-ct2*sa2,a2*st2],[0,sa2,ca2,d2],[0,0,0,1]])
print(A2)

a3, alfa3, d3, theta3 = sympy.symbols("a3 alfa3 d3 theta3")

ct3=1
st3=0
ca3=1
sa3=0
a3=0
d3=d3

A3=sympy.Matrix([[ct3,-st3*ca3,st3*sa3,a3*ct3],[st3,ct3*ca3,-ct3*sa3,a3*st3],[0,sa3,ca3,d3],[0,0,0,1]])
print(A3)

a4, alfa4, d4, theta4 = sympy.symbols("a4 alfa4 d4 theta4")

ct4=sympy.cos(theta4)
st4=sympy.sin(theta4)
ca4=1
sa4=0
a4=0
d4=d4

A4=sympy.Matrix([[ct4,-st4*ca4,st4*sa4,a4*ct4],[st4,ct4*ca4,-ct4*sa4,a4*st4],[0,sa4,ca4,d4],[0,0,0,1]])
print(A4)

T01=A1
T02=np.matmul(A1,A2)
print(T02)
T03=np.matmul(T02,A3)
print(T03)
T04=np.matmul(T03,A4)
print(T04)
