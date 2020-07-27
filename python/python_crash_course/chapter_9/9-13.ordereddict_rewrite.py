""" Start with Exercise 6-4 (page 108), where you used a 
standard dictionary to represent a glossary. Rewrite the program 
using the OrderedDict class and make sure the order of the output 
matches the order in which key-value pairs were added to the dictionary. """

from collections import OrderedDict

glossary = OrderedDict()

glossary['loop'] = 'is a control flow statement for specifying iteration, which allows code to be executed repeatedly.'
glossary['string'] = 'a string is a data type used in programming, such as an integer and floating point unit, but is used to represent text rather than numbers.'
glossary['coffee'] = 'just like ordinary cherries, the coffee fruit is also a so-called stone fruit.'
glossary['python'] = 'python is an interpreted, object-oriented, high-level programming language with dynamic semantics.'
glossary['book'] = 'a book is a medium for recording information in the form of writing or images, typically composed of many pages bound together and protected by a cover.'

for key,value in glossary.items():
    print(f'- {key.title()}:\n\t{value.capitalize()}\n')