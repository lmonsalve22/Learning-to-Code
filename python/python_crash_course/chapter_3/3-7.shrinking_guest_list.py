""" 
1. print that you can invite only two people
2. use pop() to remove each guest until get only two
3. print a message only for those two guests
4. use del to remove all guests and print the list """

guests = ['james', 'cynthya', 'jassany']

guests.insert(0, 'jaimes')
guests.insert(2, 'rosario')
guests.append('pacho')

print('Sorry friends, I can invite only two people') #1

guests.pop() #2
guests.pop()
guests.pop()
guests.pop()

for guest in guests: #3
    print(f'{guest.title()} you still on the list')

del guests[0] #4
del guests[0]

print(guests)