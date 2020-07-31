""" Read in each line from the file you just created, learning_python.txt,
and replace the word Python with the name of another language, such
as C. Print each modified line to the screen. """

filename = './learning_python.txt'

with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        if 'Python' in line:
            c = line.replace('Python', 'C')
            print(c.strip())

def if the name of iquales main is more than just 