# Ejercicio propuesto por el tutor de curso, durante la clase

class Automovil:

	def __init__(self, modelo, marca, color):
		self.modelo = modelo 
		self.marca = marca 
		self.color = color
		self._estado = True

	def encendido(self):
		return f'Su {self.marca.title()} del {self.modelo} esta encendido'

	def estado_del_automovil(self, _estado):
		if self._estado:
			return 'Auto en movimiento'
		else:
			return 'Auto en reposo'

	def acelerar(self, tipo='despacio'):
		if tipo == 'rapida':
			return 'Inyectando gasolina de 10oct'
		else:
			return 'Inyectando gasolina de 3oct'

	def frenar_auto(self, velocidad_de_frenado):
		self.velocidad_de_frenado = velocidad_de_frenado
		if velocidad_de_frenado == 'rapido':
			return 'Hemos hecho un frenado brusco, pero estamos bien'
		elif velocidad_de_frenado == 'lento':
			return 'Maneje con cuidado'
		else:
			return 'espero estes bien'

if __name__ == '__main__':
	
	mi_carro = Automovil('2020', 'Tesla', 'Azul')
	print(mi_carro.encendido())
	print(mi_carro.estado_del_automovil(True))
	print(mi_carro.acelerar('rapida'))
	print(mi_carro.frenar_auto('lento'))