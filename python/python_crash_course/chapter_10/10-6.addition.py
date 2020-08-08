""" Write a program that prompts for two numbers. Add them together 
and print the result. Catch the TypeError if either input value is 
not a number, and print a friendly error message. Test your program 
by entering two numbers and then by entering some text instead of a
number. """

print('Give me two numbers, and I\'ll add them.')

first_number = input('First number: ')
second_number = input('Second number: ')
try:
    result = int(first_number) + int(second_number)
except ValueError: #better performance with ValueError 
    print('The value is not a number')
else:
    print(f'The answer is: {result}')

