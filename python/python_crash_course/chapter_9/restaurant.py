""" This file was made for exercise 9-10 """

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0

    def describe_restaurant(self):
        print(f'Welcome to {self.restaurant_name.title()}')
        print(f'Our cousine type is: {self.cuisine_type.title()}')

    def open_restaurant(self):
        print(f'The {self.restaurant_name.title()} is OPEN')

    def set_number_server(self, number):
        self.number_serverd = number

    def increment_number_served(self, number):
        self.number_serverd += number
        print(f'Customers: {self.number_serverd}')

    def show_number_serverd(self):
        print(f'{self.number_serverd}')

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
  
    def display_flavors(self):
        self.flavors = ['strawberry', 'lucuma', 'chocolate', 'watermelon']
        print('FLAVORS:')
        for flavor in self.flavors:
            print(f'- {flavor.title()}')

if __name__ == "__main__":

    boy1 = IceCreamStand('Lalo Icecreams', 'ice creams')
    boy1.describe_restaurant()
    boy1.display_flavors()