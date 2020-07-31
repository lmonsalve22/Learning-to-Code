""" Write a program that prompts for the user’s favorite number.
Use json.dump() to store this number in a file. Write a separate program 
that reads in this value and prints the message, “I know your favorite
number! It’s _____.” """

import json

fav_number = int(input('What\'s your favorite number: '))

# Saving the user's favorite number:
with open('favorite_number.json', 'w+') as f:
    json.dump(fav_number, f)

# with open('favorite_number.txt') as f:
#     content = json.load(f)
#     print(f'I know your favorite number! It\'s {content}')


