def primera_letra(lista_de_palabras):
	primeras_letras = []

	for palabra in lista_de_palabras:
		assert type(palabra) == str, f'{palabra} no es str'
		assert len(palabra) > 0, 'No se permiten str vacios'

		primeras_letras.append(palabra[0])

	return primeras_letras

lista = ['james', 'noria', 'velarde']

# Puedes probar con estas listas, para ver la función de assert:
# lista = [10, 'noria', 'velarde']
# lista = ['james', True, 'velarde']
# lista = []

print(primera_letra(lista))