""" Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt. """

filename = 'guest.txt'

user_name = input('Hi, what\'s your name: ')

with open(filename, 'w+') as f:
    f.write(user_name)