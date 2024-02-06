import math
import sympy

# 4 Parâmetros de Denavit e Hartenberg

n=0         # número de juntas
N=4*n       # número de parâmetros de Denavit e Hartenberg

a_i=0       # tamanho do elo
alfa_i=0    # ângulo de elo
d_i=0       # offset do elo
theta_i=0   # ângulo da junta

ca=math.cos(alfa_i)
ct=math.cos(theta_i)
sa=math.sin(alfa_i)
st=math.sin(theta_i)

A_i=sympy.Matrix([[ct,-st*ca,st*sa,a_i*ct],[st,ct*ca,-ct*sa,a_i*st],[0,sa,ca,d_i],[0,0,0,1]])

print(A_i)






