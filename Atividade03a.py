import numpy as np
import math

#Ângulo-Eixo

alpha=math.pi/2    # rotação de 90º no eixo fixo Z0
beta=math.pi/6     # rotação de 30º no eixo fixo Y0
gamma=math.pi/3    # rotação de 60º no eixo fixo X0

Rotz=np.array([[math.cos(alpha),-math.sin(alpha),0],[math.sin(alpha),math.cos(alpha),0],[0,0,1]])
Roty=np.array([[math.cos(beta),0,math.sin(beta)],[0,1,0],[-math.sin(beta),0,math.cos(beta)]])
Rotx=np.array([[1,0,0],[0,math.cos(gamma),-math.sin(gamma)],[0,math.sin(gamma),math.cos(gamma)]])
print(Rotz)
print(Roty)
print(Rotx)

# Regra para composição de transformações rotacionais

R1=np.matmul(Rotx,Roty)
R=np.matmul(R1,Rotz)
print(R)

Theta_c=math.degrees(math.acos((R[0][0]+R[1][1]+R[2][2]-1)/2))
print(Theta_c)
Theta_t=Theta_c*math.pi/180

K1=1/(2*math.sin(Theta_t))
print(K1)
K2=[R[2][1]-R[1][2],R[0][2]-R[2][0],R[1][0]-R[0][1]]
K=np.dot(K1,K2)
print(K)

#Conferência

t=[0,0,0]
K=[0.5774,-0.2113,0.7887]
Theta=120*math.pi/180

Kx=K[0]
Ky=K[1]
Kz=K[2]
vt=1-math.cos(Theta)
ct=math.cos(Theta)
st=math.sin(Theta)

Rk=np.array([[Kx*Kx*vt+ct,Kx*Ky*vt-Kz*st,Kx*Kz*vt+Ky*st],[Ky*Kx*vt+Kz*st,Ky*Ky*vt+ct,Ky*Kz*vt-Kx*st],[Kz*Kx*vt-Ky*st,Kz*Ky*vt+Kx*st,Kz*Kz*vt+ct]])
print(Rk)

