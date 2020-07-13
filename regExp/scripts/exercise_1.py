"""Write a Python program to check that
a string contains only a certain set of
characters (in this case a-z, A-Z and 0-9)."""

import re

def finder(string):
    """using 're.compile' and 'var.search()'"""

    regex = re.compile(r'^[A-Za-z\d]+$')
    result = regex.search(string)

    if result:
        return 'MATCH'
    else:
        return 'NO MATCH'

print(finder('ABCDEFGabcdef1235'))
print(finder('##@@@#')) #there's a symbol
