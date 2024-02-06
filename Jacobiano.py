import numpy as np
import sympy

# Exercício 3

# Parâmetros de Denavit-Hartenberg

n=3        # número de juntas
N=4*n      # número de parâmetros de Denavit e Hartenberg

a1, alfa1, d1, theta1 = sympy.symbols("a1 alfa1 d1 theta1")

ct1=sympy.cos(theta1)
st1=sympy.sin(theta1)
ca1=0
sa1=1
a1=0
d1=0

a2, alfa2, d2, theta2 = sympy.symbols("a2 alfa2 d2 theta2")

ct2=sympy.cos(theta2)
st2=sympy.sin(theta2)
ca2=1
sa2=0
a2=a2
d2=0

a3, alfa3, d3, theta3 = sympy.symbols("a3 alfa3 d3 theta3")

ct3=sympy.cos(theta3)
st3=sympy.sin(theta3)
ca3=1
sa3=0
a3=a3
d3=0

# Matrizes de transformação homogênea

A1=sympy.Matrix([[ct1,-st1*ca1,st1*sa1,a1*ct1],[st1,ct1*ca1,-ct1*sa1,a1*st1],[0,sa1,ca1,d1],[0,0,0,1]])
#print(A1)
A2=sympy.Matrix([[ct2,-st2*ca2,st2*sa2,a2*ct2],[st2,ct2*ca2,-ct2*sa2,a2*st2],[0,sa2,ca2,d2],[0,0,0,1]])
#print(A2)
A3=sympy.Matrix([[ct3,-st3*ca3,st3*sa3,a3*ct3],[st3,ct3*ca3,-ct3*sa3,a3*st3],[0,sa3,ca3,d3],[0,0,0,1]])
#print(A3)

T01=A1
#print(T01)
T02=np.matmul(A1,A2)
#print(T02)
T03=np.matmul(T02,A3)
#print(T03)

# Valores para o Jacobiano

R00=sympy.Matrix([[1,0,0],[0,1,0],[0,0,1]])
#print(R00)
R01=sympy.Matrix([[T01[0],T01[1],T01[2]],[T01[4],T01[5],T01[6]],[T01[8],T01[9],T01[10]]])
#print(R01)
R02=sympy.Matrix([[T02[0][0],T02[0][1],T02[0][2]],[T02[1][0],T02[1][1],T02[1][2]],[T02[2][0],T02[2][1],T02[2][2]]])
#print(R02)
aux=sympy.Matrix([[0],[0],[1]])

O0=sympy.Matrix([[0],[0],[0]])
#print(O0)
O1=sympy.Matrix([[T01[3]],[T01[7]],[T01[11]]])
#print(O1)
O2=sympy.Matrix([[T02[0][3]],[T02[1][3]],[T02[2][3]]])
#print(O2)
O3=sympy.Matrix([[T03[0][3]],[T03[1][3]],[T03[2][3]]])
#print(O3)

jw1=np.matmul(R00,aux)
#print(jw1)
jw2=np.matmul(R01,aux)
#print(jw2)
jw3=np.matmul(R02,aux)
#print(jw3)

O30=O3-O0
#print(O30)
O31=O3-O1
#print(O31)
O32=O3-O2
#print(O32)

ax=jw1[0][0]
ay=jw1[1][0]
az=jw1[2][0]
S1=sympy.Matrix([[0,-az,ay],[az,0,-ax],[-ay,ax,0]])
#print(S1)

ax=jw2[0][0]
ay=jw2[1][0]
az=jw2[2][0]
S2=sympy.Matrix([[0,-az,ay],[az,0,-ax],[-ay,ax,0]])
#print(S2)

ax=jw3[0][0]
ay=jw3[1][0]
az=jw3[2][0]
S3=sympy.Matrix([[0,-az,ay],[az,0,-ax],[-ay,ax,0]])
#print(S3)

jv1=np.matmul(S1,O30)
#print(jv1)
jv2=np.matmul(S2,O31)
#print(jv2)
jv3=np.matmul(S3,O32)
#print(jv3)

# Matriz do Jacobiano

a11=jv1[0][0]
a12=jv2[0][0]
a13=jv3[0][0]
a21=jv1[1][0]
a22=jv2[1][0]
a23=jv3[1][0]
a31=jv1[2][0]
a32=jv2[2][0]
a33=jv3[2][0]
a41=jw1[0][0]
a42=jw2[0][0]
a43=jw3[0][0]
a51=jw1[1][0]
a52=jw2[1][0]
a53=jw3[1][0]
a61=jw1[2][0]
a62=jw2[2][0]
a63=jw3[2][0]

J=sympy.Matrix([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33],[a41,a42,a43],[a51,a52,a53],[a61,a62,a63]])
print(J)


