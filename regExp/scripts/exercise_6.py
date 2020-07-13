"""Write a Python program to find
the sequences of one upper case letter
followed by lower case letters."""

import re

def finder(whatever):
    """Using re.match"""
    regex = re.match('^[A-Z].*$', whatever)
    if regex:
        print('MATCH')
    else:
        print('NO MATCH')

finder('Abcdef')
finder('abcde')
finder('Cba')
