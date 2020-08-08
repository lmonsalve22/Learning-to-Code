""" store in a python dictionary a glossary and print 
each key and value """

glossary = {
    'loop' : 'is a control flow statement for specifying iteration, which allows code to be executed repeatedly.',
    'string' : 'a string is a data type used in programming, such as an integer and floating point unit, but is used to represent text rather than numbers.',
    'coffee' : 'just like ordinary cherries, the coffee fruit is also a so-called stone fruit.',
    'python' : 'python is an interpreted, object-oriented, high-level programming language with dynamic semantics.',
    'book' : 'a book is a medium for recording information in the form of writing or images, typically composed of many pages bound together and protected by a cover.'
}

for key,value in glossary.items():
    print(f'- {key.title()}:\n\t{value.capitalize()}\n')