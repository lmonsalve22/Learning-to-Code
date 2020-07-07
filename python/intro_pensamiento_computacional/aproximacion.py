# Aproximación de soluciones

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

