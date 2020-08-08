""" Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , 
"can ban user" , and so on. Write a method called 
show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method. """

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
        self.privileges = []

    def show_privileges(self):
        print('ADMIN PRIVILEGES:')
        for privilege in self.privileges:
            print(f'- {privilege.title()}')


admin1 = Admin('james', 'noria', 'jamesnoria@gmail.com', 'jamesnoria')
admin1.describe_user()
admin1.privileges = ['can add post', 'can delete post',
                     'can ban user', 'can change username']

admin1.show_privileges()
