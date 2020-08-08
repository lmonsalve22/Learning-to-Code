# 1. Tests for equality and inequality with strings
print('='*5)
car = 'Tesla'
print(car == 'tesla')
print(car == 'Tesla')

# 2. Tests using the lower() function
print('='*5)
name = 'James'
test = name.lower() == 'james'
print(test)

# 3. Numerical tests involving equality and inequality, 
# greater than and less than, greater than or equal to, 
# and less than or equal to
print('='*5)
age = 18
print(age != 19)

20 > 10
print(20 < 10)

10 >= 10
print(10<10)
print(10==10)

# 4. Tests using the and keyword and the or keyword
print('='*5)
tickets = 5
10 >= 10
test_2 = (tickets == 5) and (10 > 10)
test_3 = (tickets == 5) or (10 > 10)
print(test_2)
print(test_3)
# 5. Test whether an item is in a list
print('='*5)
pets = ['cat', 'dog', 'mouse']
print(pets)
if 'cat' in pets:
    print(f'The {pets[0]} is a cute pet')
else:
    print('I do not like that one')

# 6. Test whether an item is not in a list
print('='*5)
foods = ['ceviche', 'peruavian beans', 'pizza']
food = 'turkey'
if food not in foods:
    print('OK')