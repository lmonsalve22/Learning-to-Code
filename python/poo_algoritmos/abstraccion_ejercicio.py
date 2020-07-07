# Ejercicio a modo práctica sobre abstracción

# Definiendo una clase que nos permite ver Netflix en un SmartTv

class Netflix:

	def __init__(self, marca_tv):
		self.marca_tv = marca_tv

	def ver_catalogo(self):
		self._prender_tv()
		self._conectar_wifi()
		self._smart_hub()
		self._abrir_netflix()

	def _prender_tv(self):
		print(f'Su TV {self.marca_tv.upper()} se esta encendiendo. BIENVENIDO')
	
	def _conectar_wifi(self):
		print('Conectando a la red wifi...')
	
	def _smart_hub(self):
		print('Smart Hub = Accediendo a Netflix')
	
	def _abrir_netflix(self):
		print('¿Que desea ver hoy?')

if __name__ == '__main__':
	
	lg = Netflix('lg')
	lg.ver_catalogo()
