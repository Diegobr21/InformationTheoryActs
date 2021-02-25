import math
import sys

print('Calculadora de Información Mutua y Entropía')
print('Seleccione el tipo de procesos ingresando el número correspondiente')

validation = False

try:
	
	opcion_tipo = int(input('1 - Cuantificables \n2 - Transmisión de datos binaria \n3 - Transmisión entre estados\n: '))

	if(opcion_tipo == 1):
	    base = 10
	elif(opcion_tipo == 2):
	    base = 2
	elif(opcion_tipo == 3):
	    base = math.e
	else:
		validation = True

except Exception as e:
	validation = True
	

if validation:
	print('Ingrese una opción valida (1, 2 o 3)')
	sys.exit()


try:
	n = int(input('¿cuantos eventos?  : '))
	if n > 50:
		validation = input('Desea ingresar una cantidad de eventos tan grande? (s/n): ')
		if validation == 's':
			pass
		else:
			sys.exit()

	if n <= 0:
		print('Ingrese un valor entero positivo')
		sys.exit()
		
except Exception as e:
	print('Ingrese un valor entero')
	sys.exit()



equiprobable = False
probabilidad_eventos = []

try:
	opcion = int(input('Ingresa un "1" si los eventos son equiprobables  : '))
	if(opcion == 1):
	    equiprobable = True

except Exception as e:
	equiprobable = False



if(equiprobable):
	try:
		prob = float(input(f'Ingrese la probabilidad de los eventos: '))
		probabilidad_eventos.append(prob)

		if (prob > 1) or (prob < 0):
			print('Ingrese una probabilidad valida (entre 0 y 1)')
			sys.exit()

	except Exception as e:
		print('Ingrese un valor valido')
		sys.exit()
	
else:
	for i in range(n):
		try:
			prob = float(input(f'Probabilidad del evento {i}: '))
			probabilidad_eventos.append(prob)

			if (prob > 1) or (prob < 0):
				print('Ingrese una probabilidad valida (entre 0 y 1)')
				sys.exit()

		except Exception as e:
			print('Ingrese un valor valido')
			sys.exit()

        

#*Función para obtener ambos resultados
def info_y_entro(baselog, n, probabilidades, equip:False):
    if(equip):
        infomutua = (-math.log(probabilidades[0], baselog)) * n
        entropia = infomutua * probabilidades[0]

        return infomutua, entropia
    else:
        infomutua_lista = []
        entropia_lista = []
        for i in range(n):
            info = (-math.log(probabilidades[i], baselog))
            entrop = info * probabilidades[i]
            infomutua_lista.append(info)
            entropia_lista.append(entrop)

        infomutua = sum(infomutua_lista)
        entropia = sum(entropia_lista)

        return infomutua, entropia


results = info_y_entro(base, n, probabilidad_eventos, equiprobable)

print('\n')
if(base == 10):
    print(f'Informacion mutua: {results[0]} hartleys/s\nEntropia: {results[1]} h/s')
elif(base == 2):
    print(f'Informacion mutua: {results[0]} bits/s\nEntropia: {results[1]} b/s')
else:
    print(f'Informacion mutua: {results[0]} nats/s\nEntropia: {results[1]} n/s')