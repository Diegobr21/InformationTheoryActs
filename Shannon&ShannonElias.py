from expansion_binaria import *

n = int(input('Ingresa la cantidad de frecuencias de entrada: '))

frecuencias = []
for i in range(n):
    frecuencias.append(int(input(f'Ingresa la frecuencia #{i+1}')))

F_i = [0 for i in range(len(frecuencias))]

for i in range(len(F_i)):
    if(i != 0):
        F_i[i] = frecuencias[i -1] + F_i[i - 1]

print(F_i)


