""" Think of fice simple food, and store the in a tuple,
1. Use a for loop to print them
2. Try to modify on of the items, and make sure that Python
rejects the change
3. replace two o the items en print it """

simple_food = ('chicken', 'ceviche', 'rice', 'pizza', 'turkey')

print('The menu is:') #1
for food in simple_food:
    print(f'- {food.title()}')

# simple_food[1] = 'peruvian beans' #2

simple_food = ('duck', 'eggs', 'rice', 'pizza', 'turkey')

print('The new menu is:') #3
for food in simple_food:
    print(f'- {food.title()}')
