import math

# Inserir matriz

r11=0
r12=-math.sqrt(3)/2
r13=0.5
r21=0.5
r22=-math.sqrt(3)/4
r23=-0.75
r31=math.sqrt(3)/2
r32=0.25
r33=math.sqrt(3)/4

R=[[r11,r12,r13], [r21,r22,r23], [r31,r32,r33]]
print(R)

# Ângulos de ZYX (alpha, beta e gamma)

beta = - math.asin(r31)
gamma= math.asin(r32/math.cos(beta))
alpha= math.acos(r11/math.cos(beta))

print(alpha*180/math.pi)
print(beta*180/math.pi)
print(gamma*180/math.pi)

# Ângulos de XYZ (alpha, beta e gamma)

beta = math.asin(r13)
alpha= -math.asin(r12/math.cos(beta))
gamma= math.acos(r33/math.cos(beta))

print(alpha*180/math.pi)
print(beta*180/math.pi)
print(gamma*180/math.pi)