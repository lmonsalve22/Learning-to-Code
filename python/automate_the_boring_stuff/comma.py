spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(unalista):
	contador = 0
	juntar = ''
	#definiendo la coma
	while contador < len(unalista) -2:
		juntar += unalista[contador] + ', '
		contador += 1
	#definiendo el 'and' y el punto final(.)
	juntar += unalista[-2] + ' and '
	juntar += unalista[-1] + '. '
	print(juntar) #puede usarse return

comma(spam)
