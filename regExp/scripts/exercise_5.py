"""Write a Python program to find sequences
of lowercase letters joined with a underscore."""

import re

def finder(whatever):
    """Using 're.compile'"""
    regex = re.compile(r'^[a-z_]*$')

    if regex.search(whatever):
        print('MATCH')
    else:
        print('NO MATCH')

finder('a_b_c')
finder('b_b_a')
finder('a_B_c') #uppercase
