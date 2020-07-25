"""  Make a list of magician’s names. Pass the list to a 
function called show_magicians() , which prints the name of
each magician in the list."""


def show_magicians(some_names):
    for name in some_names:
        print(f'- {name.title()}')

magicians = ['james', 'carolina', 'cynthya']
show_magicians(magicians)