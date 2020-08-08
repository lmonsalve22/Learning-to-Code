""" Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a
line recording their visit in a file called guest_book.txt. Make
sure each entry appears on a new line in the file. """

filename = 'guest.txt'

while True:
    print('For quit just enter: "q"')
    user_name = input('Hi, what\'s your name: ')
    if user_name == 'q':
        break
    else:
        print(f'Hi, {user_name.title()}')
        with open(filename, 'a') as f:
            f.write(f'{user_name}\n')