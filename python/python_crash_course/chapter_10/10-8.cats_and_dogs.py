""" Write a program that tries to read these files and print the contents
of the file to the screen. Wrap your code in a try-except block to catch
the FileNotFound error, and print a friendly message if a file is missing. """

def read_files(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f'{filename} is not in this folder')
    
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_files(filename)
