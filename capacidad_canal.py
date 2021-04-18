import math

p = [0.2033, 0.3433, 0.2127, 0.2407]

n = 4
k = 4

q = [[0.19,	0.0033333333, 0.0033333333, 0.0033333333], 
[0.0058333333333, 0.3325, 0.00583333333333333, 0.00583333333333333], 
[0.0035, 0.0035, 0.1995, 0.0035], [0.004, 0.004, 0.004, 0.228]]

D = [0,0,0,0]
I = 0
for i in range(n):
    for j in range(k):
        D[i] += q[i][j]* (math.log10(q[i][j]/(p[0]*q[0][j] + p[1]*q[1][j] + p[2]*q[2][j])))
    I += p[i] * D[i]
print('Información mutua a maximizar para obtener la capacidad de canal: ', I)