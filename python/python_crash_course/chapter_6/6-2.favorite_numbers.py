""" Think of 5 friends and store in a dictionary
their favorite numbers, then print them all """

favorite_numbers = {
    'james' : 1,
    'carolina' : 12,
    'cynthya' : 20,
    'jaimes' : 21,
    'rosario': 40
}

for key, value in favorite_numbers.items():
    print(f'The favorite number of {key.title()} is {value}')