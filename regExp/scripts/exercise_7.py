"""Write a Python program that matches
a string that has an 'a' followed by
anything, ending in 'b'."""

import re

def finder(whatever):
    """Using re.compile"""
    regex = re.compile(r'a.*b')
    if regex.search(whatever):
        print('MATCH')
    else:
        print('NO MATCH')

finder('a$b')
finder('a1234b')
finder('a$$$c') #ends with 'c'
