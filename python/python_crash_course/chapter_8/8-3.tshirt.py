""" Write a function called make_shirt() that accepts a size 
and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of 
the shirt and the message printed on it."""

def make_shirt(size, message):
    return f'The size of the shirt is: {size}\nThe message is: {message}\n{"-"*50}'

print(make_shirt(16,'Python is awesome'))
print(make_shirt(message='Peru is beautiful', size=15))