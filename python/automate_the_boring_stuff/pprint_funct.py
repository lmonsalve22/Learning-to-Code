import pprint

message = 'Hola soy James Noria'

count = {}

for caracteres in message:
	count.setdefault(caracteres, 0)
	count[caracteres] += 1

pprint.pprint(count)