""" Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit 
one place in the world, where would you go? Include a 
block of code that prints the results of the poll. """

data = {}

poll = True

while poll:
    name = input('What\'s your name: ')
    question = input(
        'If you could visit one place in the world, where would you go?: ')
    data[name] = question
    out = input('Continue (y/n): ')
    if out == 'y':
        continue
    else:
        break

for key, value in data.items():
    print(f'{key.upper()}:\n- {value.title()}')
