""" Making more functional exercise 7-5 """

print('=====Welcome to the cinema=====')

flag = True

tickets = []
total = []

while flag:
    ticket = int(input('Enter your age: '))
    tickets.append(ticket)
    repeat = input('Is there anyone else (y/n): ')
    if repeat == 'y':
        continue
    else:
        break

for i in tickets:
    if i < 3:
        total.append(0)
    elif i <= 12:
        total.append(10)
    else:
        total.append(15)

print(f'The total of your ticket is: {sum(total)}')