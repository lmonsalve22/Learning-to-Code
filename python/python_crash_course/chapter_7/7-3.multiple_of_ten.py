""" Ask the user for a number, and then report whether the
number is a multiple of 10 or not """

number = int(input('Please enter a number: '))

if number % 10 == 0:
    print(f'{number} is multiple of ten')
else:
    print(f'Sorry, but {number} is not multiple of ten')