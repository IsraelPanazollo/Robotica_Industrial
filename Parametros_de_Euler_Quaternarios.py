import numpy as np
import math
import sympy

#Parâmetros de Euler / Quaternários

K=[1,0,0]
Theta=math.pi/3

e1=K[0]*math.sin(Theta/2)
e2=K[1]*math.sin(Theta/2)
e3=K[2]*math.sin(Theta/2)
e4=math.cos(Theta/2)

print(e1)
print(e2)
print(e3)
print(e4)

r11=1-2*e2**2-2*e3**2
r12=2*(e1*e2-e3*e4)
r13=2*(e1*e3-e2*e4)
r21=2*(e1*e2+e3*e4)
r22=1-2*e1**2-2*e3**2
r23=2*(e2*e3-e1*e4)
r31=2*(e1*e3-e2*e4)
r32=2*(e2*e3-e1*e4)
r33=1-2*e1**2-2*e2**2

Re=np.array([[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]])
print(Re)

#Conferência

e4_t=1/2*math.sqrt(1+r11+r22+r33)
e1_t=(r32-r23)/(4*e4_t)
e2_t=(r13-r31)/(4*e4_t)
e3_t=(r21-r12)/(4*e4_t)

print(e1_t)
print(e2_t)
print(e3_t)
print(e4_t)
