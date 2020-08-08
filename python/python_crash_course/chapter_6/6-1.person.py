""" Use a dictionay to store information about
a person and print each peace of info """

person = {
    'first_name': 'james',
    'last_name': 'noria',
    'age': 25,
    'city' : 'huanuco'
}

for key, value in person.items():
    print(f'{key}:{value}')
