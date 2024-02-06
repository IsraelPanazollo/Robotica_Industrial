import numpy as np
import sympy

#Ângulo-Eixo

alpha, beta, gamma = sympy.symbols("alpha beta gamma")

Rotz=sympy.Matrix([[sympy.cos(alpha),-sympy.sin(alpha),0],[sympy.sin(alpha),sympy.cos(alpha),0],[0,0,1]])
Roty=sympy.Matrix([[sympy.cos(beta),0,sympy.sin(beta)],[0,1,0],[-sympy.sin(beta),0,sympy.cos(beta)]])
Rotx=sympy.Matrix([[1,0,0],[0,sympy.cos(gamma),-sympy.sin(gamma)],[0,sympy.sin(gamma),sympy.cos(gamma)]])

R1=np.matmul(Rotx,Roty)
#print(R1)
Euler=np.matmul(R1,Rotz)
print(Euler)