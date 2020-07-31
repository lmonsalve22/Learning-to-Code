""" Write a program that reads the files you found at Project 
Gutenberg and determines how many times the word 'the' appears in each text. """

filename = 'dracula.txt'

with open(filename) as f:
    lines = f.read()

how_many = lines.lower().count('the')
print(f'Inside the {filename} the word "the" was found {how_many} times')