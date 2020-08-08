""" Think of something you could store in a list.
Write a program that creates a list containing these items """

start = True
languages = []

while start:
    name = input('Hi, what\'s your name?: ')
    print(f'Welcome {name.title()}')
    fav_language = input('What is your favorite programming language?:\n')
    languages.append(fav_language)
    finish = input('would you like to continue (y/n): ')
    if finish == 'y':
        continue
    else:
        break

print('People likes the following programming languages:')
for language in languages:
    print(f'- {language.title()}')
