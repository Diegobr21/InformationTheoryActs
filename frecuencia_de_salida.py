import numpy as np
import sys

# Agregar el vector de frecuencias de entrada
n = int(input('Ingrese la cantidad de frecuencias de entrada: '))
p = []
for x in range(n):
    p.append(float(input(f'p[{x}] = ')))

# Validacion para el arreglo p
"""
if sum(p) != 1:
    print('Las frecuencias de entrada deben sumar 1')
    sys.exit(0)
"""

# Agregar la matriz de probabilidades de transicion
m = n
Q = np.empty((n,m))
for i in range(n):
    for j in range(m):
        Q[i][j] = float(input(f'Q[{i}][{j}] = '))

# Validacion para la matriz de transicion
"""
q_sum = Q.sum(axis = 1)
for k in range(len(q_sum)):
    if q_sum[k] != 1:
        print('Las columnas de la matriz deben sumar 1')
        sys.exit(0)
"""

# Crear matriz global de transicion a partir de la matriz Q
Q_global = np.copy(Q)
for i in range(n):
    for j in range(m):
        Q_global[i][j] = Q_global[i][j] * p[i]


output_frequencies = Q_global.sum(axis = 0)


print(f'\n=== p ===\n {p}\n')
print(f'=== Q ===\n {Q}\n')
print(f'=== Q global ===\n {Q_global}\n')
print(f'=== Frecuencias de salida ===\n {output_frequencies}\n')
