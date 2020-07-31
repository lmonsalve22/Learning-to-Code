""" Write a program that reads the file and prints what you wrote
three times. Print the contents once by reading in the entire file,
once by looping over the file object, and once by storing the lines
in a list and then working with them outside the with block. """

filename = 'learning_python.txt'

# Reading in the entire file
with open(filename) as f:
    content = f.read()
    print(content)

# Looping over the file object
with open(filename) as f:
    for line in f:
        print(f'\n{line.rstrip()}')

# Storing the lines in a list
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())
