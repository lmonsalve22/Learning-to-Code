# Busqueda binaria

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