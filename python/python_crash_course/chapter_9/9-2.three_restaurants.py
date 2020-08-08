""" Start with your class from Exercise 9-1. Create three
different instances from the class, and call 
describe_restaurant() for each instance. """

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Welcome to {self.restaurant_name.title()}')
        print(f'Our cousine type is: {self.cuisine_type.title()}')
    
    def open_restaurant(self):
        print(f'The {self.restaurant_name.title()} is OPEN')

restaurant1 = Restaurant('Don Pancho', 'fried chicken')
restaurant2 = Restaurant('American Store', 'burguer')
restaurant3 = Restaurant('Healthy place', 'burguer')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()