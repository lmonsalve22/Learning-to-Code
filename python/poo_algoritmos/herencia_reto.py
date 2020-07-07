# Reto propuesto en la clase de Herencia

class Autos:

	def __init__(self, marca, modelo, color):
		self.marca = marca
		self.modelo = modelo
		self.color = color

	def encendido(self):
		return f'Su {self.marca} {self.modelo} se esta encendiendo...'

	def llenar_gasolina(self, tipo=True):
		self.tipo = tipo
		if tipo:
			return 'Se esta llenando gasolina de 95oct'
		else:
			return 'Se esta llenando gasolina de 85oct'

class Autos_electricos(Autos):
	
	def __init__(self, marca, modelo, color):
 		super().__init__(marca, modelo, color)

	def cargar_bateria(self, completo=True):
		self.completo = completo
		if self.completo:
			return 'Carga completa, puede seguir su viaje'
		else:
			return 'Aun necesito cargar más'

if __name__ == '__main__':
	
	auto_1 = Autos('Tesla', '2020', 'Rojo')
	print(auto_1.encendido())
	print(auto_1.llenar_gasolina(tipo=False))

	auto_2 = Autos_electricos('Toyota', '2030', 'Blanco')
	print(auto_2.encendido())
	print(auto_2.cargar_bateria(completo=False))