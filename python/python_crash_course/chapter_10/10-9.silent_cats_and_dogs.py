""" Modify your except block in Exercise 10-8 to fail
silently if either file is missing """

def read_files(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        pass

filenames = ['cat.txt', 'dogs.txt'] #the correct name is cats.txt
for filename in filenames:
    read_files(filename)