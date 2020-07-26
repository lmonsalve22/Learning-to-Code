

class Restaurant:

    TODO: #see the entire chapter
    
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