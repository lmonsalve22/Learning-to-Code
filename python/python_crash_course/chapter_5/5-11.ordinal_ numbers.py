""" print a list with ordinal number
but modify 1st, 2nd, 3rd """

ordinal_numbers = list(range(1,10))

for number in ordinal_numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')