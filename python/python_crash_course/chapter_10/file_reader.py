""" Some examples from the chapter """

filename = 'pi_digits.txt'

print('Reading an entire file')
with open('pi_digits.txt') as f:
    contents = f.read()
    print(contents.rstrip())

print('\nreading line by line')
with open(filename) as f:
    for line in f:
        print(line.rstrip()) #rstrip → quita los espacios en blanco

print('\nMaking a list of lines')
with open(filename) as f:
    lines = f.readlines() #readlines → agrega los valores a una lista

for line in lines:
    print(line.rstrip())

print('\nWorking with a file\'s contents')
with open(filename) as f:
    lines = f.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
