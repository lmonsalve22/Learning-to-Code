""" Using an example on the books, use some for loops
to print them """

food_1 = ['pizza', 'falafel', 'carrot cake', 'cannoli']
food_2 = ['pizza', 'falafel', 'carrot cake', 'ice cream']

print('First list:')
for i in food_1:
    print(f'- {i.title()}')

print('Second list:')
for j in food_2:
    print(f'- {j.title()}')