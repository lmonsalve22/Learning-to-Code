"""Write a Python program that matches
a string that has an a followed by zero
or more b's."""

import re

def finder(string):
    """using 're.match'"""
    regex = re.match('^a[\w]*', string)
    if regex:
        print('We have a MATCH')
    else:
        print('NO MATCH')

finder('abc')
finder('abbc')
finder('abbba')
