""" Make a list of people who should take the favorite
languages poll and then loop through the list and find
some new member for the poll """


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

names = ['james', 'sarah', 'carolina', 'edward', 'cynthya']

for name in names:
    if name in favorite_languages:
        print(f'Thanks {name.title()} for responding')
    else:
        print(f'Hi {name.title()} would you like to take the poll?')