""" Modify program from 6-2 so each person can have more
than one favorite number. Then print each person's name along
with their favorite numbers """

favorite_numbers = {
    'james' : [1, 2, 3],
    'carolina' : [12, 13, 14],
    'cynthya' : [20, 21, 22],
    'jaimes' : [21, 31, 32],
    'rosario': [40, 41, 42]
}

for name, number in favorite_numbers.items():
    print(f'{name.title().upper()}')
    for fav_number in number:
        print(f'- {fav_number}')