""" Working with exercise 3-4 through 3-7 use len()
to print the number of people you are inviting to
dinner """

guests = ['james', 'cynthya', 'jassany']

print('Hi everyone, I found a bigger dinner table') #1

guests.insert(0, 'jaimes') #2
guests.insert(2, 'rosario') #3
guests.append('pacho') #4

print(f'Our new list of guests is:') #5
for guest in guests:
    print(f'- {guest.title()}')

print(f'We are {len(guests)} guests')