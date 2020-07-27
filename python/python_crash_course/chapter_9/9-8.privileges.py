""" Write a separate Privileges class. The class should have 
one attribute, privileges , that stores a list of strings as 
described in Exercise 9-7. Move the show_privileges() method 
to this class. Make a Privileges instance as an attribute in 
the Admin class. Create a new instance of Admin and use your
method to show its privileges. """

class Users:

    def __init__(self, first_name, last_name, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}')
        print(f'- Email: {self.email}')
        print(f'- Username: {self.username}')

    def greet_user(self):
        print(f'Welcome {self.first_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

class Admin(Users):

    def __init__(self, first_name, last_name, email, username):
        super().__init__(first_name, last_name, email, username)
        self.privileges = Privileges()

class Privileges:

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print('ADMIN PRIVILEGES:')
        if self.privileges:
            for privilege in self.privileges:
                print(f'- {privilege.title()}')
        else:
            print('No privileges')

admin1 = Admin('james', 'noria', 'jamesnoria@gmail.com', 'jamesnoria')

admin1.describe_user()

admin1.privileges.privileges = ['can post', 'can delete']

admin1.privileges.show_privileges()