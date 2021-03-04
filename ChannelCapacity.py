import math

# Arrays
p = [0.4, 0.5, 0.1]

q = [
    [0.376, 0.016, 0.008],
    [0.005, 0.465, 0.03],
    [0.003, 0.004, 0.093]
]

# Variables
productoI = 0
productoK = 0
dividendo = 0
sumaT = 0
division = 0
sumaK = 0
sumaN = 0

n = len(p)
k = len(q)

# Algorithm
for i in range(n):
    productoK = 0
    for j in range(k):
        dividendo = 0
        for t in range(n):
            sumaT = p[t]*q[t][j]
            dividendo = dividendo + sumaT

        division = (q[i][j]) / dividendo
        sumaK = q[i][j] * math.log10(division)
        productoK = productoK + sumaK
    
    sumaN = p[i] * productoK
    productoI = sumaN + productoI


print(f'\nI(A,B) = {productoI} \n')