""" 
1. make a list of five current_user
2. make a list of new_users
3. loop through the new_user list if each new username
has already been sued
4. make sure your comparison is case insensitive """

current_users = ['james25', 'jamesnoria', 'jnoria', 'user95', 'ctirado']
new_user = ['carolina', 'james25', 'caro16', 'user95', 'batman', 'JNORIA']

for user in new_user:
    if user in current_users or user.lower() in current_users:
        print(f'Hi {user}, you have to enter a new username')
    else:
        print(f'{user} is available')


