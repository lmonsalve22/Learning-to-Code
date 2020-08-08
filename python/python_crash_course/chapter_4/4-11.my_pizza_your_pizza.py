""" Make a copy of original list of pizzas:
1. add a new pizza to the original list
2. add a different pizza to the list friend_pizza
3. print them in diferrent for loops """

pizzas = ['americana', 'hawaina', 'peperoni']

friend_pizzas = pizzas[:]

pizzas.append('peruana')

friend_pizzas.append('italiana')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(f'- {pizza.title()}')

print('My friend\'s favorite pizzas are:')
for f_pizza in friend_pizzas:
    print(f'- {f_pizza.title()}')