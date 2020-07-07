stuff = {'rope': 10, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def inventario(undiccionario):
	"""Mostrar un inventario y su total de objetos"""
	#Por preferencia, uso una lista para la suma total de objetos
	suma_total = []
	print('INVENTARIO:\n')
	for key, value in undiccionario.items():
		print(f'-> {key.title()}: {value}')
		suma_total.append(value)
	print(f'En su inventario hay: {sum(suma_total)} objetos') #puede usarse return

inventario(stuff) #En caso de return, usar print(def)


