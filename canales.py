from itertools import permutations, product
import sys


try:
    inp_A = str(input('Ingrese los caracteres del alfabeto de entrada sin espacios: '))
    out_B = str(input('Ingrese los caracteres del alfabeto de salida sin espacios: '))
    lengthA = len(inp_A)
    lengthB = len(out_B)
except:
    print('Caracteres no validos')

print('\n')
try:
    n = int(input('Ingrese la longitud hasta la que quiere ver la cant. de combinaciones: '))
except:
    print('Cantidad invalida')
    sys.exit()

lensA = []
lensB = []
for i in range(n):
    permA = product(inp_A, repeat= i + 1)
    permB = product(out_B, repeat= i + 1)
    lensA.append(len(list(permA)))
    lensB.append(len(list(permB)))

print('\n')
print('l        A         B\n')
for i in range(n):
    print(f'{i+1}       {lensA[i]}      {lensB[i]}')

"""
#TEST code
perm = product('01*', repeat=2)
  
# Print the obtained permutations  
print(list(perm))
"""