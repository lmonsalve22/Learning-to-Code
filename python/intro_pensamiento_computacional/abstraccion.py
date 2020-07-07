def enumeracion_exhaustiva(objetivo):

	respuesta = 0

	while respuesta**2 < objetivo:
		respuesta += 1

	if respuesta**2 == objetivo:
		return f'La raíz cuadrada de {objetivo} es {respuesta}'
	else:
		return f'{objetivo} no tiene una raíz cuadrada exacta'

def aproximacion_de_soluciones(objetivo):

	epsilon = 0.01 #0.0001
	paso = epsilon**2
	respuesta = 0.0

	while abs(respuesta**2 - objetivo) >= epsilon and objetivo:
		# print(abs(respuesta**2 - objetivo), respuesta)
		respuesta += paso

	if abs(respuesta**2 - objetivo) >= epsilon:
		return f'No se encontró la ráiz cuadrada {objetivo}'
	else:
		return f'La raíz cuadrada de {objetivo} es {respuesta}'

def busqueda_binaria(objetivo):

	epsilon = 0.01
	bajo = 0.0
	alto = max(1.0, objetivo)
	respuesta = (alto + bajo) / 2

	while abs(respuesta**2 - objetivo) >= epsilon:
		# print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
		if respuesta**2 < objetivo:
			bajo = respuesta
		else:
			alto = respuesta

		respuesta = (alto + bajo) / 2

	return f'La raíz cuadrada del obejtivo es {respuesta}'

print('-----AVERIGUEMOS LA RAIZ CUADRADA DE UN NÚMERO-----')
objetivo = int(input('Por favor introduzca un número: '))
opcion = int(input(f'''\n¿Cual metodo desea usar para saber la raiz cuadrada de {objetivo}:

[1]Enumaración exhaustiva
[2]Aproximación de soluciones
[3]Busqueda binaria

Introduzca 1, 2 o 3 según corresponda: '''))

if opcion == 1:
	print(enumeracion_exhaustiva(objetivo))
elif opcion == 2:
	print(aproximacion_de_soluciones(objetivo))
elif opcion == 3:
	print(busqueda_binaria(objetivo))
else:
	print(f'{opcion} no es una opción valida')
