""" Show the ticket's price according to the input  """
print('=====Welcome to the cinema=====')

age = int(input('Please enter your age: '))

if age < 3:
    print('Ticket is FREE')
elif age <= 12:
    print('Ticket is $10')
else:
    print('Ticket is $15')