import numpy as np
import math
import sympy

#Eixo-Ângulo

K=[0.707,0.707,0]
Theta=math.pi/6
t=[0,0,0]

Kx=K[0]
Ky=K[1]
Kz=K[2]
vt=1-math.cos(Theta)
ct=math.cos(Theta)
st=math.sin(Theta)

Rk=np.array([[Kx*Kx*vt+ct,Kx*Ky*vt-Kz*st,Kx*Kz*vt+Ky*st],[Ky*Kx*vt+Kz*st,Ky*Ky*vt+ct,Ky*Kz*vt-Kx*st],[Kz*Kx*vt-Ky*st,Kz*Ky*vt+Kx*st,Kz*Kz*vt+ct]])
print(Rk)

Tab=np.array([[Rk[0][0],Rk[0][1],Rk[0][2],t[0]],[Rk[1][0],Rk[1][1],Rk[1][2],t[1]],[Rk[2][0],Rk[2][1],Rk[2][2],t[2]],[0,0,0,1]])
print(Tab)

#Conferência

r11=Kx*Kx*vt+ct
r12=Kx*Ky*vt-Kz*st
r13=Kx*Kz*vt+Ky*st
r21=Ky*Kx*vt+Kz*st
r22=Ky*Ky*vt+ct
r23=Ky*Kz*vt-Kx*st
r31=Kz*Kx*vt-Ky*st
r32=Kz*Ky*vt+Kx*st
r33=Kz*Kz*vt+ct

Theta_c=math.degrees(math.acos((r11+r22+r33-1)/2))
print(Theta_c)
Theta_t=Theta_c*math.pi/180

K1=1/(2*math.sin(Theta_t))
print(K1)
K2=[r32-r23,r13-r31,r21-r12]
K=np.dot(K1,K2)
print(K)