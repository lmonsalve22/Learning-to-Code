"""
1. print the guest who can't make it
2. replace for the new one
3. print the new set of invitations """


guests = ['james', 'cynthya', 'carolina']

# for guest in guests:
#     print(f'Hi {guest.title()} would you like to dinner?')

print(f'Hi everyone, but {guests[2].title()} is sick and she can\'t come') #1

guests.remove('carolina') 
guests.append('jassany') #2

for guest in guests: #3
    print(f'Hi {guest.title()} would you like to dinner?')
