""" Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default 
message, and a shirt of any size with a different message. """

def make_shirt(size='large', message='I love Python'):
    return f'The size of the shirt is: {size.title()}\nThe message is: {message}\n{"-"*50}'

print(make_shirt())
print(make_shirt(size='medium'))
print(make_shirt(size='small', message='Python rocks!!'))