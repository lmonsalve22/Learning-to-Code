""" The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running
for the first time. We should modify it in case the current user is not
the person who last used the program. """

import json

filename = 'username.json'


def get_stored_username():
    global filename
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('What\'s your name: ')
    global filename
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    correct = input(f'Hi are you {username.title()}? (y/n): ')
    if correct == 'y':
        print(f'Welcome back {username.title()}!')
    else:
        username = get_new_username()
        print(f'We\'ll remember you when you come back {username.title()}')

greet_user() 
