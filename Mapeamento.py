import numpy as np
import math
import sympy

#Transladado

P_B=[]           #Vetor do ponto P no frame B

P_A_Borg=[]      #Vetor distância entre a origem do frame A e a origem do frame B

P_A=P_B+P_A_Borg #Vetor do ponto P no frame A
#print(P_A)

#Rotacionado

P_B=[0,2,1]      #Vetor do ponto P no frame B

alpha=math.pi/6  #Ângulo de rotação do eixo

Rotx=np.array([[1,0,0],[0,math.cos(alpha),-math.sin(alpha)],[0,math.sin(alpha),math.cos(alpha)]])
Roty=np.array([[math.cos(alpha),0,math.sin(alpha)],[0,1,0],[-math.sin(alpha),0,math.cos(alpha)]])
Rotz=np.array([[math.cos(alpha),-math.sin(alpha),0],[math.sin(alpha),math.cos(alpha),0],[0,0,1]])

R_A_B=Rotx       #Matriz de rotação no eixo x

P_A=np.dot(R_A_B,P_B)    #Vetor do ponto P no frame A
#print(P_A)

#Genérico

P_B=[3,7,0]           #Vetor do ponto P no frame B

P_A_Borg=[10,5,0]     #Vetor distância entre a origem do frame A e a origem do frame B

alpha=math.pi/6       #Ângulo de rotação do eixo

Rotx=np.array([[1,0,0],[0,math.cos(alpha),-math.sin(alpha)],[0,math.sin(alpha),math.cos(alpha)]])
Roty=np.array([[math.cos(alpha),0,math.sin(alpha)],[0,1,0],[-math.sin(alpha),0,math.cos(alpha)]])
Rotz=np.array([[math.cos(alpha),-math.sin(alpha),0],[math.sin(alpha),math.cos(alpha),0],[0,0,1]])

R_A_B=Rotz       #Matriz de rotação no eixo Z

T_A_B=np.array([[R_A_B[0][0],R_A_B[0][1],R_A_B[0][2],P_A_Borg[0]],[R_A_B[1][0],R_A_B[1][1],R_A_B[1][2],P_A_Borg[1]],[R_A_B[2][0],R_A_B[2][1],R_A_B[2][2],P_A_Borg[2]],[0,0,0,1]])

P_B_f=[[P_B[0]],[P_B[1]],[P_B[2]],[1]]  # Ponto B 3x1 para 4x1 (com adição de 1 na última linha)

P_A=np.dot(T_A_B,P_B_f)  #Vetor do ponto P no frame A
#print(P_A)
