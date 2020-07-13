"""Write a Python program that matches
a string that has an a followed by zero
or one 'b'. """

import re

def finder(string):
    """using '?' and 're.match'"""
    regex = re.match('^a[\w]?.*$', string)

    if regex:
        print('WE HAVE A MATCH')
    else:
        print('WE DON\'T HAVE A MATCH')

finder('abc')
finder('abbbc')
finder('acabbc')
