import numpy as np
import math

#Ângulo-Eixo

#a)
alpha=math.pi/18       # Ângulo de 10º
beta=math.pi/9         # Ângulo de 20º
gamma=math.pi/6        # Ângulo de 30º

Rotz=np.array([[math.cos(alpha),-math.sin(alpha),0],[math.sin(alpha),math.cos(alpha),0],[0,0,1]])
Roty=np.array([[math.cos(beta),0,math.sin(beta)],[0,1,0],[-math.sin(beta),0,math.cos(beta)]])
Rotx=np.array([[1,0,0],[0,math.cos(gamma),-math.sin(gamma)],[0,math.sin(gamma),math.cos(gamma)]])

#EulerZYX=Rotz@Roty@Rotx  #Multiplicação das matrizes
#print(EulerZYX)

R1=np.matmul(Rotz,Roty)
R=np.matmul(R1,Rotx)    #Multiplicação das matrizes
print(R)

#b
alpha=math.pi/6         # Ângulo de 30º
beta=math.pi/2          # Ângulo de 90º
gamma=-math.pi*55/180   # Ângulo de-55º

Rotz=np.array([[math.cos(alpha),-math.sin(alpha),0],[math.sin(alpha),math.cos(alpha),0],[0,0,1]])
Roty=np.array([[math.cos(beta),0,math.sin(beta)],[0,1,0],[-math.sin(beta),0,math.cos(beta)]])
Rotx=np.array([[1,0,0],[0,math.cos(gamma),-math.sin(gamma)],[0,math.sin(gamma),math.cos(gamma)]])

#EulerZYX=Rotz@Roty@Rotx  #Multiplicação das matrizes
#print(EulerZYX)

R1=np.matmul(Rotz,Roty)
R=np.matmul(R1,Rotx)      #Multiplicação das matrizes
print(R)