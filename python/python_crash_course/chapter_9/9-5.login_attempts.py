""" Write a method called increment_login_attempts() 
that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets
the value of login_attempts to 0. """

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


user1 = Users('james', 'noria', 'jamesnoria@gmail.com', 'jamesnoria')
user2 = Users('carolina', 'noria', 'carolinanoria@gmail.com', 'cnoria')
user3 = Users('cynthya', 'tirado', 'c_tirado@gmail.com', 'ctirado')

user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user2.describe_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.reset_login_attempts()
user3.describe_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.reset_login_attempts()
