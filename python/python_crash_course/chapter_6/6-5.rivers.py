""" Make a dictionary containing three major rivers and
print them as the following way: """

rivers = {
    'nile' : 'egypt',
    'amazonas' : 'peru',
    'missisipi' : 'usa'
}

for key, value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}')

print('The rivers are:')
for key in rivers.keys():
    print('- ',key.title())

print('The countries are:')
for value in rivers.values():
    print('- ',value.title())