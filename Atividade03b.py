import numpy as np
import math

r11=1/math.sqrt(2)
r12=0
r13=1/math.sqrt(2)
r21=-1/2
r22=1/math.sqrt(2)
r23=1/2
r31=-1/2
r32=-1/math.sqrt(2)
r33=1/2

R=[[r11,r12,r13], [r21,r22,r23], [r31,r32,r33]]

print(R)

e4=1/2*math.sqrt(1+r11+r22+r33)
e1=(r32-r23)/(4*e4)
e2=(r13-r31)/(4*e4)
e3=(r21-r12)/(4*e4)

print(e1)
print(e2)
print(e3)
print(e4)

s=e1**2+e2**2+e3**2+e4**2
print(s)

Theta=math.acos(e4)*2
print(Theta)
Th=Theta*180/math.pi
print(Th)

kx=e1/math.sin(Theta/2)
ky=e2/math.sin(Theta/2)
kz=e3/math.sin(Theta/2)

K=[kx,ky,kz]
print(K)

#COnferência

K=[-0.6785983445458469, 0.6785983445458469, -0.28108463771482023]
Theta=1.0960568152406256
t=[0,0,0]

Kx=K[0]
Ky=K[1]
Kz=K[2]
vt=1-math.cos(Theta)
ct=math.cos(Theta)
st=math.sin(Theta)

Rk=np.array([[Kx*Kx*vt+ct,Kx*Ky*vt-Kz*st,Kx*Kz*vt+Ky*st],[Ky*Kx*vt+Kz*st,Ky*Ky*vt+ct,Ky*Kz*vt-Kx*st],[Kz*Kx*vt-Ky*st,Kz*Ky*vt+Kx*st,Kz*Kz*vt+ct]])
print(Rk)

r11=1-2*e2**2-2*e3**2
r12=2*(e1*e2-e3*e4)
r13=2*(e1*e3+e2*e4)
r21=2*(e1*e2+e3*e4)
r22=1-2*e1**2-2*e3**2
r23=2*(e2*e3-e1*e4)
r31=2*(e1*e3-e2*e4)
r32=2*(e2*e3+e1*e4)
r33=1-2*e1**2-2*e2**2

Re=np.array([[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]])
print(Re)