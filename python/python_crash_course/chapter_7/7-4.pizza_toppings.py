""" Write a loop that prompts the user to enter a series of pizza
toppings until they enter quit value. """

flag = True

pizza_toppings = []

while flag:
    print('Add a topping for your pizza')
    topping = input('Enter the topping: ')
    pizza_toppings.append(topping)
    print(f'Nice, {topping} added')
    loop = input('Continue? (y/n): ') #like 'quit'
    if loop == 'y':
        continue
    else:
        break

print('All the toppings are:')
for pizza_topping in pizza_toppings:
    print(f'- {pizza_topping}')