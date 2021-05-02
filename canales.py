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
    print('l\tA\tB\n')
    for i in range(n):
        print(f'{i+1}\t{lensA[i]}\t{lensB[i]}')


def alfabetos_irregulares(inputA, inputB, length_c_A):
    try:
        n = int(input('Ingrese la longitud hasta la que quiere ver la cant. de combinaciones: '))
    except:
        print('Cantidad invalida')
        sys.exit()
    print(f'{n} iteraciones para el alfabeto {inputA} y {inputB}')
    """
    partitionsA = int((len(inputA)) / length_c_A )#? Particiones en las que hay que dividir el alfabeto de entrada
    alphabetA = [[] for i in range(partitionsA)]
    charactersA = [c for c in inputA]
    for i in range(len(alphabetA)):
        for j in range(partitionsA):
            alphabetA[i].append(charactersA[0])
            charactersA.pop(0)
    print(alphabetA)
    """







try:
    answer = int(input('Ingresa un "1" si el alfabeto de *salida* es irregular, si no, ingresa otro numero: '))
except:
    print('Ingresa un numero')
    sys.exit()
if(answer == 1):
    irregular = True
else:
    irregular = False

if(irregular): #?--IRREGULAR ALPHABETS
    try:
        caracteres = int(input('Ingresa cuantos diferentes caracteres hay en el alfabeto de salida: '))
        B = [[] for i in range(caracteres)]
        for i in range(caracteres):
            character = str(input(f'Ingresa el caracter #{1+i} sin espacios: '))
            B[i].append(character)
        length_characters_A = int(input('Ingrese la longitud(constante) de los caracteres del alfabeto de entrada: '))
        lenA = int(input('Ingrese cuantos diferentes caracteres hay en el alfabeto de entrada: '))
        A = [[] for i in range(lenA)]
        for i in range(lenA):
            character = str(input(f'Ingresa el caracter #{1+i} sin espacios: '))
            if(len(character) == length_characters_A):
                A[i].append(character)
            else:
                print('No corresponde al tamaño especificado')
                sys.exit()
        
        print('Alfabeto de entrada: \n', A)
        print('Alfabeto de salida: \n', B)
        alfabetos_irregulares(A, B, length_characters_A)

    except:
        print('Caracter o numero invalido')
        sys.exit()

else: #?--REGULAR ALPHABETS
    try:
        inp_A = str(input('Ingrese los caracteres del alfabeto de entrada sin espacios: '))
        out_B = str(input('Ingrese los caracteres del alfabeto de salida sin espacios: '))
        lengthA = len(inp_A)
        lengthB = len(out_B)
        alfabetos_regulares(inp_A, out_B)
    except:
        print('Caracteres no validos')
        sys.exit()


#!Comment everything else and run this code if you want to see how itertools.product() works
"""
#TEST code
perm = product('01*', repeat=2)
  
# Print the obtained permutations  
print(list(perm))
"""