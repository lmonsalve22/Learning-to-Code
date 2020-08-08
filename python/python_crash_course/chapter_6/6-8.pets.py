""" Make three dictionaries representing different pets, and
store all three dictionaries in a list called pets. Loop through
your list of pets. As you loop through the list, print everything
you know about each pet """

pets = []

chulu = {
    'kind': 'cat',
    'owner': 'james',
    'name' : 'chulu'
}
pets.append(chulu)
laica = {
    'kind': 'dog',
    'owner': 'luis',
    'name' : 'laica'
}
pets.append(laica)
mickey = {
    'kind': 'mouse',
    'owner': 'walt',
    'name' : 'mickey'
}
pets.append(mickey)

for pet in pets:
    name = pet['name'].title()
    owner = pet['owner'].title()
    kind = pet['kind'].title()
    print(f'{name.upper()}:\n- Owner: {owner}\n- Kind: {kind}')
