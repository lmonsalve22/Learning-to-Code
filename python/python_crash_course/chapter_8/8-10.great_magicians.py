

def show_magicians(some_names):
    for name in some_names:
        print(f'- {name.title()}')

def make_great(some_names):
    great_magicians = []
    while some_names:
        great_magician = some_names.pop()
        great = great_magician.title() + ' ' + 'The great'
        great_magicians.append(great)
        some_names.append(great_magician)

    for magician in great_magicians:
        print(magician)

    

magicians = ['james', 'carolina', 'cynthya']

make_great(magicians)

show_magicians(magicians)


