""" Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the
list of magicians by adding the phrase the Great to each
magician’s name. Call show_magicians() to see that the list
has actually been modified. """

def show_magicians(some_names):
    for name in some_names:
        print(f'- {name.title()}')

def make_great(some_names):
    great_magicians = []
    while some_names:
        new = some_names.pop()
        great = new + ' the GREAT!'
        great_magicians.append(great)

    for name in great_magicians:
        print(f'- {name.title()}')

lista_de_magos = ['james', 'cynthya', 'carolina']

show_magicians(lista_de_magos)
make_great(lista_de_magos)