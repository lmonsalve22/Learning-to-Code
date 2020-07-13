"""Write a Python program that matches
a string that has an a followed by one
or more b's."""

import re

def finder(string):
    """using '+' and 're.compile' with 'var.search()'"""
    regex = re.compile(r'^a[\w]+$') #if we want to avoid numbers:[^\d]

    if regex.search(string):
        print('MATCH')
    else:
        print('NO MATCH')

finder('abbbbc')
finder('ab')
finder('bca') #there's no "a" at the beginning
