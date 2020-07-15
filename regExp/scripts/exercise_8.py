"""Write a Python program to replace
whitespaces with an underscore
and vice versa."""

import re

def finder(whatever):
    """replace and compile for the next argument"""
    regex = re.compile('\s')

    if regex.search(whatever):
        print('MATCH:')
        random = whatever.replace(' ', '_')
        print(f'- {random}')
    else:
        print('NO MATCH')

finder('hola soy james')
finder('Python is awesome')
finder('1 2 3 4 5')

