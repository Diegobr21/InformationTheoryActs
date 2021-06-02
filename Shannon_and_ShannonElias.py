from expansion_binaria import *
import math
from fractions import Fraction

n = int(input('Ingresa la cantidad de frecuencias de entrada: '))

frecuencias = []
for i in range(n):
    frecuencias.append(float(input(f'Ingresa la frecuencia #{i+1}: ')))

F_i = [0 for i in range(len(frecuencias))]

for i in range(len(F_i)):
    if(i != 0):
        F_i[i] = frecuencias[i -1] + F_i[i - 1]

#print(F_i)

def Shannon():
    global frecuencias
    global F_i
    print('Metodo de Shannon')

    l_k = []

    for f in frecuencias:
        l_k.append(math.ceil(math.log(1/f, 2)))
    print('l_k: ', l_k)

    codificacion = []
    codificacion_truncada = []

    for f in F_i: 
        fraccion = str(Fraction(f))
        expansion = expansion_binaria(fraccion)[0]
        cod = ''
        for e in expansion:
            cod += str(e)
        codificacion.append(cod)

    for i in range(len(codificacion)):
        codificacion_truncada.append(codificacion[i][:l_k[i]])
    print(f'codificacion truncada:\n{codificacion_truncada}')

def ShannonElias():
    global frecuencias
    global F_i
    print('Metodo de Shannon-Fano-Elias')

    l_x = []
    for f in frecuencias:
        l_x.append(math.floor(math.log(1/f, 2)) + 1)
    print('l_x: ', l_x)

    F_x = [(frecuencias[i] + F_i[i])/2 for i in range(len(frecuencias))]
    print(F_x)
    codificacion = []
    codificacion_truncada = []

    for f in F_x: 
        fraccion = str(Fraction(f))
        expansion = expansion_binaria(fraccion)[0]
        cod = ''
        for e in expansion:
            cod += str(e)
        codificacion.append(cod)

    for i in range(len(codificacion)):
        codificacion_truncada.append(codificacion[i][:l_x[i]])
    print(f'codificacion truncada:\n{codificacion_truncada}')


#*---------------START----------------*#
x = True
while x == True:
    print('Selecciona:\n1 - Shannon\n2 - Shannon Fano Elias\n')
    opcion = int(input('Seleccion(1 ó 2):  '))
    if(opcion == 1):
        Shannon()
        opcion2 = int(input('1 - seguir, 0 - parar: '))
        if(opcion2 == 0):
            x = False
    if(opcion == 2):
        ShannonElias()
        opcion2 = int(input('1 - seguir, 0 - parar: '))
        if(opcion2 == 0):
            x = False
    else:
        print('Opción no válida')



