""" Make a class called User . Create two attributes called 
first_name and last_name , and then create several other 
attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary
of the user’s information. Make anoth """

class Users:

    def __init__(self, first_name, last_name, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username

    def describe_user(self):
        print(f'''{self.first_name.title()} {self.last_name.title()}
        - Email: {self.email}
        - Username: {self.username}''')
    
    def greet_user(self):
        print(f'Welcome {self.first_name.title()}')

user1 = Users('james', 'noria', 'jamesnoria@gmail.com', 'jamesnoria')
user2 = Users('carolina', 'noria', 'carolinanoria@gmail.com', 'cnoria')
user3 = Users('cynthya', 'tirado', 'c_tirado@gmail.com', 'ctirado')

user1.describe_user()
user2.describe_user()
user3.describe_user()
user1.greet_user()
user2.greet_user()
user3.greet_user()
