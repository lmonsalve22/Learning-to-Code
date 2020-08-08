""" 
1. print that you found a bigger table
2. use insert() to add the new guest to the beginning
3. use insert() to add the new guest to the middle
4. use append() to add one new guest to the end
5. print the new invitation list """


guests = ['james', 'cynthya', 'jassany']

print('Hi everyone, I found a bigger dinner table') #1

guests.insert(0, 'jaimes') #2
guests.insert(2, 'rosario') #3
guests.append('pacho') #4

print(f'Our new list of guests is:') #5
for guest in guests:
    print(f'- {guest.title()}')