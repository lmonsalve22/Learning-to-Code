""" Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name 
and a cuisine_type  Make a method called describe_restaurant()
that prints these two pieces of information, and a method called 
open_restaurant() that prints a message indicating that the restaurant is open. """

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Welcome to {self.restaurant_name.title()}')
        print(f'Our cousine type is: {self.cuisine_type.title()}')
    
    def open_restaurant(self):
        print(f'The {self.restaurant_name.title()} is OPEN')
    
restaurante = Restaurant('Crusteceo Carcarudo', 'fish')
restaurante.describe_restaurant()
restaurante.open_restaurant()