""" write a in-elif-else chain that determines a person's
stage of life. Set a value for the variable age """

age = int(input('What\'s your age:\n'))

if age < 2:
    print('baby')
elif age == 2 or age < 4:
    print('toddler')
elif age == 4 or age < 13:
    print('kid')
elif age == 13 or age < 20:
    print('teenager')
elif age == 20 or age < 65:
    print('adult')
else:
    print('elder')