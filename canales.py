from itertools import permutations, product
import sys

def alfabetos_regulares(inputA, outputB):
    print('\n')
    try:
        n = int(input('Ingrese la longitud hasta la que quiere ver la cant. de combinaciones: '))
    except:
        print('Cantidad invalida')
        sys.exit()

    lensA = []
    lensB = []
    for i in range(n):
        permA = product(inputA, repeat= i + 1)
        permB = product(outputB, repeat= i + 1)
        lensA.append(len(list(permA)))
        lensB.append(len(list(permB)))

    print('\n')
    print('l        A         B\n')
    for i in range(n):
        print(f'{i+1}       {lensA[i]}      {lensB[i]}')

def alfabetos_irregulares(inputA, inputB):
    print('Ok')



try:
    answer = int(input('Ingresa un "1" si el alfabeto de salida es irregular, si no, ingresa otro numero: '))
except:
    print('Ingresa un numero')
    sys.exit()
if(answer == 1):
    irregular = True

if(irregular):
    try:
        caracteres = int(input('Ingresa cuantos diferentes caracteres hay en el alfabeto: '))
        B = [[] for i in range(caracteres)]
        for i in range(caracteres):
            caracter = str(input(f'Ingresa el caracter #{1+i} sin espacios: '))
            B[i].append(caracter)
        print('Alfabeto de salida: \n', B)
    except:
        print('Caracter o numero invalido')

else:
    try:
        inp_A = str(input('Ingrese los caracteres del alfabeto de entrada sin espacios: '))
        out_B = str(input('Ingrese los caracteres del alfabeto de salida sin espacios: '))
        lengthA = len(inp_A)
        lengthB = len(out_B)
    except:
        print('Caracteres no validos')




"""
#TEST code
perm = product('01*', repeat=2)
  
# Print the obtained permutations  
print(list(perm))
"""