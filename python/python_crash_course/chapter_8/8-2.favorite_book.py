""" Write a function called favorite_book() that accepts one
parameter, title . The function should print a message, 
such as One of my favorite books is Alice in Wonderland """

def favorite_book(title):
    return f'My favorite book is {title.title()}'

print(favorite_book('harry potter'))
print(favorite_book('narnia'))
print(favorite_book('the witcher'))