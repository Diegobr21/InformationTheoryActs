from fractions import Fraction

def expansion_binaria(fraccion):
    #fraccion = str(input('Ingrese la fracción diadica en formato "1/denominador" :  '))
    try:
        num_fraccion = fraccion.split('/')
        numerador = float(num_fraccion[0])
        denominador = float(num_fraccion[1])
    except:
        pass

    #decimal_diadica = (numerador/denominador)
    fraccion_diadica = Fraction(fraccion)
    print(fraccion_diadica)
    expansion_binaria = []
    erres = []
    r = fraccion_diadica
    r = (r * 2)
    first_r = r

    while r not in erres:
        if(r >= 1):
            erres.append(r)
            r = r - 1
            expansion_binaria.append(1)
        else:
            erres.append(r)
            expansion_binaria.append(0)

        r = (r * 2)
    erres.insert(0, first_r)
    erres.pop(0)

    period_start = erres.index(r) #repeated r


    print('erres : ', erres)
    print('expansion binaria : ', expansion_binaria, 'inicio del periodo en indice: ', period_start)   

#? ---START---
n = int(input('Ingrese la cantidad de frecuencias a sacarles expansion binaria: '))

fracciones = []
for i in range(n):
    f = str(input(f'#{i + 1} - Ingrese la fracción diadica en formato "1/denominador" :  '))
    fracciones.append(f)

for f in fracciones:
    expansion_binaria(f)