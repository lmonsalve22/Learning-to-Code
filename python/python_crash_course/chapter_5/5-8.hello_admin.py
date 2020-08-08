""" Make a list with 5 usernames and make an if-else statement,
for admin print an special message, but for the other just print
a simple 'hello' """

username = input('Please enter your username:\n')

usernames = ['admin', 'jamesnoria', 'jnoria', 'user95', 'ctirado']

if username in usernames and username == 'admin':
    print('Hello admin, would you like to see a status report?')
elif username in usernames:
    print(f'Hello {username}, thank you for logging in again')
else:
    print('I do not know you')