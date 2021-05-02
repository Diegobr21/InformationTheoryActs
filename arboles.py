import sys

def look_sigmas(sigmas, sigma_index, cant_bits, b):
    for g in sigmas[sigma_index][1]: #agrupacion de los nodos iniciales
        try: #llegamos a un caracter
            node = int(g)
        except: #otro sigma
            b +=1
    x = False
    if(x==True):
        return look_sigmas(sigmas, sigma_index, cant_bits, b)
    else:
        return cant_bits

def arbol_jerarquico(frecuencias):
    frecuencias_copy = list(frecuencias)
    frecuencias_copy.sort(reverse = True)
    for i in range(len(frecuencias_copy)):
        frecuencias_copy[i] = (frecuencias_copy[i], i)
    #list of tuples sorted by frequency 

    sigmas = [] # tuple(sum, [index1, index2])
    i = 0
    while len(frecuencias_copy) > 2: #while its not binary
        new_sigma = (frecuencias_copy[-1][0] + frecuencias_copy[-2][0], f'sigma{i}')
        i += 1
        sigmas.append((new_sigma[0], [frecuencias_copy[-1][1], frecuencias_copy[-2][1]]))
        frecuencias_copy.pop(-1)
        frecuencias_copy.pop(-1)
        frecuencias_copy.append(new_sigma)
        frecuencias_copy.sort(key=lambda x: x[0], reverse = True)
    print(sigmas, frecuencias_copy)

    cant_bits = [1 for i in range(len(frecuencias))]
    b = 1
    for i in range(len(frecuencias_copy)):
        sigma_index = int(frecuencias_copy[i][1].replace('sigma',''))
        for g in sigmas[sigma_index][1]: #agrupacion de los nodos iniciales
            try: #llegamos a un caracter
                node = int(g)
            except: #otro sigma
                b +=1


#*----------------------------Start----------------------------*
n=1
try:
    n = int(input('ingrese la cantidad de caracteres en el alfabeto: '))
    if(n <= 0):
        raise Exception
except:
    print('Ingrese un numero valido')
    sys.exit()

print('Ingrese las frecuencias de entrada de los caracteres')
frecuencias = []
for i in range(n):
    try:
        frecuencias.append(float(input(f'Frecuencia de entrada {i + 1}: ')))
    except:
        frecuencias.append(.1)

if(sum(frecuencias) != 1):
    print('Las frecuencias no suman 1')
    sys.exit()
else:
    print('Datos de entrada correctos')


run = False
while run == False:
    print('Ingrese el tipo de árbol que quiere formar:\n1- jerárquico\n2- balanceado\n3- ternario')
    opcion = int(input('Selección (1, 2 o 3): '))
    opciones = [1, 2, 3]
    if(opcion not in opciones):
        print('Opcion no válida, intente de nuevo')
    else:
        run = True

if(opcion == 1):
    print('Jerárquico')
    arbol_jerarquico(frecuencias)
if(opcion == 2):
    print('Balanceado')
if(opcion == 3):
    print('Ternario')


