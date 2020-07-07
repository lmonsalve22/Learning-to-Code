# enumeración exhaustiva

def enumeracion_exhaustiva(objetivo):

	respuesta = 0

	while respuesta**2 < objetivo:
		respuesta += 1

	if respuesta**2 == objetivo:
		return f'La raíz cuadrada de {objetivo} es {respuesta}'
	else:
		return f'{objetivo} no tiene una raíz cuadrada exacta'
