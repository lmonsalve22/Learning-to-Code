# Definición de una clase

class Persona:

	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def saluda(self, otra_persona):
		return f'Hola {otra_persona.title()}, me llamo {self.nombre.title()}.'

# Uso de la clase:

james = Persona('james', 25)
print(james.saluda('cynthya'))