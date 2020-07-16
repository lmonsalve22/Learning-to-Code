"""Write a Python program to remove everything 
except alphanumeric characters from a string."""

import re

def finder(whatever):
    """Using a re.compile and var.sub"""
    regex = re.compile(r'[\W]+')
    print(regex.sub('', whatever))

finder('?\\\James Noria·$%25')
finder('$$$$###1%2&3/5|6')