""" Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list 
of magicians’ names. Because the original list will be unchanged, 
return the new list and store it in a separate list. """

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
make_great(lista_de_magos[:])
show_magicians(lista_de_magos)